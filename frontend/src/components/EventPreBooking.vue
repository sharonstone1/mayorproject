<template>
  <div class="card">
     <div class="card-header">
      <h4>{{title}}</h4>
    </div>

    <form v-on:submit.prevent="submitForm">
      <div class="card-body">

        <TextInput id='inputUserNameEvent' type="text" label="Name" placeholder="Enter your name"
          v-model="form.fullname"
          v-show="userLogged == false"
        />

        <TextInput id="inputUserEmailEvent" label="Email" placeholder="" type="email"
           v-model="form.email"
           v-show="userLogged == false"
        />

        <TextInput id="inputPhoneEvent" label="Phone number" placeholder="" type="tel"
           v-model="form.phone_number"
        />

        <TextInput id='inputAddressEvent' type="text" label="Address" placeholder="Enter your address"
          v-model="form.address"
        />

        <DateInput id="inputDateEvent" label="Event date" min="2020-07-22" max="2030-07-22"
          v-model="form.date"
        />

        <TimeInput id="inputTimeEvent" label="Time" min="12:00" max="20:00"
           v-model="form.time"
        />
      </div>
      <br>
      <div class="card-footer">
        <div class="form-group row">
          <div class="offset-sm-2">
            <button class="btn btn-primary" type="submit">
              Event pre-booking
            </button>
          </div>
        </div>
        <SuccessErrorAlert :success="success" :error="error"/>
      </div>
    </form>
  </div>
</template>

<script>
import TextInput from '@/components/form/TextInput'
import DateInput from '@/components/form/DateInput'
import TimeInput from '@/components/form/TimeInput'
import RestaurantApi from '@/RestaurantApi'
import SuccessErrorAlert from '@/components/form/SuccessErrorAlert'
import FormMixin from '@/mixins/FormMixin'
import EventBus from '@/EventBus'

export default {
  name: 'EventPreBooking',
  mixins: [FormMixin],
  data: function () {
    return {
      userLogged: false
    }
  },
  components: { SuccessErrorAlert, TimeInput, DateInput, TextInput },
  props: ['title'],
  methods: {
    defaultForm () {
      return {
        fullname: '',
        email: '',
        phone_number: '',
        address: '',
        date: '',
        time: ''
      }
    },
    makeFormRequest (form) {
      return RestaurantApi.makeEventPreBooking(form)
    },
    onFormSubmissionSuccess (response) {
      EventBus.emit(EventBus.EVENT_BOOKING, response.data)
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
