import Vue from 'vue'

const _EventBus = new Vue()

/* Global event bus used to share events between components */
const EventBus = {
  /* Emit an event that will be catch by all registered event handlers */
  emit (eventName, ...args) {
    _EventBus.$emit(eventName, ...args)
  },
  /* Subscribe to a specific event */
  on (eventName, callback) {
    _EventBus.$on(eventName, callback)
  },
  /* *Unsubscribe from a specific event */
  off (eventName, callback) {
    _EventBus.$off(eventName, callback)
  },
  LOGIN: 'user-log-in', /* called when the user is logged in */
  LOGOUT: 'user-log-out', /* called when the user is logged out */
  TABLE_BOOKING: 'user-table-booking', /* called when a table booking as been made */
  DELIVERY_ORDER: 'user-delivery-order', /* called when a Delivery has been booked */
  COOKING_LESSON_BOOKING: 'user-cooking-lesson-booking', /* called when a cooking lesson has been booked */
  EVENT_BOOKING: 'user-event-booking', /* called when an event booking has been made */
  ADMIN_DISH_AVAILABLE: 'admin-dish-available', /* Called when the dishes have been fetched */
  PROFILE_FETCHED: 'profile-fetched', /* Called when the user profile has been fetched */
  DISHES_UPDATES: 'admin-has-updated-dishes', /* Called when the list of dishes has been updates */
  MENUS_UPDATED: 'menus-updated' /* Called when the menus have been updated */
}

export default EventBus
