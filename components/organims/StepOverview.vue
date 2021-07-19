<template>
  <div class="overview">
    <v-header-form title="Project Overview" />
    <div class="project__section">
      <div>
        <h3>Client Information</h3>
        <div>
          <div>
            <h4>Client</h4>
            <div class="captitalize">
              {{ formData.client.name }}
            </div>
          </div>
          <div>
            <h4>Email</h4>
            <div>{{ formData.client.email }}</div>
          </div>
        </div>
      </div>
      <div>
        <h3>Project Information</h3>
        <div>
          <div>
            <h4>Client</h4>
            <div>{{ formData.project.project }}</div>
          </div>
          <div>
            <h4>Email</h4>
            <div>{{ formData.project.description }}</div>
          </div>
        </div>
      </div>
      <div>
        <h3>Team members</h3>
        <div class="overview__members">
          <v-card-member-display
            v-for="member in members"
            :key="member.email"
            :member="member"
          />
        </div>
      </div>
    </div>
    <v-button-form name="Assemble" @click.native="nextStep" />
  </div>
</template>

<script>
import ButtonForm from '~/components/atoms/ButtonForm.vue'
import HeaderForm from '~/components/molecules/Header.vue'

import CardMemberDisplay from '~/components/molecules/CardMemberDisplay.vue'

import teamMembers from '~/team.json'

export default {
  components: {
    'v-button-form': ButtonForm,
    'v-header-form': HeaderForm,
    'v-card-member-display': CardMemberDisplay
  },
  props: {
    formData: {
      type: Object,
      required: true
    }
  },
  computed: {
    members () {
      return teamMembers.filter(m => this.formData.members.includes(m.email))
    }
  },
  methods: {
    nextStep () {
      this.$emit('nextStep')
    }
  }
}
</script>

<style lang="scss" scoped>
@import "~/assets/scss/var.scss";

.overview {
  h4 {
    font-weight: 500;
  }
  & .overview__subtitlte {
    text-transform: uppercase;
  }
  & .overview__members {
    display: grid;
    grid-template-columns: 1fr;
    @include desktop {
      grid-template-columns: $card-size $card-size $card-size $card-size;
    }
    grid-row-gap: 40px;
    grid-column-gap: 40px;
  }
  & .project__section {
    margin: 50px 0;
  }
}
</style>
