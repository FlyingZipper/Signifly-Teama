<template>
  <div class="card-member">
    <div class="card-member__image">
      <img :src="member.image" alt="">
    </div>
    <div class="card-member__info">
      <div>
        <div class="capitalize name">
          {{ name }}
        </div>
        <div class="capitalize role">
          {{ role }}
        </div>
        <a :href="mailto" class="mailto email">
          {{ member.email }}
        </a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    member: {
      type: Object,
      required: true
    }
  },
  computed: {
    mailto () {
      return `mailto:${this.member.email}`
    },
    name () {
      return this.member.name.toLowerCase()
    },
    role () {
      return this.member.role.toLowerCase()
    }
  }
}
</script>

<style lang="scss" scoped>
@import "~/assets/scss/var.scss";
$font-size: 1rem;
$font-size-small: 0.75rem;

.card-member {
  & .card-member__image {
    & > img {
      max-width: $card-size;
    }
    margin-bottom: 10px;
  }
  & .card-member__info {
    & .name {
      font-weight: 600;
      font-size: $font-size;
    }
    & .role {
      font-size: $font-size;
      font-weight: 300;
      margin-bottom: 10px;
    }
    & .email {
      font-size: $font-size-small;
    }
  }
}
</style>
