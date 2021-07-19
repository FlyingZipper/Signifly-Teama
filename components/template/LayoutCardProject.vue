<template>
  <div class="layout-project">
    <div class="layout-project__grid">
      <v-card-project
        v-for="(project, slug) in projects"
        :key="slug"
        :slug="slug"
        :project="project"
      />
      <div />
    </div>
  </div>
</template>

<script>
import CardProject from '~/components/molecules/CardProject.vue'

export default {
  components: {
    'v-card-project': CardProject
  },
  props: {
    projects: {
      type: Object,
      required: true
    }
  }
}
</script>

<style lang="scss" scoped>
.layout-project {
  margin-bottom: 100px;
  & .layout-project__grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr;
    grid-row-gap: 40px;
    grid-column-gap: 40px;
  }
}
</style>
