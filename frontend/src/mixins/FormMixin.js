import _ from 'lodash'
import SuccessErrorAlert from '@/components/common/form/SuccessErrorAlert'

export default {
  components: { SuccessErrorAlert },
  data: function () {
    return {
      form: this.defaultForm(),
      success: null,
      error: null
    }
  },
  watch: {
    form: {
      // If the form is changed, we reset the success or error message.
      handler () {
        // Equality between objects in javascript search for reference, not content.
        if (this.success && _.isEqual(this.form, this.defaultForm())) {
          return
        }
        this.clearMessage()
      },
      deep: true
    }
  },
  methods: {
    // Form submission
    submitForm () {
      // Error or success messages are cleared
      this.clearMessage()

      const app = this
      this.makeFormRequest(this.form)
        .then(function (response) {
          app.onFormSubmissionSuccess(response)
        })
        .catch(function (error) {
          // Display the error to the user
          if (error.response) {
            if (error.response.status === 400) {
              app.error = 'One of the form field is incorrect'
            } else {
              app.error = 'booking service error'
            }
          } else if (error.request) {
            app.error = 'The booking service is not reachable'
          } else {
            app.error = 'Internal request error'
          }
        })
    },
    clearMessage () {
      // Clear the error/success message if any
      this.success = null
      this.error = null
    },
    defaultForm () {
      // This method should be implemented by the component using the mixin. We expect an object containing the
      // default values of the form.
      console.assert('This must be implemented by the parent')
    },
    makeFormRequest (form) {
      // This method should be implemented by the component using the mixin. It execute the request of the
      // form passed in parameter
      console.assert('This must be implemented by the parent')
      return {}
    },
    onFormSubmissionSuccess (response) {
      // If the form is successfuly submited we reset the content and display a message of success.
      this.form = this.defaultForm()
      this.success = 'Thank you for your booking'
    }
  }
}
