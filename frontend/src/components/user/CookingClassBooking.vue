<template>
  <form v-on:submit.prevent="submitForm">
    <TextInput type="text" id="CandidateName" placeholder="Your name" label="Candidate name"
      v-model="form.fullname"
      v-show="userLogged == false"
    />

    <TextInput type="email" id="CandidateEmail" placeholder="Your email" label="Email"
      v-model="form.email"
      v-show="userLogged == false"
    />

    <TextInput type="tel" id="CandidatePhone" placeholder="Your phone number" label="Phone number"
      v-model="form.phone_number"/>

    <TextInput type="text" id="CandidateAddress" placeholder="Your address" label="Address"
      v-model="form.address"/>

    <DateInput id="ClassDate" label="Date" min="2020-07-22" max="2030-07-22"
       v-model="form.date"/>

    <SelectInput id="ClassType" label="Type" :options="classTypes" v-model="form.type"/>

    <SelectInput id="ClassTime" label="Time" :options="classTime" v-model="form.time"/>

    <div class="form-group row">
      <div class="col-sm-10 offset-sm-2">
        <button class="btn btn-primary" type="submit">
          Subscribe
        </button>
      </div>
    </div>

    <SuccessErrorAlert :success="success" :error="error"/>
  </form>
</template>

<script>
import TextInput from '@/components/common/form/TextInput'
import FormMixin from '@/mixins/FormMixin'
import DateInput from '@/components/common/form/DateInput'
import SelectInput from '@/components/common/form/SelectInput'
import RestaurantApi from '@/RestaurantApi'
import EventBus from '@/EventBus'

export default {
  name: 'CookingClassBooking',
  components: { SelectInput, DateInput, TextInput },
  mixins: [FormMixin],
  data () {
    return {
      classTypes: {
        stream: 'Cooking lesson live streaming',
        live: 'At the restaurant'
      },
      classTime: {
        morning: 'Starting at 8 o\'clock until lunch',
        afternoon: 'Starting at 15 o\'clock until dinner'
      },

      userLogged: false
    }
  },
  methods: {
    defaultForm () {
      return {
        fullname: '',
        email: '',
        phone_number: '',
        address: '',
        date: '',
        type: null,
        time: null
      }
    },
    makeFormRequest (form) {
      return RestaurantApi.makeLessonBooking(form)
    },
    onFormSubmissionSuccess (response) {
      EventBus.emit(EventBus.COOKING_LESSON_BOOKING, response.data)
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
