<template>
  <div class="container">
    <form v-for="(order,index) in bookings"
          :id="$id('order-' + index)"
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
        <template v-for="(order, index) in bookings">
          <tr :key="order.url">
            <td>{{ order.fullname }}</td>
            <td><input type="date" v-model="order.date" :form="$id('order-' + index)"></td>
            <td><input type="time" v-model="order.time" :form="$id('order-' + index)"></td>
            <td><input type="text" v-model="order.address" :form="$id('order-' + index)"></td>
            <td>
              <ul>
                <li>{{ order.phone_number }}</li>
                <li>{{ order.email }}</li>
              </ul>
            </td>
            <td>
              <button class="btn btn-secondary" data-toggle="modal" :data-target="$idRef('modal-' + index)" :href="$idRef('modal-' + index)">Details</button>
            </td>
            <td>
              <button class="btn btn-primary" :form="$id('order-' + index)">Update</button>
            </td>
            <td>
              <button class="btn btn-warning" @click="cancelOrder(order, index)">Cancel</button>
            </td>
          </tr>
        </template>
      </tbody>
    </table>

    <Portal v-for="(order, index) in bookings" :key="$id('portal-' + index)" :to="portalTarget" :order="index">
      <Modal :modal-id="$id('modal-' + index)"
             extra-class="modal-xl"
             title="Delivery details"
             :key="$id('modal-' + index)"
      >
        <DeliveryDetails :order="order" :items="order.items" :menus="menus"/>
      </Modal>
    </Portal>
  </div>
</template>

<script>
import RestaurantApi from '@/RestaurantApi'
import DeliveryDetails from '@/components/common/management/DeliveryDetails'
import Modal from '@/components/common/Modal'
import IdGenerator from '@/IdGenerator'
import { Portal, PortalTarget } from 'portal-vue'

export default {
  name: 'AdminDelivery',
  props: {
    bookings: Array,
    menus: Array,
    portalTarget: String
  },
  components: {
    Modal,
    DeliveryDetails,
    Portal,
    PortalTarget // eslint-disable-line vue/no-unused-components
  },
  methods: {
    updateOrder (deliveryOrder, index) {
      const client = RestaurantApi.client()
      client.put(deliveryOrder.url, deliveryOrder)
        .then(function (response) {
          deliveryOrder = response.data()
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
      this.bookings.splice(index, 1)
    },
    getModalId (order) {
      return IdGenerator.fromURL(order.url, 'modal-details')
    }
  }
}
</script>

<style scoped>

</style>
