<template>
  <div class="px-3">
    <div
      class="text-light py-2 px-2"
      @click="reviewDetail"
      style="cursor: pointer"
    >
      <div class="d-flex justify-content-between align-items-center">
        <div class="row col-3 d-flex align-items-center p-0">
          <div class="row">
            <img class="col-4 pe-0" src="@/assets/user.png" alt="user" style="width:56px;">
            <p 
              class="m-0 fw-bold fs-4 col-6 user"
              @click="goProfile"
            >{{ review.userName }}</p>
          </div>
          <p class="m-0" style="fs-small;">{{ review.created_at }}</p>
        </div>

        <!-- {{ review }} -->

        <div>
          {{ review.rank }}
          <img src="@/assets/star.png" style="width: 20px; height: 10px margin-left: 1rem;">
        </div>
      </div>
      <p class="mt-3 mb-1 fs-4">{{ review.content }}</p>
    </div>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'ReviewItem',
  props: {
    review: Object,
    movie: Object,
  },
  methods: {
    reviewDetail() {
      this.$router.push({ name: 'ReviewDetail', params: { 
        review_pk: this.review.id,
        movie_id: this.movie.movie_id,
        movie_pk: this.movie.id
      }})
    },
    goProfile() {
      this.$router.push({ name: 'Profile', params: { user_pk: this.review.user }})
    }
  }
}
</script>

<style>

</style>