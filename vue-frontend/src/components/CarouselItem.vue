<template>
  <div class="carousel-item active" data-bs-interval="200">
    <img :src="backdrop_path" class="d-block w-100" :alt="movie.title ">
    <div class="carousel-caption d-none d-md-block">
      <h5>{{ movie.title }}</h5>
      <p>{{ movie.overview }}</p>
    </div>
  </div>

</template>

<script>
// import MovieDetailView from '@/views/movie/MovieDetailView'

export default {
  name: 'CarouselItem',
  components: {
    // MovieDetailView,
  },
  props: {
    movie: Object,
  },
  data() {
    return {
      backdrop_path: `https://image.tmdb.org/t/p/original/${ this.movie.backdrop_path }`
    }
  }
}
</script>

<style>

</style>