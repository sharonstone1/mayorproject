<!-- Administration of table booking -->

<template>
  <div class="container">
    <form v-for="booking in bookings"
          :id="`form-${booking.url}`"
          :key="`form-${booking.url}`"
          @submit.prevent="updateForm(booking)"
    ></form>

    <table class="table table-hover table-responsive">
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
        <template v-for="(booking, index) in bookings">
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
              <button class="btn btn-warning" @click="deleteBooking(booking, index)">Cancel</button>
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
  props: {
    bookings: Array
  },
  methods: {
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
    },
    deleteBooking (booking, index) {
      const app = this
      RestaurantApi.client().delete(booking.url)
        .then(function (response) {
          app.bookings.splice(index, 1)
        })
        .catch(function (error) {
          console.log(`failed to delete ${booking.url}: ${error}`)
        })
    }
  }
}
</script>

<style scoped>

</style>
