import Vue from 'vue'

const _EventBus = new Vue()

const EventBus = {
  emit (eventName, ...args) {
    _EventBus.$emit(eventName, ...args)
  },
  on (eventName, callback) {
    _EventBus.$on(eventName, callback)
  },
  off (eventName, callback) {
    _EventBus.$off(eventName, callback)
  },
  LOGIN: 'user-log-in',
  LOGOUT: 'user-log-out',
  TABLE_BOOKING: 'user-table-booking',
  DELIVERY_ORDER: 'user-delivery-order',
  COOKING_LESSON_BOOKING: 'user-cooking-lesson-booking',
  EVENT_BOOKING: 'user-event-booking',
  ADMIN_DISH_AVAILABLE: 'admin-dish-available',
  PROFILE_FETCHED: 'profile-fetched',
  DISHES_UPDATES: 'admin-has-updated-dishes',
  MENUS_UPDATED: 'menus-updated'
}

export default EventBus
