<template>
  <nuxt-link to="/create" class="material-icons-outlined button-create">
    add
  </nuxt-link>
</template>

<script>
export default {}
</script>

<style lang="scss" scoped>
@import "~/assets/scss/var.scss";
.button-create {
  transition: all 0.2s ease-in-out;
  color: #ffffff;
  padding: 15px;
  background-color: $main;
  border-radius: 100%;
  position: fixed;
  bottom: 5%;
  right: 5%;
  &:hover {
    box-shadow: 4px 4px 0 #000;
    transform: translate(-2px, -2px);
  }
}
</style>
