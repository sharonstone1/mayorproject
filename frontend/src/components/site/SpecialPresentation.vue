<template>
  <div class="container">
    <h2>{{ title }}</h2>
    <slot></slot>
    <!-- List of daily specials presented in cards -->
    <div class="row">
      <div class="col-xl-3 col-lg-4 col-md-6" v-for="(dish) in specials" :key="`dish-${dish.url}`">
        <!-- Card-->
        <div class="card mb-3">
          <div class="card-header"> {{ getDayDisplayName(dish.day) }} </div>
          <div class="card-body">
            <img :src="dish.image" data-toggle="modal" :data-target="`#modal-${getId(dish)}`">
          </div>
          <div class="card-footer">
            {{ dish.title }}
            <br>
            {{ dish.price }}
          </div>
        </div>

        <!-- Modal associated with the card-->
        <div class="modal fade" :id="`modal-${getId(dish)}`" role="dialog" tabindex="-1">
          <div class="modal-dialog modal-dialog-centered" role="document">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title"> {{ dish.title }} </h5>
                <button aria-label="Close" class="close" data-dismiss="modal" type="button">
                  <span aria-hidden="true">&times;</span>
                </button>
              </div>
              <div class="modal-body">
                <p style="font-family: Verdana">{{ dish.description }}</p>
              </div>
              <div class="modal-footer">
                <button class="btn btn-secondary" data-dismiss="modal" type="button">Close</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import RestaurantApi from '@/RestaurantApi'
import IdGenerator from '@/IdGenerator'

export default {
  name: 'SpecialPresentation',
  props: ['specials', 'title'],
  methods: {
    getDayDisplayName: RestaurantApi.utils.getDayDisplayName,
    getId (dish) {
      return IdGenerator.fromURL(dish.url)
    }
  }
}
</script>

<style scoped>

</style>
