<template>
  <div class="container">
    <h2>{{title}}</h2>
    <slot></slot>
    <form v-on:submit.prevent="submitForm">
      <TextInput
        id="inputUserName"
        label="Name"
        placeholder="Name"
        type="text"
        v-model="form.fullname"
        v-show="userLogged == false"
      />
      <TextInput
        id="inputUserEmail"
        label="Email"
        placeholder="Email"
        type="email"
        v-model="form.email"
        v-show="userLogged == false"
      />
      <TextInput
        id="phone-input"
        label="Telephone"
        placeholder="Telephone number"
        type="tel"
        v-model="form.phone_number"
      />
      <TextInput
        id="inputUserAddress"
        label="Address"
        placeholder="Address"
        type="address"
        v-model="form.address"
      />
      <DateInput
        id="inputDate"
        label="Start date:"
        max="2030-07-22"
        min="2020-07-22"
        v-model="form.date"
      />
      <TimeInput
        id="inputTime"
        label="Time"
        min="12:00"
        max="23:59"
        v-model="form.time"
      />
    </form>

    <br>

    <h5>My order form</h5>

    <div class="form">
      <div class="form-group row">
        <label
          class="col-form-label col-sm-3"
          for="courseTypeSelect"
        >Course Type</label>
        <div class="col-sm-9">
          <select
            class="form-control"
            id="courseTypeSelect"
            name="course type"
            v-model="selection.dishType"
            :disabled="deliveryItemReadOnly"
          >
            <option
              v-for="(menu, type, index) in deliveryMenu"
              :value="type"
              :key="'order-dish-type-' + index"
            >
              {{ type }}
            </option>
          </select>
        </div>
      </div>

      <div class="form-group row">
        <label class="col-form-label col-sm-3">Course</label>
        <div class="col-sm-9">
          <select
            class="form-control"
            name="course"
            v-model="selection.dish"
            :disabled="deliveryItemReadOnly"
          >
            <option
              :value="index"
              v-for="(menu, index) in deliveryMenu[selection.dishType]"
              :key="'order-dish-select-' + index"
            >
              {{ menu.title }}
            </option>
          </select>
        </div>
      </div>

      <div class="form-group row">
        <label class="col-form-label col-sm-3">Count</label>
        <div class="col-sm-9">
          <input
            class="form-control"
            type="number"
            v-model="selection.count"
            :readonly="deliveryItemReadOnly"
          >
        </div>
      </div>

      <div class="form-group row">
        <div class="offset-sm-3 col-sm-9">
          <button
            class="btn btn-primary form-control"
            @click="addDeliveryItem"
            :disabled="!deliveryItemReady"
            formaction=""
          >
            Add
          </button>
        </div>
      </div>
    </div>

    <br>

    <table class="table table-bordered border-0">
      <thead>
      <tr>
        <th>My command</th>
        <th>quantities</th>
        <th>prices</th>
        <th/>
      </tr>
      </thead>
      <tbody>
      <tr v-for="(item, index) in form.items" :key="'order-item-' + index">
        <td>{{ item.dish.title }}</td>
        <td>{{ item.count }}</td>
        <td>{{ item.dish.price * item.count }}</td>
        <td>
          <button @click="removeDeliveryItem(index)">
            Remove
          </button>
        </td>
      </tr>
      </tbody>
    </table>

    <button class="btn btn-primary form-control" @click="submitForm">
      Order
    </button>

    <SuccessErrorAlert :error="error" :success="success"/>
  </div>
</template>

<script>

import TextInput from '@/components/form/TextInput'
import DateInput from '@/components/form/DateInput'
import TimeInput from '@/components/form/TimeInput'
import RestaurantApi from '@/RestaurantApi'
import _ from 'lodash'
import FormMixin from '@/mixins/FormMixin'
import SuccessErrorAlert from '@/components/form/SuccessErrorAlert'
import EventBus from '@/EventBus'

export default {
  name: 'DeliveryOrder',
  props: ['restaurantMenu', 'lunchSpecials', 'dinnerSpecials', 'title'],
  mixins: [FormMixin],
  data () {
    return {
      selection: {
        dishType: '',
        dish: '',
        count: 0
      },
      userLogged: false
    }
  },
  computed: {
    deliveryItemReadOnly () {
      console.log('delivery item check')
      return this.form.date === '' || this.form.time === ''
    },
    deliveryMenu () {
      // There's no type to select if the day and time have not been selected
      if (this.deliveryItemReadOnly) {
        return {}
      }

      // First we add elements from the menu
      const menu = {}
      for (const [key, value] of Object.entries(this.restaurantMenu)) {
        menu[key] = value
      }

      // Then we add elements from the specials if available

      // First we retrieve the day of the week
      const weekdays = ['SU', 'MO', 'TU', 'WE', 'TH', 'FR', 'SA']
      const date = new Date(this.form.date)
      const day = weekdays[date.getDay()]

      // Second, we identify the type of specials served at the time
      // selected by the user
      let specials = null
      if (this.form.time < '17:00') {
        specials = this.lunchSpecials
      } else {
        specials = this.dinnerSpecials
      }

      // Finally, if a special is served at that time we add
      // the special to the list of types
      for (const special of specials) {
        if (special.day === day) {
          if (!menu['Daily specials']) {
            menu['Daily specials'] = []
          }
          menu['Daily specials'].push(special)
        }
      }

      return menu
    },
    deliveryItemReady () {
      return !this.deliveryItemReadOnly &&
        this.selection.count > 0 &&
        this.selection.dish !== '' &&
        this.selection.dishType !== ''
    }
  },
  methods: {
    defaultForm () {
      return {
        fullname: '',
        email: '',
        address: '',
        phone_number: '',
        date: '',
        time: '',
        items: []
      }
    },
    makeFormRequest (form) {
      const order = _.cloneDeep(form)

      // use dish url instead of dish object
      for (const item of order.items) {
        item.dish = item.dish.url
      }

      // send the order to the rest API
      return RestaurantApi.makeDeliveryOrder(order)
    },
    onFormSubmissionSuccess (response) {
      EventBus.emit(EventBus.DELIVERY_ORDER, response.data)
      FormMixin.methods.onFormSubmissionSuccess.call(this, response)
    },
    addDeliveryItem () {
      // retrieve the dish
      const selection = this.selection
      this.form.items.push({
        dish: this.deliveryMenu[selection.dishType][selection.dish],
        count: this.selection.count
      })
    },
    removeDeliveryItem (index) {
      this.form.items.splice(index, 1)
    }
  },
  components: {
    TextInput,
    DateInput,
    TimeInput,
    SuccessErrorAlert
  },
  mounted () {
    const app = this
    EventBus.on(EventBus.LOGIN, function () {
      app.userLogged = true
      app.form.username = ''
      app.form.email = ''
    })
    EventBus.on(EventBus.LOGOUT, function () {
      app.userLogged = false
      app.form.username = ''
      app.form.email = ''
    })
  }
}
</script>

<style scoped>

</style>
