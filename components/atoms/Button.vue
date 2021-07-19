<template>
  <button class="button">
    {{ name }}
  </button>
</template>

<script>
export default {
  props: {
    name: {
      type: String,
      required: false,
      default: 'Continue'
    }
  }
}
</script>

<style lang="scss" scoped>
@import "~/assets/scss/var.scss";

.button{
  text-transform: capitalize;
  background-color: $gray-dark;
  color: #FFFFFF;
  font-size: 1rem;
  font-weight: 600;
  padding: 0.5em 1em;
  border-radius: 2px;
}

</style>
