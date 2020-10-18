import Vue from 'vue'
import App from './App.vue'
import 'bootstrap/dist/js/bootstrap.bundle.min'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'font-awesome/css/font-awesome.min.css'
import './assets/restaurant.css'
import UniqueId from 'vue-unique-id'
import PortalVue from 'portal-vue'

// Configure vue
Vue.config.devtools = true
Vue.use(UniqueId)
Vue.use(PortalVue)

// Create the application instance of vue
/* eslint-disable no-new */
new Vue({
  render: h => h(App),
  el: '#app',
  template: '<App/>',
  components: { App }
})
