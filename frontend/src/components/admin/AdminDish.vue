<!-- Manage the restaurant menu -->

<template>
  <div>
    <div v-for="(dishCategory, categoryName) in dishes" :key="categoryName">
      <div class="modal fade" :id="`modalId-${dishCategory.name}`" tabindex="-1" role="dialog" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered modal-xl" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title">{{dishCategory.name}}</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>

            <div class="card  mb-3" v-for="(dish, index) in dishCategory.items" :key="dish.url" >
        <form @submit.prevent="updateForm(dish)">

          <div class="card-body">

            <TextInput :id="`titleInput-${index}-${dishCategory.name}`" type="text" v-model="dish.title" label="Title"/>

            <TextArea :id="`descriptionInput-${index}-${dishCategory.name}`" v-model="dish.description" label="Description"/>

            <NumberInput :id="`priceInput-${index}-${dishCategory.name}`" label="Price" min="1" max="5000" v-model="dish.price"/>

            <SelectInput :id="`typeInput-${index}-${dishCategory.name}`" label="Type" :options="types" v-model="dish.type"/>

            <SelectInput :id="`dayInput-${index}-${dishCategory.name}`" label="Day" :options="days" v-model="dish.day"/>

            <SelectInput :id="`servingTimeInput-${index}-${dishCategory.name}`" label="Serving Time" :options="servingTimes" v-model="dish.serving_time"/>

            <!-- Upload control of the associated image -->
            <div class="form-group row">
              <label :for="`imageInput-${index}-${dishCategory.name}`" class="col-sm-2 col-form-label">
                Image
              </label>
              <div class="col-sm-10">
                <input type="file" :id="`imageInput-${index}-${dishCategory.name}`" accept="image/jpeg, image/png" multiple="false"
                       @change="selectFile(dish, $event.target.files[0])" />
              </div>
            </div>
          </div>

          <div class="card-footer">
            <div class="form-group row">
              <div class="col-sm-10 offset-sm-2">
                <button class="btn btn-primary" type="submit">
                  Update
                </button>
              </div>
            </div>
          </div>
        </form>
        </div>

          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
import RestaurantApi from '@/RestaurantApi'
import TextInput from '@/components/common/form/TextInput'
import TextArea from '@/components/common/form/TextArea'
import NumberInput from '@/components/common/form/NumberInput'
import SelectInput from '@/components/common/form/SelectInput'
import EventBus from '@/EventBus'

export default {
  name: 'AdminDish',
  components: { SelectInput, NumberInput, TextArea, TextInput },
  data () {
    return {
      dishes: {
        starter: {
          name: 'Starters',
          items: []
        },
        main: {
          name: 'Mains',
          items: []
        },
        special: {
          name: 'Specials',
          items: []
        },
        side: {
          name: 'Sides',
          items: []
        },
        dessert: {
          name: 'Deserts',
          items: []
        }
      },
      types: {
        starter: 'Appetizing starter',
        main: 'Main course',
        dessert: 'Delicious desert',
        special: 'Daily special',
        side: 'Sides'
      },
      days: {
        MO: 'Monday',
        TU: 'Tuesday',
        WE: 'Wednesday',
        TH: 'Thursday',
        FR: 'Friday',
        SA: 'Saturday',
        SU: 'Sunday',
        '*': 'Everyday'
      },
      servingTimes: {
        lunch: 'Lunch',
        dinner: 'Dinner',
        '*': 'Lunch and Dinner'
      }
    }
  },
  mounted () {
    const app = this
    RestaurantApi.getDishes()
      .then(function (response) {
        // Put dishes into their categories
        for (const dish of response.data) {
          app.dishes[dish.type].items.push(dish)
        }

        const adminDish = []
        for (const key in app.dishes) {
          adminDish.push(app.dishes[key].name)
        }
        EventBus.emit(EventBus.ADMIN_DISH_AVAILABLE, adminDish)
      })
      .catch(function (error) {
        console.log('failed to get dishes: ' + error)
      })
  },
  methods: {
    selectFile (dish, file) {
      if (file) {
        dish.file = file
      }
    },
    updateForm (form) {
      const formData = new FormData()
      formData.append('title', form.title)
      formData.append('description', form.description)
      formData.append('price', form.price)
      formData.append('type', form.type)
      formData.append('day', form.day)
      formData.append('serving_time', form.serving_time)
      if (form.file) {
        formData.append('image', form.file)
      }

      RestaurantApi.client().put(
        form.url,
        formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        }
      )
        .then(function (response) {
          EventBus.emit(EventBus.DISHES_UPDATES)
        })
        .catch(function (error) {
          console.log('failure during dish update: ' + error)
        })
      console.log('update form: ' + form)
    }
  }
}
</script>

<style scoped>

</style>
