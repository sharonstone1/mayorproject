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
    },
    onTableBooking (booking) {
      if (!this.profile || !this.userLogged) {
        return
      }
      this.profile.table_bookings.push(booking)
    },
    onDeliveryOrder (order) {
      if (!this.profile || !this.userLogged) {
        return
      }
      this.profile.delivery_orders.push(order)
    },
    onEventBooking (booking) {
      if (!this.profile || !this.userLogged) {
        return
      }
      this.profile.events.push(booking)
    },
    onCookingLessonBooking (booking) {
      if (!this.profile || !this.userLogged) {
        return
      }
      this.profile.cooking_lessons.push(booking)
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
    EventBus.on(EventBus.TABLE_BOOKING, this.onTableBooking)
    EventBus.on(EventBus.DELIVERY_ORDER, this.onDeliveryOrder)
    EventBus.on(EventBus.EVENT_BOOKING, this.onEventBooking)
    EventBus.on(EventBus.COOKING_LESSON_BOOKING, this.onCookingLessonBooking)

    // Fetch the user profile
    app.fetchUserProfile()
  }
}
</script>

<style scoped>

</style>
