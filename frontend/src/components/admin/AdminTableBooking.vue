<template>
  <div class="container">
    <input type="date" v-model="date">

    <form v-for="booking in bookings"
          :id="`form-${booking.url}`"
          :key="`form-${booking.url}`"
          @submit.prevent="updateForm(booking)"
    ></form>

    <table class="table table-hover">
      <thead>
        <tr>
          <th scope="col">Name</th>
          <th scope="col">Date</th>
          <th scope="col">Time</th>
          <th scope="col">Guests</th>
          <th scope="col">Contact</th>
          <th scope="col"></th>
          <th scope="col"></th>
        </tr>
      </thead>
      <tbody>
        <template v-for="booking in bookings">
          <tr :key="booking.url">
            <td>{{ booking.fullname }}</td>
            <td><input type="date" v-model="booking.date" :form="`form-${booking.url}`"></td>
            <td><input type="time" v-model="booking.time" :form="`form-${booking.url}`"></td>
            <td><input type="number" v-model="booking.guest_count" :form="`form-${booking.guest_count}`"></td>
            <td>
              <ul>
                <li>{{ booking.phone_number }}</li>
                <li>{{ booking.email }}</li>
              </ul>
            </td>
            <td>
              <button class="btn btn-primary" :form="`form-${booking.url}`">Update</button>
            </td>
            <td>
              <button class="btn btn-warning">Cancel</button>
            </td>
          </tr>
        </template>
      </tbody>
    </table>
  </div>
</template>

<script>
import RestaurantApi from '@/RestaurantApi'

export default {
  name: 'AdminTableBooking',
  data () {
    return {
      date: (new Date()).toISOString().substring(0, 10),
      bookings: []
    }
  },
  methods: {
    fetchBookings () {
      const app = this
      RestaurantApi.getTableBookings({ date: this.date })
        .then(function (response) {
          app.bookings = response.data
        })
    },
    updateForm (booking) {
      const app = this
      const client = RestaurantApi.client()
      client.put(booking.url, booking)
        .then(function (response) {
          if (response.data.date !== app.date) {
            console.log('element must be removed from the view!')
          }
        })
        .catch(function (error) {
          console.log(`failure ${error} while updating resource: ${booking.url}`)
        })
    }
  },
  mounted () {
    this.fetchBookings()
  },
  watch: {
    date (newDate, oldDate) {
      this.fetchBookings()
    }
  }
}
</script>

<style scoped>

</style>
