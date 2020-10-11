<template>
  <Modal :title="title" extra-class="modal-xl" :modal-id="modalId">
    <h2>{{title}}</h2>
    <input type="date" class="form-control" v-model="date">

    <component :is="bookingComponent" :bookings="bookings" v-bind="$attrs"/>
  </Modal>
</template>

<script>
import Modal from '@/components/common/Modal'
export default {
  name: 'AdminBooking',
  components: { Modal },
  props: {
    title: String,
    getBookings: Function,
    bookingComponent: Object,
    modalId: String
  },
  data () {
    return {
      date: (new Date()).toISOString().substring(0, 10),
      bookings: []
    }
  },
  methods: {
    fetchBookings () {
      const app = this
      this.getBookings({ date: this.date })
        .then(function (response) {
          app.bookings = response.data
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
