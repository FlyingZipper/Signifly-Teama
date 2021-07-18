<template>
  <div class="form-create-project">
    <div class="form-create-project__selector">
      <v-step-selector v-model="step" icon="face" text="Client" :step="1" />
      <v-step-selector
        v-model="step"
        icon="extension"
        text="Project"
        :step="2"
      />
      <v-step-selector v-model="step" icon="groups" text="Members" :step="3" />
      <v-step-selector
        v-model="step"
        icon="visibility"
        text="Overview"
        :step="4"
      />
    </div>
    <div /> <!-- Space holder for selector step component -->
    <div class="form-create-project__steps">
      <transition name="slide" mode="out-in">
        <v-step-client-info
          v-if="step === 1"
          v-model="form.client"
          @nextStep="incrementStep"
        />
        <v-step-project-info
          v-if="step === 2"
          v-model="form.project"
          @nextStep="incrementStep"
        />
        <v-step-team-member
          v-if="step === 3"
          v-model="form.members"
          @nextStep="incrementStep"
        />
        <v-step-overview v-if="step === 4" :form-data="form" @nextStep="save" />
      </transition>
    </div>
  </div>
</template>

<script>
import StepSelector from '~/components/molecules/StepSelector.vue'

import StepClientInfo from '~/components/organims/StepClientInfo.vue'
import StepProjectInfo from '~/components/organims/StepProjectInfo.vue'
import StepTeamMember from '~/components/organims/StepTeamMember.vue'
import StepOverview from '~/components/organims/StepOverview.vue'

export default {
  components: {
    'v-step-selector': StepSelector,
    'v-step-client-info': StepClientInfo,
    'v-step-project-info': StepProjectInfo,
    'v-step-team-member': StepTeamMember,
    'v-step-overview': StepOverview
  },
  data () {
    return {
      step: 1,
      form: {
        client: {},
        project: {},
        members: []
      }
    }
  },
  methods: {
    incrementStep () {
      this.step++
    },
    save () {
      this.$createTeam(this.form).then((response) => {
        this.$router.push({ path: '/fesfs' })
      })
    }
  }
}
</script>

<style lang="scss" scoped>
.form-create-project {
  margin: 0 5%;
  display: grid;
  grid-template-columns: 20rem auto 20rem;
  & > .form-create-project__selector {
    position: fixed;
    top: 50%;
    left: 5%;
    transform: translateY(-50%);
    & > * {
      margin-bottom: 50px;
      &:last-child {
        margin-bottom: 0px;
      }
    }
  }
  & > .form-create-project__steps {
    // margin-top: 10rem;
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    margin-bottom: 5rem;
  }
}
</style>
