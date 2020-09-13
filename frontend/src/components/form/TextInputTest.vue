<template>
  <div class="form-group row">
    <label
      :for="id"
      class="col-sm-2 col-form-label"
    >{{ label }}</label>
    <div class="col-sm-10">
      <input
        :type="type"
        class="form-control"
        :id="id"
        :placeholder="placeholder"
        :value="value"
        @input="$emit('input', $event.target.value)"
      >
    </div>
  </div>
</template>

<script>
export default {
  name: 'TextInputTest',
  props: ['label', 'id', 'type', 'placeholder', 'value']
}
</script>

<style scoped>

</style>
