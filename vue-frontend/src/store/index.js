import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import _ from 'lodash'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'
const API_KEY = 'c12ca67b05f1378e09cf647da6b26b3e'


export default new Vuex.Store({
  state: {
    movies: [],
    movieGenre: [],
    cosMovies: [],
    top5Movies: [],

  },
  getters: {
  },
  mutations: {
    GET_MOVIES(state, movies) {
      state.movies = movies
    },
    GET_COS_MOVIE(state, cosMovies) {
      state.cosMovies = cosMovies
    },
    GET_TOP5_MOVIES(state, top5Movies) {
      state.top5Movies = top5Movies
    }
  },
  actions: {
    getMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/`,
        // headers: {
        //   Authorization: `Token ${context.state.token}`
        // },
      })
        .then((res) => {
          console.log(res)
          context.commit('GET_MOVIES', res.data)
        })
        .catch(err => console.log(err))
    },
    getCosMovie(context, movie_id){
      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/${movie_id}/recommendations?api_key=${API_KEY}&language=ko-KR&page=1`
      })
        .then(res => {
          // console.log(res.data.results)
          context.commit('GET_COS_MOVIE', res.data.results)
        })
    },
    // 인기도 탑 5
    getTop5Movies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/`,
        // headers: {
        //   Authorization: `Token ${context.state.token}`
        // },
      })
        .then((res) => {
          console.log(res)
          const movies = res.data
          _.sortBy(movies, 'popularity').reverse()
          const top5Movies = movies.slice(0, 5)
          console.log(top5Movies)
          context.commit('GET_TOP5_MOVIES', top5Movies)
        })
        .catch(err => console.log(err))
    },
  },
  modules: {
  }
})
