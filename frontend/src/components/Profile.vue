<template>
  <div></div>
</template>

<script>
import EventBus from '@/EventBus'
import RestaurantApi from '@/RestaurantApi'

export default {
  name: 'Profile',
  props: ['modalId'],
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
          app.userLogged = true
        })
        .catch(function (error) {
          console.log('Failed at fetching user profile: ' + error)
        })
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

    // Fetch the user profile
    app.fetchUserProfile()
  }
}
</script>

<style scoped>

</style>
