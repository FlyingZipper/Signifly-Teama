<template>
  <div class="form-layout">
    <v-header-form small title="Client Information" />
    <v-input-text v-model="stepform.name" label="Name" name="name" />
    <v-input-text v-model="stepform.email" label="Email" name="email" />
    <v-button-form @click.native="nextStep" />
  </div>
</template>

<script>
import InputText from '~/components/molecules/InputText.vue'
import ButtonForm from '~/components/atoms/ButtonForm.vue'
import HeaderForm from '~/components/molecules/Header.vue'

export default {
  components: {
    'v-button-form': ButtonForm,
    'v-input-text': InputText,
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
        email: '',
        name: ''
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

<style lang="scss" scoped>

</style>
