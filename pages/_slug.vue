<template>
  <div>
    <div v-if="project !== null" class="project">
      <v-header :title="project.project.project" />
      <p class="project__description">
        {{ project.project.description }}
      </p>
      <div class="project__section">
        <div>
          <h3>Client Information</h3>
          <div class="project__information">
            <div>
              <h4>Client</h4>
              <div>{{ project.client.name }}</div>
            </div>
            <div>
              <h4>Email</h4>
              <a class="mailto" href="mailto:">{{ project.client.email }}</a>
            </div>
          </div>
        </div>
        <div>
          <h3>Team members</h3>
          <div class="project__members">
            <v-card-member-display
              v-for="(member, index) in project.members"
              :key="`${member.email}-${index}`"
              :member="member"
            />
          </div>
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
import CardMemberDisplay from '~/components/molecules/CardMemberDisplay.vue'

export default {
  components: {
    'v-header': Header,
    'v-card-member-display': CardMemberDisplay
  },
  data () {
    return {
      project: null,
      loading: true,
      default: {
        client: {
          name: 'N/A',
          email: 'N/A'
        },
        project: {
          project: 'N/A',
          description: 'N/A'
        },
        members: []
      }
    }
  },
  computed: {
    mailto () {
      return `mailto:${this.project.client.email}`
    }
  },
  created () {
    this.$getTeam(this.$route.params.slug)
      .then((response) => {
        if (response.exists()) {
          this.project = response.val()
          if (this.project.client === undefined) {
            this.project.client = this.default.client
          }
          if (this.project.project === undefined) {
            this.project.project = this.default.project
          }
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
@import "~/assets/scss/var.scss";

.project {
  & .project__description {
    @include desktop {
      max-width: 50%;
    }
  }
  & .project__section {
    display: grid;
    grid-template-columns: auto;
    @include desktop {
      grid-template-columns: 1fr 2fr;
    }
    & .project__members {
      display: grid;
      grid-template-columns: 1fr;
      @include desktop {
        grid-template-columns: 1fr 1fr 1fr 1fr;
      }
      grid-row-gap: 40px;
      grid-column-gap: 10px;
    }
  }
}
</style>
