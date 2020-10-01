<template>
  <div class="form-group row">
    <label :for="id" class="col-sm-2 col-form-label">
      {{ label }}
    </label>
    <div class="col-sm-10">
      <VSelect :id="id" :options="options" v-model="value"/>
    </div>
  </div>
</template>

<script>
import VSelect from '@/components/common/form/VSelect'
export default {
  name: 'SelectInput',
  components: { VSelect },
  props: {
    label: String,
    id: String,
    options: Object,
    value: String
  },
  watch: {
    value (newValue) {
      this.$emit('input', newValue)
    }
  }
}
</script>

<style scoped>

</style>
