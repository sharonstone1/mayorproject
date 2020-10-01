<template>
  <div class="form-group row">
    <label
      :for="id"
      class="col-sm-2 col-form-label"
    >{{ label }}</label>
    <div class="col-sm-10">
      <input
        type="date"
        :id="id"
        name="date"
        class="form-control"
        :value="value"
        @input="$emit('input', $event.target.value)"
        :min="min"
        :max="max"
      >
    </div>
  </div>
</template>

<script>
export default {
  name: 'DateInput',
  props: ['label', 'id', 'value', 'min', 'max']
}
</script>

<style scoped>

</style>
