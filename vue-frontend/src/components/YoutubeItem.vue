<template>
  <div class="m-5">
    <iframe :src="youtubeURI" width="560" height="315" allowfullscreen>
    </iframe>
  </div>
</template>

<script>
export default {
  name: 'YoutubeItem',
  props: {
    youtube: Object,
  },
  computed: {
    youtubeURI() {
      const videoId = this.youtube.key
      return `https://www.youtube.com/embed/${videoId}`
    },
  }
}
</script>

<style>

</style>