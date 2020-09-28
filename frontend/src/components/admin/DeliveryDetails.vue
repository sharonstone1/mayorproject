<template>
  <div class="container">
    <form v-for="(item,index) in items"
          :id="`form-${item.url}`"
          :key="`form-${item.url}`"
          @submit.prevent="updateItem(item,index)"
          hidden
    ></form>

    <table class="table table-hover">
      <thead>
        <tr>
          <th scope="col">Dish</th>
          <th scope="col">Count</th>
          <th scope="col"></th>
          <th scope="col"></th>
        </tr>
      </thead>
      <tbody>
        <template v-for="(item, index) in items">
          <tr :key="item.url">
            <td>{{ dishesName[item.dish] }}</td>
            <td><input type="number" v-model="item.count" :form="`form-${item.url}`"></td>
            <td>
              <button class="btn btn-primary" :form="`form-${item.url}`">Update</button>
            </td>
            <td>
              <button class="btn btn-warning" @click="removeItem(item, index)">Remove</button>
            </td>
          </tr>
        </template>
      </tbody>
    </table>

    <h2>Add new item to your delivery</h2>
    <OrderItemSelection
      :time="order.time"
      :date="order.date"
      :dinner-specials="dinnerSpecials"
      :lunch-specials="lunchSpecials"
      :restaurant-menu="restaurantMenu"
      @item-add="onItemAdded($event)"
    />
  </div>
</template>

<script>
import RestaurantApi from '@/RestaurantApi'
import OrderItemSelection from '@/components/admin/OrderItemSelection'

export default {
  name: 'DeliveryDetails',
  components: { OrderItemSelection },
  props: ['order', 'items', 'dishes', 'dinnerSpecials', 'lunchSpecials', 'restaurantMenu'],
  data: function () {
    return {
    }
  },
  methods: {
    updateItem (item) {
      RestaurantApi.client().put(item.url, item)
        .then(function (response) {
          item = response.data
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    removeItem (item, index) {
      const app = this
      RestaurantApi.client().delete(item.url)
        .then(function (response) {
          app.items.splice(index, 1)
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    getDishName (item) {
      return item.url
    },
    onItemAdded (item) {
      const app = this
      RestaurantApi.addOrderItem({
        order: this.order.url,
        dish: item.dish,
        count: item.count
      })
        .then(function (response) {
          app.items.push(response.data)
        })
        .catch(function (error) {
          console.log('Item not added, server failure: ' + error)
        })
    }
  },
  computed: {
    dishesName () {
      const result = {}
      for (const dish of this.dishes) {
        result[dish.url] = dish.title
      }
      return result
    }
  }
}
</script>

<style scoped>

</style>
