<template>
  <div class="container">
    <h2>{{ title }}</h2>
    <slot></slot>
    <div class="card-body">
      <form v-on:submit.prevent="submitForm">
        <TextInput id="inputName" label="Name" placeholder="name" type="name"
          v-model="form.fullname"
        />

        <TextInput id="inputEmail" label="Email" placeholder="Email" type="email"
          v-model="form.email"
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
              reserve table
            </button>
          </div>
        </div>

      </form>

      <SuccessErrorAlert :error="error" :success="success"/>
    </div>
  </div>
</template>

<script>
import TextInput from '@/components/form/TextInput'
import DateInput from '@/components/form/DateInput'
import TimeInput from '@/components/form/TimeInput'
import NumberInput from '@/components/form/NumberInput'
import CheckboxInput from '@/components/form/CheckboxInput'
import RestaurantApi from '@/RestaurantApi'
import FormMixin from '@/mixins/FormMixin'
import SuccessErrorAlert from '@/components/form/SuccessErrorAlert'

export default {
  name: 'TableBooking',
  props: ['title'],
  mixins: [FormMixin],
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
    }
  }
}
</script>

<style scoped>

</style>
