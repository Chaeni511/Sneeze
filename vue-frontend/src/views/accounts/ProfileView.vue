<template>
  <div>
    <h1>{{ username }}'s Profile</h1>
  </div>
</template>

<script>
export default {
  name: 'ProfileView',
  computed: {
    username() {
      return this.$store.state.username
    }
  }
}
</script>

<style>

</style>