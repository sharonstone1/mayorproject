import Vue from 'vue'
import App from './App.vue'
import 'bootstrap/dist/js/bootstrap.bundle.min'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'font-awesome/css/font-awesome.min.css'
import './assets/restaurant.css'
import UniqueId from 'vue-unique-id'
import PortalVue from 'portal-vue'

// Vue.config.productionTip = false
Vue.config.devtools = true
Vue.use(UniqueId)
Vue.use(PortalVue)

/* eslint-disable no-new */
new Vue({
  render: h => h(App),
  el: '#app',
  template: '<App/>',
  components: { App }
})

// /* eslint-disable no-new */
// new Vue({
//   el: '#app',
//   template: '<App/>',
//   components: { App }
// }).$mount('#app')
