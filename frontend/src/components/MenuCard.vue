<template>
  <div class="col-lg-3">
    <div class="card">
      <div class="card-header">
        <h4>{{ title }}</h4>
      </div>
      <div
        class="card-body"
        :id="menu"
      >
        <table class="table table-borderless">
          <template v-for="(item, index) in menu">
            <tr :key="'menu-card-' + index">
              <td><h6>{{ item.title }}</h6></td>
              <td>{{ item.price }}</td>
            </tr>
          </template>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MenuCard',
  props: ['title', 'menu']
}
</script>

<style scoped>

</style>
