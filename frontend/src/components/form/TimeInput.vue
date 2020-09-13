<template>
  <div class="form-group row">
    <label
      :for="id"
      class="col-sm-2 col-form-label"
    >{{ label }}</label>
    <div class="col-sm-10">
      <input
        type="time"
        :id="id"
        name="time"
        class="form-control"
        :min="min"
        :max="max"
      >
    </div>
  </div>
</template>

<script>
export default {
  name: 'TimeInput',
  props: ['label', 'id', 'min', 'max']
}
</script>

<style scoped>

</style>
