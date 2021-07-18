<template>
  <div class="layout">
    <div />
    <div v-if="project !== null" class="content_layout">
      <v-header :title="project.project.project" />
      <p>
        {{ project.project.description }}
      </p>
      <div>
        <h3>Client Information</h3>
        <div>
          <h4>Client</h4>
          <div>{{ project.client.name }}</div>
        </div>
        <div>
          <h4>Email</h4>
          <div>{{ project.client.email }}</div>
        </div>
      </div>
      <div>
        <h3>Team members</h3>
        <div v-for="member in project.members" :key="member.email">
          {{ member.email }}
        </div>
      </div>
    </div>
    <div v-else>
      No team found for this project
    </div>
    <div />
  </div>
</template>

<script>
import Header from '~/components/molecules/Header.vue'

export default {
  components: {
    'v-header': Header
  },
  data () {
    return {
      project: null,
      loading: true
    }
  },
  created () {
    this.$getTeam(this.$route.params.slug)
      .then((response) => {
        if (response.exists()) {
          this.project = response.val()
        } else {
          this.project = null
        }
        this.loading = false
      })
      .catch(() => {
        this.loading = false
        this.project = null
      })
  }
}
</script>

<style lang="scss" scoped>
.content_layout {
  margin-right: 100px !important;
  margin-top: 135px !important;
  margin-bottom: 100px;
}
</style>
