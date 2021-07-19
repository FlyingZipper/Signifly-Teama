<template>
  <div class="layout">
    <v-navbar />
    <main id="main">
      <transition
        name="fade"
        mode="out-in"
      >
        <Nuxt />
      </transition>
    </main>
  </div>
</template>

<script>
import Navbar from '~/components/organims/Navbar.vue'
export default {
  components: {
    'v-navbar': Navbar
  }

}
</script>

<style>

</style>
