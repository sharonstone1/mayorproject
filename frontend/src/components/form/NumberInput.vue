<template>
  <div class="form-group row">
    <label :for="id" class="col-sm-2 col-form-label">{{ label }}</label>
    <div class="col-sm-10">
      <input
        type="number"
        class="form-control"
        :id="id"
        :min="min"
        :max="max"
        :placeholder="placeholder"
        :value="value"
        @input="$emit('input', $event.target.value)"
      >
    </div>
  </div>
</template>

<script>
export default {
  name: 'NumberInput',
  props: ['label', 'id', 'min', 'max', 'placeholder', 'value']
}
</script>

<style scoped>

</style>
