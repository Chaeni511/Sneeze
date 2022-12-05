<template>
  <div class="container" id="background">
    <div class="row">
      <router-link class="col-1" :to="{name: 'MovieDetail', params: { movie_id: movieId } }">
        <img src="@/assets/back.png" style="width:25px;" alt="back">
      </router-link>
      <span class="col-10" style="text-align: center;">리뷰 작성</span>
    </div>
    <br>
    <form @submit.prevent="createReview">
      <div class="mb-3 py-3">
        <input type="text" class="form-control" id="title1" aria-describedby="titleHelp" v-model.trim="title" placeholder="제목">
        <div id="titleHelp" class="form-text">100자 이하</div>
      </div>
      <div class="mb-3 py-3">
        <textarea type="text" class="form-control" id="content" v-model.trim="content" placeholder="내용" style="height: 500px;"></textarea>
      </div>
      <div class="mb-3 py-3" style="width:80px;">
        <input type="number" class="form-control" id="content" min="0" max="10" aria-describedby="rankHelp" v-model.trim="rank" placeholder="평점">
        <div id="rankHelp" class="form-text">0 ~ 10점</div>
      </div>
      <button type="submit" class="btn btn-primary">등록</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ReviewForm',
  data() {
    return {
      title: null,
      content: null,
      rank: null,
      movieId: this.$route.params.movie_id,
      moviePk: this.$route.params.movie_pk,
    }
  },
  methods: {
    createReview() {

      const title = this.title
      const content = this.content
      const rank = this.rank
      if (!title) {
        alert('제목을 입력해주세요!')
        return
      } else if (!content) {
        alert('내용을 입력해주세요!')
        return
      } else if (!rank) {
        alert('평점을 입력해주세요!')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/movies/${this.movieId}/review_list_create/`,
        data: {
          title,
          content,
          rank,
          movie: this.moviePk,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then(() => {
          this.$router.push({ name: 'MovieDetail', params: { movie_id: this.movieId }})
        })
    }
  }
}
</script>

<style>

</style>