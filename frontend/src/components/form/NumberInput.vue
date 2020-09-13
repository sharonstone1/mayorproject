<template>
  <div class="form-group row">
    <label
      :for="id"
      class="col-sm-2 col-form-label"
    >{{ label }}</label>
    <div class="col-sm-10">
      <input
        type="number"
        :id="id"
        name="guest"
        class="form-control"
        :min="min"
        :max="max"
        :placeholder="placeholder"
      >
    </div>
  </div>
</template>

<script>
export default {
  name: 'NumberInput',
  props: ['label', 'id', 'min', 'max', 'placeholder']
}
</script>

<style scoped>

</style>
