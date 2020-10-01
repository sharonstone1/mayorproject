<template>
  <div class="container">
    <h2> {{ title }}</h2>
    <div class="row">
      <div class="col-lg-6">
        <slot></slot>
      </div>
      <div class="col-lg-6">
        <img :src="image">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Welcome',
  props: ['title', 'image']
}
</script>

<style scoped>

</style>
