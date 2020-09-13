<template>
  <div class="form-group row">
    <label :for="id" class="col-sm-2 col-form-label">{{ label }}</label>
    <div class="col-sm-10">
      <div class="form-check">
        <input type="checkbox" class="form-check-input"
          :id="id"
          :name="name"
          :checked="value"
          @input="$emit('input', $event.target.checked)"
        >
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CheckboxInput',
  props: ['label', 'id', 'name', 'value']
}
</script>

<style scoped>

</style>
