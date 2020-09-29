<template>
  <Modal title="Login" :modalId="modalId">
    <form v-on:submit.prevent="submitForm" id="loginForm">
        <TextInput label="User name" placeholder="Your username" type="text"
           v-model="form.login"/>

        <TextInput label="Password" placeholder="Your password" type="password"
                   v-model="form.password"/>

        <SuccessErrorAlert :error="error" :success="success"/>
    </form>

    <template v-slot:footer>
      <button type="submit" class="btn btn-primary" form="loginForm">Login</button>
    </template>
  </Modal>
</template>

<script>
import FormMixin from '@/mixins/FormMixin'
import TextInput from '@/components/form/TextInput'
import RestaurantApi from '@/RestaurantApi'
import Modal from '@/components/Modal'
import $ from 'jquery'
import EventBus from '@/EventBus'

export default {
  name: 'Login',
  props: ['modalId'],
  components: { TextInput, Modal },
  mixins: [FormMixin],
  methods: {
    defaultForm () {
      return {
        login: '',
        password: ''
      }
    },
    makeFormRequest (form) {
      return RestaurantApi.login(form)
    },
    onFormSubmissionSuccess (response) {
      $(`#${this.modalId} .close`).click()
      EventBus.emit(EventBus.LOGIN)
      this.form = this.defaultForm()
    }
  }
}
</script>

<style scoped>

</style>
