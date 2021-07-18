<template>
  <div>
    <nav class="navbar">
      <nuxt-link class="navbar__logo" to="/">
        <img
          src="~assets/svg/signifly.svg"
          class=""
          alt=""
          style="width: auto; height: 40px"
        >
        <h2 class="navbar__title">
          Teams
        </h2>
      </nuxt-link>
      <h4 class="navbar__location">
        {{ location }}
      </h4>
    </nav>
  </div>
</template>

<script>
export default {
  data () {
    return {
      routeConvertion: {
        '/create': 'Create Project',
        '/': 'Dashboard'
      }
    }
  },
  computed: {
    location () {
      if (this.$route.path in this.routeConvertion) {
        return this.routeConvertion[this.$route.path]
      }
      return 'Project'
    }
  },
  created () {
    console.log(this.$route.path)
  }
}
</script>

<style lang="scss" scoped>
@import "~/assets/scss/var.scss";

.navbar {
  margin: 20px 5%;
  position: fixed;
  & > .navbar__logo {
    display: flex;
    align-items: center;
    & > .navbar__title {
      padding-left: 4px;
      line-height: 40px;
      font-size: 30px;
      font-weight: 600;
      color: $purple;
      margin: 0;
    }
  }
  & > .navbar__location {
    font-size: 18px;
    line-height: 25px;
    font-weight: 400;
    margin: 15px 0;
    color: $gray-dark;
    text-transform: capitalize;
  }
}
</style>
