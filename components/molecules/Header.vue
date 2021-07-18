<template>
  <div class="step-form-title">
    <h3 :class="{ 'small' : small}">
      {{ title }}
    </h3>
    <span class="step-form-title__indicator" />
  </div>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      required: true
    },
    small: {
      type: Boolean,
      required: false,
      default: false
    }
  }
}
</script>

<style lang="scss" scoped>
@import "~/assets/scss/var.scss";

.step-form-title {
  position: relative;
  font-weight: 600;
  & > h3 {
    font-size: 1.5rem;
    text-transform: capitalize;
    &.small {
      font-size: 1.15rem;
    }
  }
  & > .step-form-title__indicator {
    z-index: -1;
    width: 250px;
    height: 15px;
    background-color: $purple;
    position: absolute;
    bottom: -2px;
    margin-top: 30px;
    opacity: 0.15;
    transform: translateX(-5%);
  }
}
</style>
