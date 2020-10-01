<template>
  <div class="container">
    <form v-for="(order,index) in deliveryOrders"
          :id="`form-${order.url}`"
          :key="`form-${order.url}`"
          @submit.prevent="updateOrder(order,index)"
    ></form>

    <table class="table table-hover table-sm table-responsive">
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
      <DeliveryDetails :order="order" :items="order.items" :menus="menus"/>
    </Modal>
  </div>
</template>

<script>
import RestaurantApi from '@/RestaurantApi'
import DeliveryDetails from '@/components/common/management/DeliveryDetails'
import Modal from '@/components/common/Modal'
import IdGenerator from '@/IdGenerator'

export default {
  name: 'AdminDelivery',
  props: {
    menus: Object,
    deliveryOrders: []
  },
  components: { Modal, DeliveryDetails },
  methods: {
    updateOrder (deliveryOrder, index) {
      const client = RestaurantApi.client()
      client.put(deliveryOrder.url, deliveryOrder)
        .then(function (response) {
          // TODO: Inform parent that the order has been changed
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
  }
}
</script>

<style scoped>

</style>
