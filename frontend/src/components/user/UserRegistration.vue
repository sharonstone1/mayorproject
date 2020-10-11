<template>
  <Modal title="Create an account" :modal-id="modalId">
    <form v-on:submit.prevent="submitForm" id="userRegistrationForm">
      <TextInput label="User name" placeholder="Your username" type="text"
         v-model="form.username"/>

      <TextInput label="Email" placeholder="Your email" type="email"
         v-model="form.email"/>

      <TextInput label="Password" placeholder="Your password" type="password"
                 v-model="form.password"/>

      <TextInput label="Password Confirmation" placeholder="Password confirmation" type="password"
                 v-model="form.password_confirm"/>

      <TextInput label="First Name" placeholder="Your first name" type="text"
         v-model="form.first_name"/>

      <TextInput label="Last Name" placeholder="Your last name" type="text"
         v-model="form.last_name"/>

      <SuccessErrorAlert :error="error" :success="success"/>
    </form>

    <template v-slot:footer>
      <button type="submit" class="btn btn-primary" form="userRegistrationForm">register</button>
    </template>
  </Modal>
</template>

<script>
import FormMixin from '@/mixins/FormMixin'
import TextInput from '@/components/common/form/TextInput'
import RestaurantApi from '@/RestaurantApi'
import $ from 'jquery'
import EventBus from '@/EventBus'
import Modal from '@/components/common/Modal'

export default {
  name: 'UserRegistration',
  props: ['modalId'],
  components: { Modal, TextInput },
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
          const clickModal = $(`#${app.modalId} .close`)
          clickModal.click()
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
