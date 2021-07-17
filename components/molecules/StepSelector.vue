<template>
  <button class="step-selector" @click="selectStep()">
    <span class="material-icons-outlined">{{ icon }}</span>
    <span class="text">{{ text }}</span>
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
      console.log('kek')
      this.$emit('input', this.step)
    }
  }
}
</script>

<style lang="scss" scoped>
@import '~/assets/scss/var.scss';
.step-selector{
  display: flex;
  align-items: center;
  justify-content: space-between;
  & > .material-icons-outlined{
    padding-right: 10px;
  }
  & > .text {
    color: $purple
  }
}
</style>
