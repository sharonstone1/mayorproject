<template>
  <div>
    <div class="row">
      <div class="col-lg-6">
        <h6 class="card-header">
          {{ title }}
        </h6><br>
        <p><slot /></p>
        <br>
      </div>
      <br>

      <div class="col-lg-6">
        <img :src="image">
      </div>
    </div>
    <br>
  </div>
</template>

<script>
export default {
  name: 'EventDescription',
  props: ['title', 'image']
}
</script>

<style scoped>

</style>
