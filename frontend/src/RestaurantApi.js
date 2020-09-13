import axios from 'axios'

const client = axios.create({
  baseURL: '/api'
})

export default {
  getDishes: function () {
    return client.get('/dishes/')
  },
  makeDeliveryOrder: function (order) {
    return client.post('/orders/', order)
  },
  makeTableBooking: function (booking) {
    return client.post('/table-booking/', booking)
  },
  makeEventPreBooking: function (booking) {
    return client.post('/event-pre-booking/', booking)
  },
  utils: {
    getDayDisplayName (day) {
      const dayToText = {
        MO: 'Monday',
        TU: 'Tuesday',
        WE: 'Wednesday',
        TH: 'Thursday',
        FR: 'Friday',
        SA: 'Saturday',
        SU: 'Sunday',
        '*': 'Everyday'
      }
      return dayToText[day]
    }
  }
}
