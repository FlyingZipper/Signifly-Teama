<template>
  <div class="layout">
    <div />
    <v-layout-card-project />
    <div />
    <v-button-create />
  </div>
</template>

<script>
import ButtonCreate from '~/components/atoms/ButtonCreate.vue'
import LayoutCardProject from '~/components/template/LayoutCardProject.vue'

export default {
  components: {
    'v-button-create': ButtonCreate,
    'v-layout-card-project': LayoutCardProject
  },
  data () {
    return {
      text: ''
    }
  }
}
</script>

<style>
/* .layout{
  margin: 0 5%;
  display: grid;
  grid-template-columns: 10rem auto;
} */
</style>
