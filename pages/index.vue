<template>
  <div class="layout">
    <div />
    <v-layout-card-project :projects="projects" />
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
      projects: {},
      loading: true
    }
  },
  created () {
    this.$getTeams()
      .then((response) => {
        if (response.exists()) {
          this.projects = response.val()
        } else {
          this.project = {}
        }
        this.loading = false
      })
      .catch(() => {
        this.loading = false
        this.project = {}
      })
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
