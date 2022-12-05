<template>
  <div class="container" id="communityUpdate">
    <div class="row">
      <router-link class="col-1" :to="{name : 'CommunityDetail', params: { community_pk: communityId } }">
        <img src="@/assets/back.png" style="width:25px;" alt="back">
      </router-link>
      <span class="col-10" style="text-align: center;">게시글 수정</span>
    </div>
    <br>
    <form @submit.prevent="updateCommunity">
      <div class="mb-3 py-3">
        <!-- <label for="title" class="form-label">제목</label> -->
        <input type="text" class="form-control" id="title1" aria-describedby="titleHelp" v-model.trim="title">
        <div id="titleHelp" class="form-text">100자 이하</div>
      </div>
      <div class="mb-3 py-3">
        <!-- <label for="content" class="form-label">내용</label> -->
        <textarea type="text" class="form-control" id="content" v-model.trim="content" style="height: 500px;"></textarea>
      </div>
      <button type="submit" class="btn btn-primary">수정</button>
    </form>
  </div>

  
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommunityDetailUpdateView',
  data() {
    return {
      communityId: this.$route.params.community_pk.toString(),
      title: null,
      content: null,
    }
  },
  created() {
    this.getCommunityDetail()
  },
  methods: {
    getCommunityDetail(){
      // console.log(this.communityId)
      axios({
        method: 'get',
        url: `${API_URL}/community/detail/${this.communityId}/`, 
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
      })
        .then(res => {
          // console.log(res)
          this.title = res.data.title
          this.content = res.data.content
        })
        .catch(err => console.log(err))
    },
    updateCommunity() {
      const title = this.title
      const content = this.content
      if (!title) {
        alert('제목을 입력해주세요!')
        return
      } else if (!content) {
        alert('내용을 입력해주세요!')
        return
      }
      axios({
        method: 'put',
        url: `${API_URL}/community/community/${this.communityId}/`,
        data: {
          title,
          content,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          this.$router.push({ name: 'CommunityDetail', params: { community_pk: res.data.id }})
        })
    }
  }
}
</script>

<style>
#communityUpdate {
  width:800px;
  min-height: 500px;
  height: auto;
  padding: 3%;
  margin-top: 50px;
  border-radius: 10px;
  background-color: #30333E;
  /* text-align: center; */
}
</style>