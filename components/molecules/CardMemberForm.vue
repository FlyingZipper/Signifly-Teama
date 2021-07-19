<template>
  <button
    :class="{ enabled: enabled }"
    class="card-member-form"
    @click="selectMember"
  >
    <div
      :class="[
        enabled ? 'material-icons-outlined enabled' : '',
        'card-member-form__initials',
      ]"
    >
      {{ initials }}
    </div>
    <div class="card-member-form__info">
      <span class="card-member-form__name">{{ name }}</span>
      <span class="card-member-form__email">{{ email }}</span>
    </div>
  </button>
</template>

<script>
export default {
  props: {
    name: {
      type: String,
      required: true
    },
    email: {
      type: String,
      required: true
    },
    enabled: {
      type: Boolean,
      required: true
    }
  },
  computed: {
    initials () {
      if (this.enabled) {
        return 'done_outline'
      }
      const initials = this.name.split(' ', 2)
      if (initials.length < 2) {
        return initials[0][0]
      }
      return `${initials[0][0]}${initials[1][0]}`
    }
  },
  methods: {
    selectMember () {
      this.$emit('toggle', this.email)
    }
  }
}
</script>

<style lang="scss" scoped>
@import "~/assets/scss/var.scss";

.card-member-form {
  width: 100%;
  transition: all 0.2s ease-in-out;
  display: flex;
  flex-direction: row;
  align-items: center;
  flex-shrink: 0;
  border: 1px solid;
  border-color: #ffffff;
  padding: 0.5em 1em;
  cursor: pointer;
  &:hover {
    box-shadow: 8px 8px 0 #000;
    border: 1px solid #f0f0f0;
    transform: translate(-4px, -4px);
    &.enabled {
      box-shadow: 8px 8px 0 $main;
    }
  }
  & > .card-member-form__initials {
    transition: all 0.2s ease-in-out;
    border-radius: 100%;
    color: #fff;
    background-color: #000;
    width: 40px;
    height: 40px;
    display: flex;
    justify-content: center;
    align-items: center;
    margin-right: 10px;
    flex-shrink: 0;
    &.enabled {
      background-color: $main;
    }
  }
  & > .card-member-form__info {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    & > .card-member-form__name {
      text-transform: capitalize;
      text-align: initial;
      font-weight: 600;
      font-size: 0.75rem;
      @include desktop {
        font-size: 1rem;
      }
      color: $black;
    }
    & > .card-member-form__email {
      color: $gray-dark;
      font-size: 0.75rem;
    }
  }
}
</style>
