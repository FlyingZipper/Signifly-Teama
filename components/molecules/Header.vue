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
    font-size: 3.5rem;
    margin: 0;
    text-transform: uppercase;
    &.small {
      font-size: 2rem;
    }
  }
  & > .step-form-title__indicator {
    width: 250px;
    height: 15px;
    background-color: $main;
    position: absolute;
    bottom: -2px;
    margin-top: 30px;
    opacity: 0.15;
    transform: translateX(-5%);
  }
}
</style>
