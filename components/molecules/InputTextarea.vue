<template>
  <div class="input-text">
    <label :for="name" class="label">{{ label }}</label>
    <textarea
      type="text"
      :name="name"
      :value="value"
      @input="$emit('input', $event.target.value)"
    />
    <span class="input-border" />
  </div>
</template>

<script>
export default {
  props: {
    label: {
      type: String,
      required: true
    },
    name: {
      type: String,
      required: true
    },
    value: {
      type: undefined,
      required: false,
      default: null
    }
  }
}
</script>

<style lang="scss" scoped>
@import "~/assets/scss/var.scss";

.input-text {
  display: flex;
  flex-direction: column;
  & > label {
    font-weight: 700;
    font-size: 1rem;
    color: $black;
  }
  & > textarea,
  input {
    outline: none;
    border: none;
    padding: 10px 0;
    border-bottom: 1px solid $black;
    font-size: 1rem;
    resize: vertical;
    height: 100px;
  }
}

/* input:after {
  content: "";
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 1px;
  background-color: #000;
  transform-origin: center left;
  transform: scaleX(0);
  transition: transform 0.2s ease-out;
} */

/* input::after {
  content: "";
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 1px;
  background-color: #000;
  transform-origin: center left;
  transform: scaleX(0);
  transition: transform 0.2s ease-out;
} */
</style>
