<template>
  <div>
    <label :for="name" class="label">{{ label }}</label>
    <input
      type="text"
      :name="name"
      :value="value"
      @input="$emit('input', $event.target.value)"
    >
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

<style scoped>
div {
  display: flex;
  flex-direction: column;
}

input {
  outline: none;
  border: none;
}

input:after {
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
}

input::after {
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
}
</style>
