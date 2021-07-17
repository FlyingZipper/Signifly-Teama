<template>
  <div>
    {{ step }}
    <v-step-selector v-model="step" icon="face" text="Client" :step="1" />
    <v-step-selector v-model="step" icon="extension" text="Project" :step="2" />
    <v-step-selector v-model="step" icon="groups" text="Members" :step="3" />
    <v-step-selector v-model="step" icon="visibility" text="Overview" :step="4" />
  </div>
</template>

<script>
import StepSelector from '~/components/molecules/StepSelector.vue'
export default {
  components: {
    'v-step-selector': StepSelector
  },
  data () {
    return {
      step: 1
    }
  }
}
</script>

<style>

</style>
