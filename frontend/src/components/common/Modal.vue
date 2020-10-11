<template>
  <div class="container">
    <div class="modal fade" :id="modalId" tabindex="-1" aria-hidden="true">
      <div :class="`modal-dialog modal-dialog-centered ${extraClass}`" >
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">{{ title }}</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body modal-workaround">
            <slot></slot>
          </div>
          <div class="modal-footer">
            <slot name="footer"></slot>
          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
export default {
  name: 'Modal',
  props: ['modalId', 'title', 'extraClass']
}
</script>

<style scoped>

</style>
