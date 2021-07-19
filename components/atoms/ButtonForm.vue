<template>
  <button class="button__form">
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

.button__form{
  transition: all 0.2s ease-in-out;
  text-transform: capitalize;
  background-color: $main;
  font-weight: 600;
  color: #FFFFFF;
  font-size: 1rem;
  padding: 0.5em 1em;
  border-radius: 4px;
  &:hover {
    box-shadow: 4px 4px 0 #000;
    transform: translate(-2px, -2px);
  }
}

</style>
