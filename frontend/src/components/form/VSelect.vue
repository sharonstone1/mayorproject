<template>
  <select :id="id" :name="id" class="form-control"
          :value="value"
          @input="$emit('input', $event.target.value)"
          :form="form">
    <option v-for="(text, key) in options" :value="key" :key="key">
      {{text}}
    </option>
  </select>
</template>

<script>
export default {
  name: 'VSelect',
  props: {
    id: String,
    options: Object,
    value: String,
    form: {
      default: '',
      type: String
    }
  }
}
</script>

<style scoped>

</style>
