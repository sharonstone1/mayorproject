<template>
  <div class="form-group row">
    <label
      :for="id"
      class="col-sm-2 col-form-label"
    >{{ label }}</label>
    <div class="col-sm-10">
      <div class="form-check">
        <input
          type="checkbox"
          :id="id"
          :name="name"
          class="form-check-input"
        >
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CheckboxInput',
  props: ['label', 'id', 'name']
}
</script>

<style scoped>

</style>
