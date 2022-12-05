<template>
  <div 
    class="movie-item p-0 col-auto g-3 mx-3"
    @click="goDetail"
  >
    <img
      :src="poster_path + movie.poster_path" alt="..."
    >
  </div>
</template>

<script>
export default {
  name: 'MovieCardView',
  props: {
    movie: Object,
  },
  data() {
    return {
      poster_path: 'https://image.tmdb.org/t/p/w300/'
    }
  },
  methods: {
    goDetail() {
      this.$router.push({ name: 'MovieDetail', params: { movie_id: this.movie.movie_id }})
    }
  }
}
</script>

<style>
  .movie-item {
    position: relative;
    display: block;
    flex: 1 1 0px;
    transition: transform 500ms;
  }
  .movie-item:hover {
    cursor: pointer;
  }
  .popular-list .movie-item:focus,
  .popular-list .movie-item:hover {
    transform: scale(1.4);
    z-index: 1;
  }
  .popular-list:focus-within ~ .movie-item,
  .popular-list:hover ~ .movie-item {
    transform: translateX(-25%);
  }

  .movie-item:focus  .movie-item,
  .movie-item:hover  .movie-item {
    transform: translateX(25%);
  }
</style>