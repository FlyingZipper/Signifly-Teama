<template>
  <div>
    <div>
      <v-form-step-selector />
    </div>
    <div>
      <div>
        <v-step-client-info />
        <v-step-project-info />
        <v-step-team-member />
        <v-step-overview />
      </div>
      <v-form-button />
    </div>
  </div>
</template>

<script>
import FormStepSelector from '~/components/organims/FormStepSelector.vue'

import StepClientInfo from '~/components/organims/StepClientInfo.vue'
import StepProjectInfo from '~/components/organims/StepProjectInfo.vue'
import StepTeamMember from '~/components/organims/StepTeamMember.vue'
import StepOverview from '~/components/organims/StepOverview.vue'

import FormButton from '~/components/atoms/FormButton.vue'

export default {
  components: {
    'v-form-step-selector': FormStepSelector,
    'v-step-client-info': StepClientInfo,
    'v-step-project-info': StepProjectInfo,
    'v-step-team-member': StepTeamMember,
    'v-step-overview': StepOverview,
    'v-form-button': FormButton
  },
  data () {
    return {
      step: 0
    }
  }
}
</script>

<style>

</style>
