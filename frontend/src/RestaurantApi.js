import axios from 'axios'

// The axios client used by the application.
const client = axios.create({
  baseURL: '/api', // base path to access the server REST API
  // configure CSRF token posted in request, the CSRF token is present in the cookie csrftoken.
  // Axios adds to the request and HTTP header named X-CSRFToken with its value.
  xsrfCookieName: 'csrftoken',
  xsrfHeaderName: 'X-CSRFToken',
  withCredentials: true
})

// API to access the restaurant REST API
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
  addOrderItem (item) {
    return client.post('/orders-items/', item)
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
  profile: function () {
    return client.get('/auth/profile/')
  },
  getTableBookings (queryParameters = {}) {
    const query = this.makeQueryString(queryParameters)
    return client.get('/table-booking/' + query)
  },
  getDeliveryOrders (queryParameters = {}) {
    const query = this.makeQueryString(queryParameters)
    return client.get('/orders/' + query)
  },
  getLessonBookings (queryParameters = {}) {
    const query = this.makeQueryString(queryParameters)
    return client.get('/cooking-lessons/' + query)
  },
  getEventBookings (queryParameters = {}) {
    const query = this.makeQueryString(queryParameters)
    return client.get('/event-pre-booking/' + query)
  },
  // Construct the query parameter part of a URL, this function accept and object
  // in input. Each set of key/value will be added to the query.
  makeQueryString (queryParameters) {
    let query = ''
    for (const [key, value] of Object.entries(queryParameters)) {
      if (query !== '') {
        query += '&'
      }
      query += `${key}=${value}`
    }
    if (query !== '') {
      query = '?' + query
    }
    return query
  },
  client: function () {
    return client
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
  },
  options: {
    classTypes: {
      stream: 'Live streaming',
      live: 'At the restaurant'
    },
    classTime: {
      morning: '8 o\'clock until lunch',
      afternoon: '15 o\'clock until dinner'
    }
  }
}
