<template>
  <div>
    Dashboard - All Projects
    <v-text-input v-model="text" name="name" label="wow" />
    <div>
      <img src="~assets/svg/signifly.svg" class="" alt="" style="width:100px; height:auto;"> Teams
    </div>
  </div>
</template>

<script>
import TextInput from '~/components/molecules/InputText.vue'

export default {
  components: {
    'v-text-input': TextInput
  },
  data () {
    return {
      text: ''
    }
  }
}
</script>

<style>
</style>
