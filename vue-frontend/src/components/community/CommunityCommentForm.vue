<template>
  <div>
    <form @submit.prevent="createComment">
      <label for="comment" class="form-label">{{ this.$store.state.username }}</label>
      <div class="d-flex justify-content-between">
        <input type="text" id="comment" class="form-control" v-model.trim="content" placeholder="악플금지!">
        <button class="btn mx-2" type="submit" style="background-color: #0072D2; color:white;">등록</button>
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommunityCommentForm',
  data() {
    return {
      content: null,
    }
  },
  props: {
    communityId: String
  },
  methods: {
    createComment() {
      const content = this.content
      if (!content) {
        alert('내용을 입력해주세요!')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/community/${this.communityId}/comment/`,
        data: {
          content,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then(() => {
          this.$emit('comment_add')
          this.content = ''
        })
        .catch(err => console.log(err))
    }
  }
}
</script>

<style>

</style>