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
              <TextInput label="User name" id="loginUserName" placeholder="Your username" type="text"
                 v-model="form.login"/>

              <TextInput label="Password" id="loginPassword" placeholder="Your password" type="password"
                         v-model="form.password"/>

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
  name: 'Login',
  props: ['modalId'],
  components: { TextInput },
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
