<template>
  <div class="movie-detail-card">
    <div class="d-flex justify-content">
      <!-- 포스터 -->
      <div class="movie-detail-poster pe-4" v-if="movie">
        <img :src="this.imageUrl + movie?.poster_path" alt="포스터 없음">
      </div>
      <!-- 포스터 끝 -->

      <!-- 영화 정보 -->
      <div class="container">
        <div class="row d-flex justify-content-between">
          <!-- 제목 & 별점 -->
          <span class="col-10 movie-detail-title">
            <p>{{ movie?.title }}</p>
          </span>

          <div class="col-2 d-flex justify-content-left">
            <img id="movie-star" src="@/assets/star.png" style="height:50px;">
            <div class="movie-vote px-2">
              {{ movie?.vote_average }}
            </div>
          </div>

          <!-- 개봉일 -->
          <div v-if="movie?.release_date" class="movie-release-date">
            개봉 : {{ movie.release_date }}
          </div>
          <!-- 개봉일 끝 -->

          <!-- 줄거리 -->
          <div class="movie-detail-header">
            <p class="mb-1">줄거리</p>
          
            <hr class="my-1">
            <div v-if="movie?.overview" class="movie-detail-body">
              {{ movie?.overview }}
            </div>
            <div v-else class="movie-detail-overview-body">
              해당 영화는 줄거리가 제공되지 않습니다.
            </div>
          </div>
          <!-- 줄거리 끝 -->

          <!-- 좋아요, 리뷰 작성 -->
          <div class="d-flex justify-content-end align-middle movie-detail-header">
            <span class="d-flex align-items-baseline ms-2 p-2 heart-box"      @click="like">
              <i v-if="isLiked" class="bi bi-heart-fill heart" style="height:50px;"></i>
              <i v-else class="bi bi-heart heart"></i>
              <p class="px-2">좋아요</p>
              <!-- <p class="ps-2">{{ this.likeNumber }}개</p> -->
            </span>

            <span class="d-flex justify-content-space-between ms-2 p-2 review-create" @click="reviewForm">
              <img class="pt-2 pb-0" src="@/assets/plus.png" style="height:40px;">
              <p class="px-2">리뷰 쓰기</p>
            </span>
          </div>
          <!-- 좋아요, 리뷰작성 끝 -->
      </div>
    </div>
  </div>
  <br>
  <br>
  <br>
  <!-- 탭 -->
  <!-- 탭 -->
    <ul class="nav nav-tabs" id="myTab" role="tablist">
      <li class="nav-item" role="presentation">
        <button class="nav-link active" id="home-tab" data-bs-toggle="tab" data-bs-target="#home-tab-pane" type="button"
          role="tab" aria-controls="home-tab-pane" aria-selected="true">리뷰</button>
      </li>
      <li class="nav-item" role="presentation">
        <button class="nav-link" id="profile-tab" data-bs-toggle="tab" data-bs-target="#profile-tab-pane" type="button"
          role="tab" aria-controls="profile-tab-pane" aria-selected="false">관련 영상</button>
      </li>
      <li class="nav-item" role="presentation">
        <button class="nav-link" id="contact-tab" data-bs-toggle="tab" data-bs-target="#contact-tab-pane" type="button"
          role="tab" aria-controls="contact-tab-pane" aria-selected="false">추천 영화</button>
      </li>
      <li class="nav-item" role="presentation">
        <button class="nav-link" id="similar-tab" data-bs-toggle="tab" data-bs-target="#similar-tab-pane" type="button"
          role="tab" aria-controls="similar-tab-pane" aria-selected="false">비슷한 영화</button>
      </li>

    </ul>
    <div class="tab-content" id="myTabContent">
      <div class="tab-pane fade show active" id="home-tab-pane" role="tabpanel" aria-labelledby="home-tab" tabindex="0">
        <div v-if="movie">
          <ReviewList :movieId="movieId" :movie="movie" class="m-3" />
        </div>
      </div>
      <div class="tab-pane fade" id="profile-tab-pane" role="tabpanel" aria-labelledby="profile-tab" tabindex="0">
        <div class="d-flex justify-content-start flex-wrap" v-if="youtubeVideos.length">
          <YoutubeItem
            v-for="(youtube, idx) in youtubeVideos"
            :key="idx"
            :youtube="youtube"
          />
        </div>
        <div v-else class="text-center p-5">
          <h4>관련 영상이 없습니다.</h4>
        </div>
      </div>

      <div class="tab-pane fade" id="contact-tab-pane" role="tabpanel" aria-labelledby="contact-tab" tabindex="0">
        <div class="row popular-list">
          <MovieDetailCard
            v-for="movie in cosMovies"
            :key="movie.created_at"
            :movie="movie"
          />
        </div>
      </div>

      <div class="tab-pane fade" id="similar-tab-pane" role="tabpanel" aria-labelledby="similar-tab" tabindex="0">
        <div class="row popular-list">
          <MovieDetailCard
            v-for="movie in similarMovies"
            :key="movie.created_at"
            :movie="movie"
          />
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import ReviewList from '@/components/review/ReviewList'
import axios from 'axios'
import MovieDetailCard from './MovieDetailCard.vue'
import YoutubeItem from '@/components/YoutubeItem.vue'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieDetailView',
  components: {
    ReviewList,
    MovieDetailCard,
    YoutubeItem,
  },
  data() {
    return {
      imageUrl: 'https://image.tmdb.org/t/p/original',
      youtubeEmbeded: 'https://www.youtube.com/embed',
      movieId: this.$route.params.movie_id.toString(),
      movie: null,
      isLiked: false,
      me: null,
      likeNumber: '',
      cosMovies: this.$store.state.cosMovies,
      similarMovies: this.$store.state.similarMovies,
      isLogin: this.$store.getters.isLogin,
    }
  },
  computed: {
    recoMovies() {
      return this.$store.state.cosMovies
    },
    youtubeVideos() {
      return this.$store.state.youtubeVideos
    },
  },
  created() {
    this.getMovie(this.$route.params.movie_id)
    this.getMe()
    this.getCosMovie()
    this.getSimilarMovie()
    this.searchYoutube()
  },
  methods: {
    reviewForm() {
      if (this.isLogin === false) {
        alert('리뷰 작성을 하시려면 로그인을 하세요!')
        return
      }
      this.$router.push({ name: 'ReviewForm', params: {
        movie_id: this.movieId,
        movie_pk: this.movie.id
       }})
    },
    getCosMovie() {
      this.$store.dispatch('getCosMovie', this.movieId)  // 디테일 페이지의 영화 id
    },
    getSimilarMovie() {
      this.$store.dispatch('getSimilarMovie', this.movieId)
    },
    getMovie(movieId) {
      // console.log(movieId)
      axios({
        method: 'get',
        url: `${API_URL}/movies/${movieId}/`,
        data: {
          movie_id: movieId
        }
      })
        .then(res => {
          // console.log(res.data)
          this.movie = res.data
          this.likeNumber = this.movie.like_users.length
        })
        .catch(err => {
          console.log(err)
          this.$router.push({ name: 'NotFound404' })
        })
    },
    searchYoutube() {
      this.$store.dispatch('searchYoutube', this.movieId)
    },
    getMe() {
      if (this.$store.getters.isLogin === false) {
        return
      }
      axios({
        method: 'get',
        url: `${API_URL}/accounts/user/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
      })
        .then(res => {
          this.me = res.data
          this.islike()
        })
    },
    like() {
      if (this.isLogin === false) {
        alert('좋아요를 하시려면 로그인을 하세요!')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/movies/${this.me.pk}/${this.movieId}/like/`,
        data: {
          myId: this.me.id,
          movieId: this.movie.id,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
      })
        .then(res => {
          this.isLiked = res.data
          if (this.isLiked === false) {
            this.likeNumber -= 1
          } else {
            this.likeNumber += 1
          }
        })
    },
    islike() {
      axios({
        method: 'post',
        url: `${API_URL}/movies/${this.me.pk}/${this.movieId}/is_liked/`,
        data: {
          myId: this.me.id,
          movieId: this.movieId,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
      })
        .then(res => {
          this.isLiked = res.data
        })
    },
  },

}
</script>

<style>

.movie-detail-card {
  font-family: 'Noto Sans KR', sans-serif;
  display: flex;
  flex-flow: column nowrap;
  justify-content: center;
  padding: 50px 15%;
  min-height: 100%;
  height: auto;
  /* background-color: #000000; */
  /* color: white; */
}

.movie-detail-toolbar {
  height: 56px;
}

/* .movie-detail-body {
  display: flex;
  flex-flow: row wrap;
  margin: 1rem;
} */

.movie-detail-info {
  display: flex;
  flex-flow: column wrap;
  justify-content: space-between;
  margin: 1rem 0 0 4rem;
  width: 60%;
}

.movie-detail-info-header {
  display: flex;
  flex-flow: row nowrap;
  justify-content: space-between;
  height: 80px;
}

.movie-detail-poster>img {
  width: 400px;
}

.movie-detail-title {
  font-size: 40px;
  font-weight: bolder;
}

.movie-detail-info-header-right {
  display: flex;
  flex-flow: row nowrap;
  align-items: center;
}

.movie-vote {
  font-size: 30px;
}

#movie-star {
  height: 50%;
  margin-left: 1rem;
}

.movie-detail-header {
  margin-top: 5rem;
  padding-top: 5rem;
  font-size: 32px;
}

.movie-detail-body {
  font-size: 20px;
}
.heart {
  color: crimson;
  margin: 0px auto;
  -webkit-transition-duration: 0.4s;
  transition-duration: 0.4s;
}

.heart-box, .review-create {
  cursor: pointer;
}

</style>
