<template>
  <div class="container">
    <h2>{{ title }}</h2>
    <slot></slot>
    <div class="card-body">
      <form v-on:submit.prevent="submitForm">
        <TextInput id="inputName" label="Name" placeholder="name" type="name"
          v-model="form.fullname"
          v-show="userLogged == false"
        />

        <TextInput id="inputEmail" label="Email" placeholder="Email" type="email"
          v-model="form.email"
          v-show="userLogged == false"
        />

        <TextInput id="inputtelephone" label="Telephone" placeholder="Telephone" type="tel"
          v-model="form.phone_number"
        />

        <DateInput id="inputDateRestaurant" label="start date:" max="2030-07-22" min="2020-07-22"
          v-model="form.date"
        />

        <TimeInput id="inputTimeRestaurant" label="Time" min="12:00" max="21:00"
          v-model="form.time"
        />

        <NumberInput id="inputGuestRestaurant" label="Guests" max="10" min="1" placeholder="1"
          v-model="form.guest_count"
        />

        <CheckboxInput id="inputVipRestaurant" label="VIP" name="vip"
          v-model="form.vip"
        />

        <div class="form-group row">
          <div class="col-sm-10 offset-sm-2">
            <button class="btn btn-primary" type="submit">
              Booking table
            </button>
          </div>
        </div>

      </form>

      <SuccessErrorAlert :error="error" :success="success"/>
    </div>
  </div>
</template>

<script>
import TextInput from '@/components/common/form/TextInput'
import DateInput from '@/components/common/form/DateInput'
import TimeInput from '@/components/common/form/TimeInput'
import NumberInput from '@/components/common/form/NumberInput'
import CheckboxInput from '@/components/common/form/CheckboxInput'
import RestaurantApi from '@/RestaurantApi'
import FormMixin from '@/mixins/FormMixin'
import SuccessErrorAlert from '@/components/common/form/SuccessErrorAlert'
import EventBus from '@/EventBus'

export default {
  name: 'TableBooking',
  props: ['title'],
  mixins: [FormMixin],
  data: function () {
    return {
      userLogged: false
    }
  },
  components: {
    SuccessErrorAlert,
    CheckboxInput,
    NumberInput,
    TimeInput,
    DateInput,
    TextInput
  },
  methods: {
    makeFormRequest (form) {
      return RestaurantApi.makeTableBooking(form)
    },
    defaultForm () {
      return {
        fullname: '',
        email: '',
        phone_number: '',
        date: '',
        time: '',
        guest_count: 1,
        vip: false
      }
    },
    onFormSubmissionSuccess (response) {
      EventBus.emit(EventBus.TABLE_BOOKING, response.data)
      FormMixin.methods.onFormSubmissionSuccess.call(this, response)
    }
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
