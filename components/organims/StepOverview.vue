<template>
  <div class="overview">
    <v-header-form title="Project Overview" />
    <div class="project__section">
      <div>
        <h3>Client Information</h3>
        <div>
          <div>
            <h4>Client</h4>
            <div>{{ formData.client.name }}</div>
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
          <v-card-member-form
            v-for="member in members"
            :key="member.email"
            :name="member.name"
            :email="member.email"
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

import CardMemberForm from '~/components/molecules/CardMemberForm.vue'

import teamMembers from '~/team.json'

export default {
  components: {
    'v-button-form': ButtonForm,
    'v-header-form': HeaderForm,
    'v-card-member-form': CardMemberForm
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

.overview{
  & .overview__subtitlte{
    text-transform: uppercase;
  }
  & .overview__members {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr;
    grid-row-gap: 40px;
    grid-column-gap: 40px;
  }
  & .project__section{
    margin: 50px 0;
  }
}
</style>
