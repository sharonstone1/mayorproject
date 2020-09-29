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

    <OrderItemSelection
      :date="form.date"
      :time="form.time"
      :restaurant-menu="restaurantMenu"
      :dinner-specials="dinnerSpecials"
      :lunch-specials="lunchSpecials"
      @item-add="addDeliveryItem($event)"
    />

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
import OrderItemSelection from '@/components/admin/OrderItemSelection'

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
    addDeliveryItem (item) {
      // retrieve the dish
      this.form.items.push(item)
    },
    removeDeliveryItem (index) {
      this.form.items.splice(index, 1)
    }
  },
  components: {
    OrderItemSelection,
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
