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
        <div class="navbar-nav ml-auto"  v-show="userLogged == false">
          <a class="nav-item nav-link" data-toggle="modal" data-target="#loginModal"  href="#login">
            Login
          </a>
          <a class="nav-item nav-link" data-toggle="modal" data-target="#registerModal" href="#register">
            Sign up
          </a>
        </div>
        <div class="navbar-nav ml-auto"  v-show="userLogged == true">
          <a class="nav-item nav-link" href="#logout" @click="logout">
            Logout
          </a>
          <a class="nav-item nav-link" href="#profile">
            Profile
          </a>
        </div>

      </div>
    </nav>

<!--    Login Modal -->
    <Login modal-id="loginModal"/>
    <UserRegistration modal-id="registerModal"/>
  </div>

</template>

<script>
import Login from '@/components/Login'
import UserRegistration from '@/components/UserRegistration'
import RestaurantApi from '@/RestaurantApi'
import EventBus from '@/EventBus'
export default {
  name: 'Navbar',
  components: { UserRegistration, Login },
  props: ['navigation'],
  data () {
    return {
      userLogged: false
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
  }
}
</script>

<style scoped>

</style>
