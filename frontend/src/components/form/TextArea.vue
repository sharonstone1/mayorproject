<template>
  <div class="form-group row">
    <label :for="id" class="col-sm-2 col-form-label">
      {{ label }}
    </label>
    <div class="col-sm-10">
      <textarea class="form-control" :id="id"
                :value="value"
                @input="$emit('input', $event.target.value)">
      </textarea>
    </div>
  </div>
</template>

<script>
export default {
  name: 'textArea',
  props: ['label', 'id', 'type', 'value']
}
</script>

<style scoped>

</style>
