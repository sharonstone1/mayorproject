<!-- Selection of dishes the user can order, it depend on the date and time the order is delivered -->

<template>
  <form class="form" @submit.prevent="addDeliveryItem()">
    <div class="form-group row">
      <label class="col-form-label col-sm-3">Course Type</label>
      <div class="col-sm-9">
        <VSelect
          :options="courseTypeSelect"
          v-model="selection.dishType"
          :disabled="deliveryItemReadOnly"
        />
      </div>
    </div>

    <div class="form-group row">
      <label class="col-form-label col-sm-3">Course</label>
      <div class="col-sm-9">
        <VSelect
          :options="courseSelect"
          v-model="selection.dish"
          :disabled="deliveryItemReadOnly"
        />
      </div>
    </div>

    <div class="form-group row">
      <label class="col-form-label col-sm-3">Count</label>
      <div class="col-sm-9">
        <input class="form-control" type="number"
               v-model="selection.count"
               :readonly="deliveryItemReadOnly"
        >
      </div>
    </div>

    <div class="form-group row">
      <div class="offset-sm-3 col-sm-9">
        <button class="btn btn-primary form-control" :disabled="!deliveryItemReady">
          Add
        </button>
      </div>
    </div>
  </form>
</template>

<script>
import VSelect from '@/components/common/form/VSelect'
export default {
  name: 'OrderItemSelection',
  components: { VSelect },
  props: {
    date: String,
    time: String,
    menus: Object
  },
  data: function () {
    return {
      selection: {
        count: 1,
        dish: null,
        dishType: null
      }
    }
  },
  computed: {
    deliveryItemReadOnly () {
      return this.date === '' || this.time === ''
    },
    deliveryMenu () {
      // There's no type to select if the day and time have not been selected
      if (this.deliveryItemReadOnly) {
        return {}
      }

      // First we add elements from the menu
      const menu = {}
      if (this.menus.restaurantMenu) {
        for (const [key, value] of Object.entries(this.menus.restaurantMenu)) {
          menu[key] = value
        }
      }

      // Then we add elements from the specials if available

      // First we retrieve the day of the week
      const weekdays = ['SU', 'MO', 'TU', 'WE', 'TH', 'FR', 'SA']
      const date = new Date(this.date)
      const day = weekdays[date.getDay()]

      // Second, we identify the type of specials served at the time
      // selected by the user
      let specials = null
      if (this.time < '17:00') {
        specials = this.menus.lunchSpecials
      } else {
        specials = this.menus.dinnerSpecials
      }

      // Finally, if a special is served at that time we add
      // the special to the list of types
      if (specials) {
        for (const special of specials) {
          if (special.day === day) {
            if (!menu['Daily specials']) {
              menu['Daily specials'] = []
            }
            menu['Daily specials'].push(special)
          }
        }
      }

      return menu
    },
    courseTypeSelect () {
      const result = {}
      for (const key in this.deliveryMenu) {
        result[key] = key
      }
      return result
    },
    courseSelect () {
      const result = {}

      if (this.selection.dishType) {
        let index = 0
        for (const course of this.deliveryMenu[this.selection.dishType]) {
          result[index] = course.title
          index++
        }
      }

      return result
    },
    deliveryItemReady () {
      return !this.deliveryItemReadOnly &&
        this.selection.count > 0 &&
        this.selection.dish !== null &&
        this.selection.dishType !== null
    }
  },
  watch: {
    courseTypeSelect () {
      this.updateDishTypeSelection()
    },
    courseSelect () {
      this.updateDishSelection()
    }
  },
  methods: {
    addDeliveryItem () {
      console.log('Add delivery item: ' + this.selection)
      this.$emit('item-add', {
        count: this.selection.count,
        dish: this.deliveryMenu[this.selection.dishType][this.selection.dish]
      })
      this.selection = {
        count: 1,
        dish: null,
        dishType: null
      }
    },
    updateDishTypeSelection () {
      const keys = Object.keys(this.courseTypeSelect)
      if (keys.length) {
        this.selection.dishType = keys[0]
      } else {
        this.selection.dishType = null
      }
    },
    updateDishSelection () {
      const keys = Object.keys(this.courseSelect)
      if (keys.length) {
        this.selection.dish = keys[0]
      } else {
        this.selection.dish = null
      }
    }
  },
  mounted () {
    this.updateDishTypeSelection()
  }
}
</script>

<style scoped>

</style>
