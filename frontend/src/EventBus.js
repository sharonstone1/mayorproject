import Vue from 'vue'

const _EventBus = new Vue()

const EventBus = {
  emit (eventName, ...args) {
    _EventBus.$emit(eventName, args)
  },
  on (eventName, callback) {
    _EventBus.$on(eventName, callback)
  },
  off (eventName, callback) {
    _EventBus.$off(eventName, callback)
  },
  LOGIN: 'user-log-in',
  LOGOUT: 'user-log-out'
}

export default EventBus
