<!-- Wrapper around one of the booking component. It puts the component in a Modal. Fetching booking data is made according
 to the date configured in a date input -->

<template>
  <Modal :title="title" extra-class="modal-xl" :modal-id="modalId">
    <h2>{{title}}</h2>
    <input type="date" class="form-control" v-model="date">

    <!-- Dynamically render the vue component passed as the bookingComponent props-->
    <component :is="bookingComponent" :bookings="bookings" v-bind="$attrs"/>
  </Modal>
</template>

<script>
import Modal from '@/components/common/Modal'
export default {
  name: 'AdminBooking',
  components: { Modal },
  props: {
    title: String, // Name of the modal
    getBookings: Function, // Function to retrieve the bookings from the REST API
    bookingComponent: Object, // Booking component to display
    modalId: String // id of the modal
  },
  data () {
    return {
      date: (new Date()).toISOString().substring(0, 10), // Initial date is today
      bookings: []
    }
  },
  methods: {
    // get the bookings from the REST API
    fetchBookings () {
      const app = this
      this.getBookings({ date: this.date })
        .then(function (response) {
          // Update the view
          app.bookings = response.data
        })
    }
  },
  mounted () {
    this.fetchBookings()
  },
  watch: {
    // When the date change, the list of bookings is refreshed
    date (newDate, oldDate) {
      this.fetchBookings()
    }
  }
}
</script>

<style scoped>

</style>
