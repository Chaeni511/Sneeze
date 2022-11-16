<template>
  <!-- <h1>Carousel</h1> -->
  <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
    <div class="carousel-indicators">
      <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
      <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
      <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
      <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="3" aria-label="Slide 4"></button>
      <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="4" aria-label="Slide 5"></button>
    </div>

    <div class="carousel-inner">
          <div v-for="(movie, index) in movies" :key="index">
              <div :class=" index === 0? 'carousel-item active' : 'carousel-item' " data-bs-interval="2000">
                  <img class="d-block w-100" :src="backdrop_path + movie.backdrop_path" :alt="movie.title">
                  <div class="carousel-caption d-none d-md-block">
                    <h5>{{ movie.title }}</h5>
                    <p>{{ movie.overview }}</p>
                  </div>
              </div>
          </div>
      </div>

    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
  </div>

    <!-- <div class="carousel-inner"> -->
      <!-- <div class="carousel-item active"> -->
      <!-- <CarouselItem
        v-for="movie in movies"
        :key="movie.id"
        :movie="movie"
      /> -->
      <!-- </div> -->
    <!-- </div> -->
</template>

<script>
// import _ from 'lodash'
// import CarouselItem from '@/components/CarouselItem'
export default {
  name: 'CarouselView',
  components: {
    // CarouselItem,
  },
  data() {
    return {
      backdrop_path: `https://image.tmdb.org/t/p/original/`
    }
  },
  computed: {
    movies() {
      return this.$store.state.top5Movies
      // return movies._.orderBy('popularity')
    }
  },
  created() {
    console.log(this.movies)
  }
}
</script>

<style>

</style>