<template>
  <div class="team form-layout">
    <v-header-form title="Team Members" />
    <div class="team__roles">
      <div class="">
        <button
          v-for="(teamGroup, role) in team"
          :key="role"
          @click="setActiveRole(role)"
        >
          <h3 class="team__role" :class="{ enabled: role === activeRole }">
            {{ role }}
          </h3>
        </button>
      </div>
      <ul class="team__members">
        <li
          v-for="member in currentRoleMembers"
          :key="member.email"
          class="team__member"
        >
          <v-card-member-form
            :name="member.name"
            :email="member.email"
            :enabled="isEnabled(member.email)"
            @toggle="toggleCard"
          />
        </li>
      </ul>
    </div>
    <v-button-form @click.native="nextStep" />
  </div>
</template>

<script>
import CardMemberForm from '~/components/molecules/CardMemberForm.vue'
import HeaderForm from '~/components/molecules/Header.vue'
import ButtonForm from '~/components/atoms/ButtonForm.vue'
import teamMembers from '~/team.json'

export default {
  components: {
    'v-card-member-form': CardMemberForm,
    'v-button-form': ButtonForm,
    'v-header-form': HeaderForm
  },
  props: {
    value: {
      type: Array,
      required: true
    }
  },
  data () {
    return {
      team: {},
      activeRole: null
    }
  },
  computed: {
    currentRoleMembers () {
      return this.team[this.activeRole]
    }
  },
  created () {
    teamMembers.forEach((member) => {
      if (!(member.role in this.team)) {
        this.team[member.role] = []
      }
      this.team[member.role].push(member)
    })
    this.activeRole = Object.keys(this.team)[0]
  },
  methods: {
    isEnabled (email) {
      return this.value.includes(email)
    },
    setActiveRole (role) {
      this.activeRole = role
    },
    nextStep () {
      this.$emit('input', this.value)
      this.$emit('nextStep')
    },
    toggleCard (email) {
      if (this.value.includes(email)) {
        this.$emit(
          'input',
          this.value.filter(i => i !== email)
        )
      } else {
        this.$emit('input', [...this.value, email])
      }
    }
  }
}
</script>

<style lang="scss" scoped>
@import "~/assets/scss/var.scss";

.team {
  & .team__roles {
    & button {
      margin-right: 20px;
      &:last-child {
        margin-right: 0;
      }
    }
    & .team__role {
      text-transform: uppercase;
      font-size: 1.15rem;
      font-weight: 600;
      color: $gray;
      &:hover {
        color: $black;
      }
      &.enabled {
        color: $main;
      }
    }
  }
  & .team__members {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-row-gap: 5px;
    grid-column-gap: 5px;
    @include desktop {
      grid-template-columns: 1fr 1fr 1fr 1fr;
      grid-row-gap: 40px;
      grid-column-gap: 40px;
    }

    // & > .team__member {

    // }
  }
}
</style>
