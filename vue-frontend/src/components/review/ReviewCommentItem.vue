<template>
  <div class="container">
    <div v-if="update">
      <div class="row justify-content-between">
        <div class="col-3 d-flex justify-content-start pb-2">
          <img src="@/assets/user.png" alt="profile" style="height:40px;width:40px;">
          <p 
            class="m-0 fw-bold fs-3 col-3 user"
            @click="goProfile"
          >{{ comment.userName }}</p>
        </div>
        <div class="col-3 d-flex justify-content-end" v-if="this.me.username === comment.userName">
          <span class="mx-2" @click="updateForm" style="cursor: pointer">수정</span>
          <span class="mx-2" @click="deleteComment" style="cursor: pointer">삭제</span>
        </div>
      </div>
      <p id="commentContent">{{ comment.content }}</p>
    </div>

    <div v-else>
      <p id="commentUsername">{{ comment.userName }}</p>
      <form @submit.prevent="updateComment">
        <div class="d-flex justify-content-between">
          <input type="text" id="content" class="form-control" v-model.trim="updateContent" value="updateContent">
          <button class="btn mx-2" type="submit" style="background-color: #0072D2; color:white;">등록</button>
          <button class="btn mx-2" type="submit" style="background-color: #0072D2; color:white;" @click="cancelUpdate">취소</button>
        </div>
      </form>
    </div>
    <hr>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ReviewCommentItem',
  props: {
    comment: Object,
    review: Object,
  },
  data() {
    return {
      update: true,
      updateContent: this.comment.content,
      me: [],
    }
  },
  created() {
    this.getMe()
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
    deleteComment() {
      axios({
        method: 'delete',
        url: `${API_URL}/movies/review_comment/${this.review.id}/${this.comment.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then(() => {
          this.$emit('delComment')
        })
    },
    updateForm() {
      this.update = !this.update
    },
    cancelUpdate() {
      this.update = !this.update
    },
    updateComment() {
      const updateContent = this.updateContent
      if (!updateContent) {
        alert('내용을 입력해주세요!')
        return
      }
      axios({
        method: 'put',
        url: `${API_URL}/movies/review_comment/${this.review.id}/${this.comment.id}/`,
        data: {
          content: updateContent,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
      })
        .then(() => {
          this.update = !this.update
          this.$emit('updateComment')
        })
    },
    goProfile() {
      this.$router.push({ name: 'Profile', params: { user_pk: this.review.user }})
    },
  },
}
</script>

<style>

</style>