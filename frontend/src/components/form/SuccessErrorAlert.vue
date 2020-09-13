<template>
  <div>
    <div class="alert alert-success" role="alert" v-show="success">
      {{success}}
    </div>
    <div class="alert alert-danger" role="alert" v-show="error">
      {{error}}
    </div>
  </div>
</template>

<script>
export default {
  name: 'SuccessErrorAlert',
  props: ['success', 'error']
}
</script>

<style scoped>

</style>
