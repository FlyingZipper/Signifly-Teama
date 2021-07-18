<template>
  <nuxt-link class="card-project" :to="`/${slug}`">
    <div class="card-project__project">
      <v-header small :title="project.project.project" />
      <p>
        {{ project.project.description }}
      </p>
    </div>
    <div class="card-project__client">
      <span class="capitalize"><b>Client:</b> {{ project.client.name }}</span>
      <span><b>Email:</b> {{ project.client.email }}</span>
      <span><b>Team Size:</b> {{ project.members.length }}</span>
    </div>
    <span class="material-icons-outlined card-project__arrow">east</span>
  </nuxt-link>
</template>

<script>
import Header from '~/components/molecules/Header.vue'

export default {
  components: {
    'v-header': Header
  },
  props: {
    project: {
      type: Object,
      required: true
    },
    slug: {
      type: String,
      required: true
    }
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
