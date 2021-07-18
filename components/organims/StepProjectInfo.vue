<template>
  <div class="form-layout">
    <v-header-form title="Project Information" />
    <v-input-text v-model="stepform.project" label="Project Name" name="project" />
    <v-input-textarea v-model="stepform.description" label="Description" name="description" />
    <v-button-form @click.native="nextStep" />
  </div>
</template>

<script>
import InputText from '~/components/molecules/InputText.vue'
import InputTextarea from '~/components/molecules/InputTextarea.vue'
import ButtonForm from '~/components/atoms/ButtonForm.vue'
import HeaderForm from '~/components/molecules/Header.vue'

export default {
  components: {
    'v-button-form': ButtonForm,
    'v-input-text': InputText,
    'v-input-textarea': InputTextarea,
    'v-header-form': HeaderForm
  },
  props: {
    value: {
      type: Object,
      required: true
    }
  },
  data () {
    return {
      stepform: {
        project: '',
        description: ''
      }
    }
  },
  created () {
    this.stepform = this.value
  },
  methods: {
    nextStep () {
      this.$emit('nextStep')
    }
  }
}
</script>

<style>

</style>
