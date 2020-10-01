<template>
  <div class="container">
    <form v-for="booking in bookings"
          :id="getFormId(booking)"
          :key="getFormId(booking)"
          @submit.prevent="updateBooking(booking)"
          hidden
    ></form>

    <table class="table table-hover table-responsive">
      <thead>
        <tr>
          <th scope="col">Name</th>
          <th scope="col">Date</th>
          <th scope="col">Time</th>
          <th scope="col">Type</th>
          <th scope="col">Contact</th>
          <th scope="col"></th>
          <th scope="col"></th>
        </tr>
      </thead>
      <tbody>
        <template v-for="(booking, index) in bookings">
          <tr :key="booking.url">
            <td>{{ booking.fullname }}</td>
            <td><input type="date" v-model="booking.date" :form="getFormId(booking)"></td>
            <td><VSelect :options="$options.classType" v-model="booking.type" :form="getFormId(booking)"/></td>
            <td><VSelect :options="$options.classTime" v-model="booking.time" :form="getFormId(booking)"/></td>
            <td>
              <ul>
                <li>{{ booking.email }}</li>
                <li>{{ booking.phone_number }}</li>
                <li>{{ booking.address }}</li>
              </ul>
            </td>
            <td>
              <button class="btn btn-primary" :form="getFormId(booking)">Update</button>
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
import VSelect from '@/components/common/form/VSelect'

export default {
  name: 'AdminCookingLesson',
  components: { VSelect },
  props: {
    bookings: Array
  },
  methods: {
    updateBooking (booking) {
      RestaurantApi.client().put(booking.url, booking)
        .then(function (response) {
          booking = response.data
        })
        .catch(function (error) {
          console.log(`failed to update ${booking.url}: ${error}`)
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
    },
    getFormId (booking) {
      return `admin-form-cooking-update-${booking.url}`
    }
  },
  created () {
    // Import options from the Restaurant API
    this.$options.classType = RestaurantApi.options.classTypes
    this.$options.classTime = RestaurantApi.options.classTime
  }
}
</script>

<style scoped>

</style>
