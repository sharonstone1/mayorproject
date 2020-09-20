import axios from 'axios'

const client = axios.create({
  baseURL: '/api',
  xsrfCookieName: 'csrftoken',
  xsrfHeaderName: 'X-CSRFToken',
  withCredentials: true
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
  makeLessonBooking: function (booking) {
    return client.post('/cooking-lessons/', booking)
  },
  login: function (credentials) {
    return client.post('/auth/login/', credentials)
  },
  logout: function () {
    return client.post('/auth/logout/')
  },
  register: function (registration) {
    return client.post('/auth/register/', registration)
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
