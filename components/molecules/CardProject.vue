<template>
  <nuxt-link class="card-project" to="/kekw">
    <div class="card-project__project">
      <v-header small title="Project Name" />
      <p>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam id
        consequat libero, at viverra magna. Nullam suscipit, mi eget venenatis
        porttitor, risus elit cursus ex, vitae pulvinar felis nulla a lectus.
      </p>
    </div>
    <div class="card-project__client">
      <span><b>For</b> : Google</span>
      <span><b>Email</b> : Google@support.com</span>
      <span><b>Team Size</b> : 5</span>
    </div>
    <span
      class="material-icons-outlined card-project__arrow"
    >east</span>
  </nuxt-link>
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
@import "~/assets/scss/var.scss";

.card-project {
  position: relative;
  color: $black;
  widows: 100%;
  padding: 10px;
  border-radius: 8px;
  transition: all 0.2s ease-in-out;

  &:hover {
    border-color: #f0f0f0;
    box-shadow: 8px 8px 0 #000;
    transform: translate(-4px, -4px);
    & .card-project__arrow {
      opacity: 1;
      transform: translateX(0%);
    }
  }
  & .card-project__project {
    & > p {
      font-size: 0.9rem;
    }
  }
  & .card-project__client {
    display: flex;
    flex-direction: column;
    flex-shrink: 0;
    font-size: 0.75rem;
  }
  & .card-project__arrow {
    transition: all 0.2s ease-in-out;
    position: absolute;
    bottom: 5%;
    right: 5%;
    opacity: 0;
    font-size: 1.5rem;
    transform: translateX(-100%);
  }
}
</style>
