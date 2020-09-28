<template>
  <div v-if="profile">
    <div class="container">
      <div class="modal fade" id="modalId-profile" tabindex="-1" role="dialog" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered modal-xl" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title">Welcome {{profile.username}}</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>

            <div class="modal-body">
              <!--booking details-->
              <div v-if="profile.table_bookings.length > 0">
                <h2>Bookings</h2>
                <table class="table table-hover">
                  <thead>
                    <tr>
                      <th scope="col">Date</th>
                      <th scope="col">Time</th>
                      <th scope="col">Guests</th>
                      <th scope="col">Type</th>
                      <th></th>
                    </tr>
                  </thead>
                  <tbody>
                    <template v-for="booking in profile.table_bookings">
                      <tr :key="booking.url">
                        <td>{{ booking.date }}</td>
                        <td>{{ booking.time }}</td>
                        <td>{{ booking.guest_count }}</td>
                        <td>{{ booking.vip ? "VIP" : "Standard" }}</td>
                        <td><button @click="removeTableBooking(booking)" class="btn btn-warning">Cancel</button></td>
                      </tr>
                    </template>
                  </tbody>
                </table>
              </div>

              <!--delivery information-->
              <h2>Delivery</h2>
              <div v-if="profile.delivery_orders.length !== 0">
              <table  class="table table-hover">
                <thead>
                  <tr>
                    <th scope="col">Info</th>
                    <th scope="col">Details</th>
                    <th scope="col"></th>
                  </tr>
                </thead>
                <tbody>
                  <template v-for="order in profile.delivery_orders">
                    <tr :key="order.url">
                      <td>
                        <ul>
                          <li>Date: {{order.date}}</li>
                          <li>Time: {{order.time}}</li>
                          <li>Address: {{order.address}}</li>
                          <li>Total Price: {{getOrderTotalPrice(order)}}
                        </ul>
                      </td>
                      <td>
                        <table class="table table-bordered">
                          <thead>
                            <tr>
                              <th scope="col">Dish</th>
                              <th scope="col">Price</th>
                              <th scope="col">Count</th>
                              <th scope="col"></th>
                            </tr>
                          </thead>
                          <tbody>
                            <template v-for="item in order.items">
                              <tr :key="item.url">
                                <td>{{ getDishName(item.dish) }}</td>
                                <td>{{ getDishPrice(item.dish) }}</td>
                                <td>{{item.count}}</td>
                                <td><button @click="removeDeliveryItem(order,item)" class="btn btn-warning">Remove</button></td>
                              </tr>
                            </template>
                          </tbody>
                        </table>
                      </td>
                      <td><button @click="removeDelivery(order)" class="btn btn-warning">Cancel</button></td>
                    </tr>
                  </template>
                </tbody>
              </table>
             </div>

              <!--      cooking lessons details-->
              <div v-if="profile.cooking_lessons.length > 0">
                <h2>Cooking Lessons</h2>
                <table class="table table-hover">
                  <thead>
                    <tr>
                      <th scope="col">Date</th>
                      <th scope="col">Time</th>
                      <th scope="col">Type</th>
                      <th scope="col"></th>
                    </tr>
                  </thead>
                  <tbody>
                    <template v-for="lesson in profile.cooking_lessons">
                      <tr :key="lesson.url">
                        <td>{{ lesson.date }}</td>
                        <td>{{ lesson.time }}</td>
                        <td>{{ lesson.type }}</td>
                        <td><button @click="removeCookingLesson(lesson)" class="btn btn-warning">Cancel</button></td>
                      </tr>
                    </template>
                  </tbody>
                </table>
              </div>

              <!--      events details-->
              <div v-if="profile.events.length > 0">
                <h2>My pre-booking Events</h2>
                <table class="table table-hover">
                  <thead>
                    <tr>
                      <th scope="col">Address</th>
                      <th scope="col">Date</th>
                      <th scope="col">Time</th>
                      <th scope="col"></th>
                    </tr>
                  </thead>
                  <tbody>
                    <template v-for="event in profile.events">
                      <tr :key="event.url">
                        <td>{{ event.address }}</td>
                        <td>{{ event.date }}</td>
                        <td>{{ event.time }}</td>
                        <td><button @click="removeEventPreBooking(event)" class="btn btn-warning">Cancel</button></td>
                      </tr>
                    </template>
                  </tbody>
                </table>
              </div>
            </div>
          </div>

        </div>
      </div>

    </div>
  </div>
</template>

<script>
import EventBus from '@/EventBus'
import RestaurantApi from '@/RestaurantApi'

export default {
  name: 'Profile',
  props: ['modalId', 'dishes'],
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
    onTableBooking (booking) {
      if (!this.profile || !this.userLogged) {
        return
      }
      this.profile.table_bookings.push(booking)
    },
    removeTableBooking (booking) {
      const app = this
      RestaurantApi.client().delete(booking.url)
        .then(function (response) {
          console.log('item deleted: ' + response.data)
          const bookings = app.profile.table_bookings
          const index = bookings.indexOf(booking)
          bookings.splice(index, 1)
        })
        .catch(function (error) {
          console.log('failed to delete item: ' + error)
        })
    },
    onDeliveryOrder (order) {
      if (!this.profile || !this.userLogged) {
        return
      }
      this.profile.delivery_orders.push(order)
    },
    removeDeliveryItem (order, item) {
      RestaurantApi.client().delete(item.url)
        .then(function (response) {
          console.log('delivery order item deleted: ' + response.data)
          const index = order.items.indexOf(item)
          order.items.splice(index, 1)
        })
        .catch(function (error) {
          console.log('failed to delete delivery order item: ' + error)
        })
    },
    removeDelivery (order) {
      const app = this
      RestaurantApi.client().delete(order.url)
        .then(function (response) {
          console.log('delivery order deleted: ' + response.data)
          const orders = app.profile.delivery_orders
          const index = orders.indexOf(order)
          orders.splice(index, 1)
        })
        .catch(function (error) {
          console.log('failed to delete item: ' + error)
        })
    },
    onEventBooking (booking) {
      if (!this.profile || !this.userLogged) {
        return
      }
      this.profile.events.push(booking)
    },
    removeEventPreBooking (event) {
      const app = this
      RestaurantApi.client().delete(event.url)
        .then(function (response) {
          console.log('event pre-booking deleted: ' + response.data)
          const eventsBooking = app.profile.events
          const index = eventsBooking.indexOf(event)
          eventsBooking.splice(index, 1)
        })
        .catch(function (error) {
          console.log('failed to delete event pre-booking: ' + error)
        })
    },
    onCookingLessonBooking (booking) {
      if (!this.profile || !this.userLogged) {
        return
      }
      this.profile.cooking_lessons.push(booking)
    },
    removeCookingLesson (lesson) {
      const app = this
      RestaurantApi.client().delete(lesson.url)
        .then(function (response) {
          console.log('lesson deleted: ' + response.data)
          const lessons = app.profile.cooking_lessons
          const index = lessons.indexOf(lesson)
          lessons.splice(index, 1)
        })
        .catch(function (error) {
          console.log('failed to delete lesson: ' + error)
        })
    },
    getDishDetail (url) {
      if (this.dishes) {
        for (const dish of this.dishes) {
          if (dish.url === url) {
            return dish
          }
        }
      }
    },
    getDishName (url) {
      const dish = this.getDishDetail(url)
      return dish ? dish.title : ''
    },
    getDishPrice (url) {
      const dish = this.getDishDetail(url)
      return dish ? dish.price : ''
    },
    getOrderTotalPrice (order) {
      let price = 0
      for (const item of order.items) {
        price += item.count * this.getDishPrice(item.dish)
      }
      return price
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
