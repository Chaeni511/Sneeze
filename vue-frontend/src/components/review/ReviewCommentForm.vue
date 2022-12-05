<template>
  <div>
    <div v-if="isLogin">
      <br>
      <form @submit.prevent="createReviewComment">
        <label for="comment" class="form-label">{{ this.$store.state.username }}</label>
        <div class="d-flex justify-content-between">
          <input type="text" id="comment" class="form-control" v-model.trim="content" placeholder="악플금지!">
          <button class="btn mx-2" type="submit" style="background-color: #0072D2; color:white;">등록</button>
        </div>
      </form>
    </div>
    <div v-else><p class="ps-3">댓글을 다시려면 로그인을 하세요!</p></div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ReviewCommentForm',
  props: {
    review: Object,
  },
  data() {
    return {
      content: null,
      isLogin: this.$store.getters.isLogin,
    }
  },
  methods: {
    createReviewComment() {
      const content = this.content
      if (!content) {
        alert('내용을 입력해주세요!')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/movies/${this.review.id}/review_comment/`,
        data: {
          content,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then(() => {
          this.$emit('reviewCommentAdd')
          this.content = ''
        })
        .catch(err => console.log(err))
    },
  }
}
</script>

<style>
.comment-btn {
  background-color: #0072D2;
}
</style>