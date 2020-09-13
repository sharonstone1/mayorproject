<template>
    <div class="container">
      <h2>{{title}}</h2>
      <slot></slot>
      <div class="row">
        <MenuCard v-for="(menu, title, index) in restaurantMenu"
          :menu="menu"
          :title="title"
          :key="'vkey-menu-' + index"
        />
      </div>
    </div>
</template>

<script>
import MenuCard from '@/components/MenuCard'

export default {
  name: 'MenuPresentation',
  props: ['title', 'restaurantMenu'],
  components: {
    MenuCard
  }
}
</script>

<style scoped>

</style>
