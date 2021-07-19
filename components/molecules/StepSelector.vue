<template>
  <button
    class="step-selector"
    :class="{ active: step === value }"
    @click="selectStep()"
  >
    <span class="material-icons-outlined">{{ icon }}</span>
    <span class="text">{{ text }}</span>
    <span :class="[step === value ? 'active' : 'inactive', 'indicator']" />
  </button>
</template>

<script>
export default {
  props: {
    step: {
      type: Number,
      required: true
    },
    value: {
      type: Number,
      required: true
    },
    icon: {
      type: String,
      required: true
    },
    text: {
      type: String,
      required: true
    }
  },
  methods: {
    selectStep () {
      this.$emit('input', this.step)
    }
  }
}
</script>

<style lang="scss" scoped>
@import "~/assets/scss/var.scss";
$font-size-icon: 22px;
$font-size: 15px;

.step-selector {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: space-between;
  color: $gray;
  transition: all ease-in-out 0.1s;
  &.active, &:hover {
    color: $black;
  }
  & > .material-icons-outlined {
    padding-right: 15px;
    font-size: $font-size-icon;
  }
  & > .text {
    line-height: $font-size-icon;
    font-size: $font-size;
    font-weight: 700;
  }
  .indicator {
    z-index: -1;
    transition: all ease-in-out 0.1s;
    width: 150px;
    height: 15px;
    background-color: $main;
    position: absolute;
    bottom: -5px;
    margin-top: 30px;
    &.active {
      opacity: 0.15;
      transform: translateX(-5%);
    }
    &.inactive {
      opacity: 0;
      transform: translateX(-20%);
    }
  }
}
</style>
