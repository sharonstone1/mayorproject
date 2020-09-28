<template>
  <div class="container">
    <input type="date" v-model="date">

    <form v-for="(order,index) in deliveryOrders"
          :id="`form-${order.url}`"
          :key="`form-${order.url}`"
          @submit.prevent="updateOrder(order,index)"
    ></form>

    <table class="table table-hover">
      <thead>
        <tr>
          <th scope="col">Name</th>
          <th scope="col">Date</th>
          <th scope="col">Time</th>
          <th scope="col">Address</th>
          <th scope="col">Contact</th>
          <th scope="col">Details</th>
          <th scope="col"></th>
          <th scope="col"></th>
        </tr>
      </thead>
      <tbody>
        <template v-for="(order, index) in deliveryOrders">
          <tr :key="order.url">
            <td>{{ order.fullname }}</td>
            <td><input type="date" v-model="order.date" :form="`form-${order.url}`"></td>
            <td><input type="time" v-model="order.time" :form="`form-${order.url}`"></td>
            <td><input type="text" v-model="order.address" :form="`form-${order.url}`"></td>
            <td>
              <ul>
                <li>{{ order.phone_number }}</li>
                <li>{{ order.email }}</li>
              </ul>
            </td>
            <td>
              <button class="btn btn-secondary" data-toggle="modal" :data-target="`#${getModalId(order)}`">Details</button>
            </td>
            <td>
              <button class="btn btn-primary" :form="`form-${order.url}`">Update</button>
            </td>
            <td>
              <button class="btn btn-warning" @click="cancelOrder(order, index)">Cancel</button>
            </td>
          </tr>
        </template>
      </tbody>
    </table>

    <Modal v-for="(order) in deliveryOrders"
           :modal-id="getModalId(order)"
           extra-class="modal-xl"
           title="Delivery details"
           :key="`key-modal-${order.url}`"
    >
      <DeliveryDetails :order="order" :items="order.items" :dishes="dishes" :dinnerSpecials="dinnerSpecials" :lunchSpecials="lunchSpecials" :restaurantMenu="restaurantMenu"/>
    </Modal>
  </div>
</template>

<script>
import RestaurantApi from '@/RestaurantApi'
import DeliveryDetails from '@/components/admin/DeliveryDetails'
import Modal from '@/components/Modal'
import IdGenerator from '@/IdGenerator'

export default {
  name: 'AdminDelivery',
  props: {
    dishes: Object,
    dinnerSpecials: Object,
    lunchSpecials: Object,
    restaurantMenu: Object
  },
  components: { Modal, DeliveryDetails },
  data () {
    return {
      date: (new Date()).toISOString().substring(0, 10),
      deliveryOrders: []
    }
  },
  methods: {
    fetchDeliveryOrders () {
      const app = this
      RestaurantApi.getDeliveryOrders({ date: this.date })
        .then(function (response) {
          app.deliveryOrders = response.data
        })
    },
    updateOrder (deliveryOrder, index) {
      const app = this
      const client = RestaurantApi.client()
      client.put(deliveryOrder.url, deliveryOrder)
        .then(function (response) {
          if (response.data.date !== app.date) {
            app.removeOrderFromView(index)
          }
        })
        .catch(function (error) {
          console.log(`failure ${error} while updating resource: ${deliveryOrder.url}`)
        })
    },
    cancelOrder (order, index) {
      const app = this
      RestaurantApi.client().delete(order.url)
        .then(function (response) {
          app.removeOrderFromView(index)
        })
        .catch(function (error) {
          console.log(`failure ${error} while updating resource: ${order.url}`)
        })
    },
    removeOrderFromView (index) {
      this.deliveryOrders.splice(index, 1)
    },
    getModalId (order) {
      return IdGenerator.fromURL(order.url, 'modal-details')
    }
  },
  mounted () {
    this.fetchDeliveryOrders()
  },
  watch: {
    date (newDate, oldDate) {
      this.fetchDeliveryOrders()
    }
  }
}
</script>

<style scoped>

</style>
