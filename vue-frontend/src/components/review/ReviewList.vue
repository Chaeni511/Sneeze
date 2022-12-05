<template>
  <div class="review-list">
    <div v-if="reviews?.length">
      <hr>
      <ReviewItem
        v-for="review in this.reviews"
        :key="review.created_at"
        :review="review"
        :movie="movie"
      />
    </div>
    <div v-else class="text-center">
      <h4>리뷰가 없습니다.</h4>
    </div>
  </div>
</template>

<script>
import ReviewItem from '@/components/review/ReviewItem.vue'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieReviewView',
  data() {
    return {
      reviews: null,
    }
  },
  props: {
    movieId: String,
    movie: Object,
  },
  components: {
    ReviewItem,
  },
  created() {
    this.getReviews()
  },
  methods: {
    reviewForm() {
      this.$router.push({ name: 'ReviewForm', params: {
        movie_id: this.movieId,
        movie_pk: this.movie.id
       }})
    },
    getReviews() {
      axios({
        method: 'get',
        url: `${API_URL}/movies/${this.movie.id}/review_list_create/`,
      })
      .then(res => {
        this.reviews = res.data
        // console.log(this.reviews)
      })
      .catch(err => {console.log(err)})
    },

  }
}
</script>

<style>
.review-list{
  background-color: #30333E;
  padding: 3%;
  border-radius: 10px;
}
</style>