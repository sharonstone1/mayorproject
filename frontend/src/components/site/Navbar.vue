<template>

  <div>
    <!--    Nav bar-->
    <nav class="navbar navbar-expand-md navbar-dark bg-dark fixed-top">
      <a class="navbar-brand" href="#">
        <img alt="Aux delices de sharon" height="34" src="static/media/logorestaurant.jpg" width="38">
      </a>
      <button class="navbar-toggler" data-target="#navbarCollapse" data-toggle="collapse" type="button">
        <span class="navbar-toggler-icon"/>
      </button>

      <div class="collapse navbar-collapse" id="navbarCollapse">

        <!-- Dynamic part of the navbar, it depends on the navigation prop -->
        <div class="navbar-nav ">
          <div v-for="(navElement, index) in navigation" :key="'navbar-root-' + index">
            <!-- Two types of elements can be rendered, composite and and single item-->
            <a v-if="!navElement.children"
               class="nav-item nav-link"
               :href="navElement.id">
              {{navElement.name}}
            </a>

            <!-- Composite navigation element -->
            <div v-else class="nav-item dropdown">
              <a
                class="nav-link dropdown-toggle"
                data-toggle="dropdown"
                :href="navElement.id"
              >
                {{ navElement.name }}
              </a>
              <div class="dropdown-menu">
                <a
                  v-for="(child, childIndex) in navElement.children"
                  class="dropdown-item"
                  :href="child.id"
                  :key="'navbar-root-' + index + '-' + childIndex"
                >
                  {{ child.name }}
                </a>
              </div>
            </div>
          </div>
        </div>

        <!-- Login and registration links are always here -->
        <div v-if="userLogged == false" class="navbar-nav ml-auto">
          <a class="nav-item nav-link" data-toggle="modal" data-target="#loginModal" href="#">Login</a>
          <a class="nav-item nav-link" data-toggle="modal" data-target="#registerModal" href="#">Sign up</a>
        </div>

        <div v-else class="navbar-nav ml-auto">
          <!-- Bookings administration -->
          <div class="nav-item dropdown" v-if="isStaff">
            <a class="nav-link dropdown-toggle"  data-toggle="dropdown">
              Bookings
            </a>
            <div class="dropdown-menu">
              <!-- Cooking lessons -->
              <a href="#ManagerAdminCookingLessons" data-toggle="modal" data-target="#ManagerAdminCookingLessons" class="dropdown-item">
                  Cooking Lessons
              </a>
              <!--  booking table -->
              <a href="#ManagerAdminTableBooking" data-toggle="modal" data-target="#ManagerAdminTableBooking" class="dropdown-item">
                  Booking table
              </a>
              <!--  pre booking event -->
              <a href="#ManagerAdminEventPreBooking" data-toggle="modal" data-target="#ManagerAdminEventPreBooking" class="dropdown-item">
                  Event Pre-Booking
              </a>
              <!-- Delivery order -->
              <a href="#ManagerAdminDeliveryOrder" data-toggle="modal" data-target="#ManagerAdminDeliveryOrder" class="dropdown-item">
                  Delivery Order
              </a>
            </div>
          </div>

          <!-- Dish administration -->
          <div class="nav-item dropdown" v-if="adminDish.length != 0 && isStaff">
            <a class="nav-link dropdown-toggle"  data-toggle="dropdown">
              Edit Dishes
            </a>
            <div class="dropdown-menu">
                <a v-for="dishCategory in adminDish" :key="`navbar-${dishCategory}`"
                  class="dropdown-item"
                   data-toggle="modal" :data-target="`#modalId-${dishCategory}`" :href="`#${dishCategory}`">
                  {{dishCategory}}
                </a>
            </div>
          </div>

          <a class="nav-item nav-link" href="#logout" @click="logout">
            Logout
          </a>
          <a class="nav-item nav-link" href="#profile" data-toggle="modal" data-target="#modalId-profile">
            Profile
          </a>
        </div>

      </div>
    </nav>

    <!--    Associated Modals -->
    <div v-if="!userLogged">
      <Login modal-id="loginModal"/>
      <UserRegistration modal-id="registerModal"/>
    </div>
    <div v-else-if="isStaff">
      <AdminBooking
        title="Cooking lessons"
        :booking-component="$options.components.AdminCookingLesson"
        :get-bookings="api.getLessonBookings.bind(api)"
        modal-id="ManagerAdminCookingLessons"
      />

      <AdminBooking
        title="Booking Table"
        :booking-component="$options.components.AdminTableBooking"
        :get-bookings="api.getTableBookings.bind(api)"
        modal-id="ManagerAdminTableBooking"
      />

      <AdminBooking
        title="Event Pre-Booking"
        :booking-component="$options.components.AdminEvents"
        :get-bookings="api.getEventBookings.bind(api)"
        modal-id="ManagerAdminEventPreBooking"
      />

      <AdminBooking
        title="Delivery Order"
        :booking-component="$options.components.AdminDelivery"
        :get-bookings="api.getDeliveryOrders.bind(api)"
        modal-id="ManagerAdminDeliveryOrder"
        :menus="menus"
        portal-target="adminDeliveryOrderModals"
      />

      <AdminDish/>
      <PortalTarget name="adminDeliveryOrderModals" multiple/>
    </div>

    <!-- The profile is always loaded but is not displayed if not available -->
    <Profile :menus="menus"/>
  </div>
</template>

<script>
import RestaurantApi from '@/RestaurantApi'
import EventBus from '@/EventBus'
import AdminDish from '@/components/admin/AdminDish'
import Login from '@/components/user/Login'
import Profile from '@/components/user/Profile'
import UserRegistration from '@/components/user/UserRegistration'
import AdminCookingLesson from '@/components/common/management/AdminCookingLesson'
import AdminBooking from '@/components/admin/AdminBooking'
import AdminTableBooking from '@/components/common/management/AdminTableBooking'
import AdminEvents from '@/components/common/management/AdminEvents'
import AdminDelivery from '@/components/common/management/AdminDelivery'
import { Portal, PortalTarget } from 'portal-vue'

export default {
  name: 'Navbar',

  components: {
    AdminDish,
    Login,
    Profile,
    UserRegistration,
    AdminBooking,
    Portal, // eslint-disable-line vue/no-unused-components
    AdminCookingLesson, // eslint-disable-line vue/no-unused-components
    AdminTableBooking, // eslint-disable-line vue/no-unused-components
    AdminEvents, // eslint-disable-line vue/no-unused-components
    AdminDelivery, // eslint-disable-line vue/no-unused-components
    PortalTarget
  },
  props: ['navigation', 'menus'],
  data () {
    return {
      userLogged: false,
      isStaff: false,
      adminDish: [],
      api: RestaurantApi
    }
  },
  methods: {
    logout () {
      RestaurantApi.logout()
        .then(function (response) {
          EventBus.emit(EventBus.LOGOUT)
        })
        .catch(function (error) {
          console.log('failure while logging out: ' + error)
        })
    }
  },
  mounted () {
    const app = this
    EventBus.on(EventBus.LOGIN, function () {
      app.userLogged = true
    })
    EventBus.on(EventBus.LOGOUT, function () {
      app.userLogged = false
    })
    EventBus.on(EventBus.ADMIN_DISH_AVAILABLE, function (dishes) {
      app.adminDish = dishes
    })
    EventBus.on(EventBus.PROFILE_FETCHED, function (profile) {
      app.isStaff = profile.is_staff
    })
  }
}
</script>

<style scoped>

</style>
