<template>
  <div>
    <div class="container" id="background">
      <div class="row">
        <router-link class="col-1" :to="{name: 'MovieDetail', params: { movie_id: movieId } }">
          <img src="@/assets/back.png" style="width:25px;" alt="back">
        </router-link>
        <span class="col-10" style="text-align: center;">리뷰 : <span>"{{ review?.movie_title }}"</span></span>
      </div>
      <br>
      <div class="p-3">
        <div class="row d-flex justify-content-between">
          <h2 class="col-3 fw-bold">{{ review?.title }}</h2>

          <div class="col-2 d-flex justify-content-end" v-if="this.me.username === review?.userName">
            <span class="px-2" @click="updateReview">
              <img src="@/assets/pencil.png" style="width:28px; cursor: pointer;" alt="edit">
            </span> 
            <span class="px-2" @click="deleteReview">
              <img src="@/assets/trash.png" style="width:30px; cursor: pointer;" alt="edit">
            </span>
          </div>
        </div>
    
        <div class="row">
          <!-- <img class="col-2" src="@/assets/user.png" alt="profile" style="height:50px; width:70px;"> -->
          <!-- <div class="col-3"> -->
            <div class="d-flex justify-content-between">
              <h5 class="m-0 fw-bold fs-4 user">{{ review?.userName }}</h5>
              <div class="pe-2">
                {{ review?.rank }}
                <img src="@/assets/star.png" style="width: 20px; height: 10px margin-left: 1rem;">
              </div>
            </div>
            <p><small>{{ review?.updated_at }}</small></p>
          <!-- </div> -->
        </div>
        <div class="row">
          <p>{{ review?.content }}</p>
        </div>
        <hr>
        <div v-if="review">
          <div v-if="comments">
            <ReviewCommentItem
              @delComment="delComment"
              @updateComment="updateComment"
              v-for="comment in comments"
              :key="comment.created_at"
              :comment="comment"
              :review="review"
            />
          <ReviewCommentForm
            @reviewCommentAdd="reviewCommentAdd"
            :review="review"
            class="p-3"
          />
        </div>
      </div>
      </div>
      
      </div>
  </div>
</template>

<script>
import axios from 'axios'
import ReviewCommentItem from '@/components/review/ReviewCommentItem'
import ReviewCommentForm from '@/components/review/ReviewCommentForm'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ReviewDetail',
  data() {
    return {
      review: null,
      reviewId: this.$route.params.review_pk,
      comments: null,
      movieId: this.$route.params.movie_id,
      moviePk: this.$route.params.movie_pk,
      me: [],
    }
  },
  components: {
    ReviewCommentItem,
    ReviewCommentForm,
  },
  created() {
    this.getMe()
    this.getReview()
    this.getReviewComments()
  },
  methods: {
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
        })
    },
    getReview() {
      axios({
        method: 'get',
        url: `${API_URL}/movies/review_detail/${this.reviewId}/`
      })
        .then(res => {
          this.review = res.data
        })
    },
    getReviewComments() {
      axios({
        method: 'get',
        url: `${API_URL}/movies/review_comments/${this.reviewId}/`
      })
        .then(res => {
          this.comments = res.data
        })
    },
    reviewCommentAdd() {
      this.getReviewComments()
    },
    delComment() {
      this.getReviewComments()
    },
    updateComment() {
      this.getReviewComments()
    },
    deleteReview() {
      axios({
        method: 'delete',
        url: `${API_URL}/movies/review/${this.reviewId}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then(() => {
          this.$router.push({ name: 'MovieDetail', params: { movie_id: this.movieId }})
        })
    },
    updateReview() {
      this.$router.push({ name: 'ReviewUpdate', params: {
        movie_id: this.movieId,
        movie_pk: this.moviePk,
        review_pk: this.reviewId
      }})
    }
  }
}
</script>

<style>

</style>