<template>
  <div>
    <v-navbar />
    <main id="main">
      <transition
        name="slide"
        mode="out-in"
      >
        <Nuxt />
      </transition>
    </main>
  </div>
</template>

<script>
export default {

}
</script>

<style>

</style>
