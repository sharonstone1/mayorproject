<template>
  <div class="form-group row">
    <label :for="id" class="col-sm-2 col-form-label">
      {{ label }}
    </label>
    <div class="col-sm-10">
        <select :id="id" :name="id" class="form-control"
                :value="value"
                @input="$emit('input', $event.target.value)">
          <option v-for="(text, key) in options" :value="key" :key="key">
            {{text}}
          </option>
        </select>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SelectInput',
  props: ['label', 'id', 'options', 'value']
}
</script>

<style scoped>

</style>
