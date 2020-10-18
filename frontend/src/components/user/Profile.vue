<template>
  <div v-if="profile">
    <Modal modal-id="modalId-profile" :title="`Welcome ${profile.username}`" extra-class="modal-xl">
      <div v-if="profile.table_bookings.length  > 0">
        <h2>Bookings</h2>
        <AdminTableBooking :bookings="profile.table_bookings"/>
      </div>

      <div v-if="profile.delivery_orders.length > 0">
        <h2>Delivery</h2>
        <AdminDelivery :bookings="profile.delivery_orders" :menus="menus" portal-target="profileDeliveryOrderModals"/>
      </div>

      <div v-if="profile.cooking_lessons.length > 0">
        <h2>Cooking lessons</h2>
        <AdminCookingLesson :bookings="profile.cooking_lessons"/>
      </div>

      <div v-if="profile.events.length > 0">
        <h2>Events Pre bookings</h2>
        <AdminEvents :bookings="profile.events"/>
      </div>

    </Modal>

    <PortalTarget name="profileDeliveryOrderModals" multiple="true"/>
  </div>
</template>

<script>
import EventBus from '@/EventBus'
import RestaurantApi from '@/RestaurantApi'
import Modal from '@/components/common/Modal'
import AdminTableBooking from '@/components/common/management/AdminTableBooking'
import AdminDelivery from '@/components/common/management/AdminDelivery'
import AdminCookingLesson from '@/components/common/management/AdminCookingLesson'
import AdminEvents from '@/components/common/management/AdminEvents'
import { Portal, PortalTarget } from 'portal-vue'

export default {
  name: 'Profile',
  props: ['modalId', 'menus'],
  components: {
    AdminDelivery,
    Modal,
    AdminTableBooking,
    AdminCookingLesson,
    AdminEvents,
    PortalTarget,
    Portal // eslint-disable-line vue/no-unused-components
  },
  data () {
    return {
      userLogged: false,
      profile: null
    }
  },
  methods: {
    fetchUserProfile () {
      const app = this
      RestaurantApi.profile()
        .then(function (response) {
          app.profile = response.data
          if (!app.userLogged) {
            EventBus.emit(EventBus.LOGIN, { source: app })
          }
          EventBus.emit(EventBus.PROFILE_FETCHED, app.profile)
          app.userLogged = true
        })
        .catch(function (error) {
          console.log('Failed at fetching user profile: ' + error)
        })
    },
    onBookingAdded (container, booking) {
      if (!this.profile || !this.userLogged) {
        return
      }
      container.push(booking)
    }
  },
  mounted () {
    const app = this
    // Register events
    EventBus.on(EventBus.LOGIN, function (e) {
      app.userLogged = true
      if (e && e.source === app) {
        return
      }
      app.fetchUserProfile()
    })
    EventBus.on(EventBus.LOGOUT, function () {
      app.profile = null
      app.userLogged = false
    })
    EventBus.on(EventBus.TABLE_BOOKING, function (booking) {
      app.onBookingAdded(app.profile.table_bookings, booking)
    })
    EventBus.on(EventBus.DELIVERY_ORDER, function (booking) {
      app.onBookingAdded(app.profile.delivery_orders, booking)
    })
    EventBus.on(EventBus.EVENT_BOOKING, function (booking) {
      app.onBookingAdded(app.profile.events, booking)
    })
    EventBus.on(EventBus.COOKING_LESSON_BOOKING, function (booking) {
      app.onBookingAdded(app.profile.cooking_lessons, booking)
    })

    // Fetch the user profile
    app.fetchUserProfile()
  }
}
</script>

<style scoped>

</style>
