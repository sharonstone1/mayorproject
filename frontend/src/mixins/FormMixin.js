import _ from 'lodash'
import SuccessErrorAlert from '@/components/form/SuccessErrorAlert'

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
    submitForm () {
      // TODO validation ?

      this.clearMessage()

      const app = this
      this.makeFormRequest(this.form)
        .then(function (response) {
          app.form = app.defaultForm()
          app.success = 'Thank you for your booking'
        })
        .catch(function (error) {
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
      this.success = null
      this.error = null
    },
    defaultForm () {
      console.assert('This must be implemented by the parent')
    },
    makeFormRequest (form) {
      console.assert('This must be implemented by the parent')
      return {}
    }
  }
}
