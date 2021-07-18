<template>
  <div class="card-layout">
    <div class="card-layout__grid">
      <v-card-project v-for="i in 10" :key="i" />
    </div>
  </div>
</template>

<script>
import CardProject from '~/components/molecules/CardProject.vue'

export default {
  components: {
    'v-card-project': CardProject
  }
}
</script>

<style lang="scss" scoped>
.card-layout {
  margin-top: 135px;
  margin-bottom: 100px;
  & .card-layout__grid{
  margin: 0 5%;
  display: grid;
  grid-template-columns: 20rem 20rem 20rem 20rem;
  grid-row-gap: 40px;
  grid-column-gap: 40px;
  }
}
</style>
