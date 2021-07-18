<template>
  <div class="layout">
    <div />
    <div class="content_layout">
      <v-header title="Individual Project" />
      <p>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam id
        consequat libero, at viverra magna. Nullam suscipit, mi eget venenatis
        porttitor, risus elit cursus ex, vitae pulvinar felis nulla a lectus.
      </p>
      <div>
        <h3>Client Information</h3>
        <div>
          <h4>Name</h4>
          <div>Client name</div>
        </div>
        <div>
          <h4>Email</h4>
          <div>Client email</div>
        </div>
      </div>
      <div>
        <h3>Team members</h3>
        <div>
          Team member cards
        </div>
      </div>
    </div>
    <div />
  </div>
</template>

<script>
import Header from '~/components/molecules/Header.vue'

export default {
  components: {
    'v-header': Header
  }
}
</script>

<style lang="scss" scoped>
.content_layout {
  margin-right: 100px !important;
  margin-top: 135px !important;
  margin-bottom: 100px;
}
</style>
