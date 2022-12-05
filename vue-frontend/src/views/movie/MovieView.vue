<template>
  <div class="movie-card">
    <div class=" d-flex justify-content-center">
      <form @submit.prevent="searchMovie" class="form row col-10 mb-5">
        <!-- <label for="search" class="h1">영화 검색</label> -->
        <input type="search" id="search" v-model="title" @input="searchMovie" class="form-control col" style="height:60px;" placeholder="영화제목을 입력하세요.">
        <button class="btn btn-primary col-1 ms-3">검색</button>
      </form>

    </div>
    <div class="popular-list row gy-4 mx-2"
      v-if="movies"
    >
        <MovieCardView
          v-for="movie in movies"
          :key="movie.created_at"
          :movie="movie"
        />
    </div>
    <div v-show="movies?.length === 0"> 
      <div class="text-center pt-5">
        <img src="@/assets/nothing.png" alt="없어요. 그냥 없어요">
        <p class="p-5 h1">찾으시는 영화가 없습니다. 흑흑</p>
      </div>
    </div>
    <br><br><br><br>
    <div v-show="!title">
      <b-pagination
        @input="getList"
        v-model="currentPage"
        :total-rows="total_row"
        :per-page="perPage"
        aria-controls="my-table"
        align="center"
      ></b-pagination>

      <b-table
        id="my-table"
        :movies="movies"
        :per-page="perPage"
        :current-page="currentPage"
        small
      ></b-table>
    </div>
  </div>
</template>

<script>
import MovieCardView from '@/components/MovieCardView'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieView',
  components: {
    MovieCardView
  },
  data () {
    return {
      title: null,
      movies: null,
      // list: [],
      currentPage: 1,
      perPage: 5,
      total_row: 20,
      notMovies: false,
    }
  },
  created() {
    this.getList()
  },
  methods: {
    getList() {
      // console.log(this.currentPage)
      axios({
        methods: 'get',
        url: `${API_URL}/movies/list/?page=${this.currentPage}`,
      })
        .then(res => {
          // console.log(res)
          this.movies = res.data.results
          this.total_row = parseInt(res.data.count / 20)
          this.searchCardMovie()
        })
    },
    searchMovie() {
      const moviedata = this.$store.state.movies
      if (this.title) {
        const searchMovies = moviedata.filter(movie => {
          return movie.title.includes(this.title)
        })
        this.movies = searchMovies
      } 
      else {
        this.getList()
      }
    },
    searchCardMovie() {
      if ( this.$route.params.title ) {
        this.title = this.$route.params.title
        this.$route.params.title = null
        const moviedata = this.$store.state.movies
        if (this.title) {
          const searchMovies = moviedata.filter(movie => {
            return movie.title.includes(this.title)
          })
          this.movies = searchMovies
        } 
      }
    },
  }
}
</script>

<style>
  .movie-card {
    padding: 5% 15%;
  }
  .popular-list {
    display: flex;
    margin-left: 5rem;
    margin-right: 5rem;
  }
</style>