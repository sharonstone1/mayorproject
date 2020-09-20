<template>
    <div class="modal fade" :id="modalId" tabindex="-1" role="dialog" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Login</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <form v-on:submit.prevent="submitForm">
            <div class="modal-body">
              <TextInput label="User name" id="registerUserName" placeholder="Your username" type="text"
                 v-model="form.username"/>

              <TextInput label="Email" id="registerEmail" placeholder="Your email" type="text"
                 v-model="form.email"/>

              <TextInput label="Password" id="registerPassword" placeholder="Your password" type="password"
                         v-model="form.password"/>

              <TextInput label="Password Confirmation" id="lregisterPasswordConfirmation" placeholder="Password confirmation" type="password"
                         v-model="form.password_confirm"/>

              <TextInput label="First Name" id="registerFirstName" placeholder="Your first name" type="text"
                 v-model="form.first_name"/>

              <TextInput label="Last Name" id="registerLastName" placeholder="Your last name" type="text"
                 v-model="form.last_name"/>

              <SuccessErrorAlert :error="error" :success="success"/>
            </div>
            <div class="modal-footer">
              <button type="submit" class="btn btn-primary">Login</button>
            </div>
          </form>
        </div>
      </div>
    </div>
</template>

<script>
import FormMixin from '@/mixins/FormMixin'
import TextInput from '@/components/form/TextInput'
import RestaurantApi from '@/RestaurantApi'
import $ from 'jquery'
import EventBus from '@/EventBus'

export default {
  name: 'UserRegistration',
  props: ['modalId'],
  components: { TextInput },
  mixins: [FormMixin],
  methods: {
    defaultForm () {
      return {
        username: '',
        email: '',
        password: '',
        password_confirm: '',
        first_name: '',
        last_name: ''
      }
    },
    makeFormRequest (form) {
      return RestaurantApi.register(form)
    },
    onFormSubmissionSuccess (response) {
      const app = this
      const credentials = {
        login: app.form.username,
        password: app.form.password
      }
      RestaurantApi.login(credentials)
        .then(function (response) {
          $(`#${app.modalId} .close`).click()
          EventBus.emit(EventBus.LOGIN)
        })
        .catch(function (error) {
          app.error = 'Successful registration but login failure'
          console.log('Login failure: ' + error)
        })
    }
  }
}
</script>

<style scoped>

</style>
