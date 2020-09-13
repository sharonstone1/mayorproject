<template>
  <div class="card" id="pre_booking">
    <div class="card-header">
      <h4>{{title}}</h4>
    </div>

    <form v-on:submit.prevent="submitForm">
      <div class="card-body">

        <TextInput id='inputUserNameEvent' type="text" label="Name" placeholder="Enter your name"
          v-model="form.fullname"
        />

        <TextInput id="inputUserEmailEvent" label="Email" placeholder="" type="email"
           v-model="form.email"
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
          <div class="col-sm-10 offset-sm-2">
            <button class="btn btn-primary" type="submit">
              Prebook
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

export default {
  name: 'EventPreBooking',
  mixins: [FormMixin],
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
    }
  }
}
</script>

<style scoped>

</style>
