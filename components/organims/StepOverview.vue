<template>
  <div class="overview">
    <v-header-form title="Project Overview" />
    <div v-for="(stepData, step) in formData" :key="step">
      <h3 class="overview__subtitlte">
        {{ step }}
      </h3>
      {{ stepData }}
      <!-- <ul>
        <li>

        </li>
      </ul> -->
    </div>
    <v-button-form name="Assemble" @click.native="nextStep" />
  </div>
</template>

<script>
import ButtonForm from '~/components/atoms/ButtonForm.vue'
import HeaderForm from '~/components/molecules/Header.vue'

export default {
  components: {
    'v-button-form': ButtonForm,
    'v-header-form': HeaderForm
  },
  props: {
    formData: {
      type: Object,
      required: true
    }
  },
  created () {
    console.log(this.formData)
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
}
</style>
