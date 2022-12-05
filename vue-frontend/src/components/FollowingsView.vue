<template>
  <div>
    <a class="link m-0 fw-bold fs-3" :href="urls">{{ user.username }}</a>
    <!-- <p 
      class="m-0 fw-bold fs-3 user"
      @click="goProfile"
      >{{ user.username }}</p> -->
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'FollowingsView',
  data() {
    return {
      user: [],
      urls: `http://localhost:8080/profile/${this.userId}/`
    }
  },
  props: {
    userId: Number
  },
  created() {
    this.getUser()
  },
  methods: {
    getUser() {
      axios({
        method: 'get',
        url: `${API_URL}/userinfo/${this.userId}/`,
      })
        .then(res => {
          this.user = res.data
        })
    },
    goProfile() {
      this.$router.push({ name: 'Profile', params: { user_pk: this.userId }})
    },
  }
}
</script>

<style>

</style>