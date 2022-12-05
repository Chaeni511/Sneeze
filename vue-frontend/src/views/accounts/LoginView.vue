<template>
  <div class="container login">
    <div class="card col-md-3 m-auto p-3" id="login" style="width: 20rem; text-align: center;">
      <div class="card-body">
        <h3 class="card-title" style="font-weight: bold;">로그인</h3>
        <br>
        <form @submit.prevent="logIn">
          <div class="text-left ps-4">
            <label for="username" class="card-subtitle mb-2text-start">아이디</label><br>
            <input type="text" id="username" v-model="username">
          </div>
          <br>
          <div class="text-left ps-4">
            <label for="password" class="card-subtitle mb-2">비밀번호</label><br>
            <input type="password" id="password" v-model="password">
          </div>
          <br>
          <div class="d-grid col-11 mx-auto py-3">
            <input type="submit" class="btn btn-outline-light" value="logIn">
          </div>

          <hr>
          <p class="py-1">아직 회원이 아니십니까? <router-link :to="{ name: 'Signup'}">회원가입</router-link></p>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LogInView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    logIn() {
      const username = this.username
      const password = this.password

      const payload = {
        username: username,
        password: password,
      }
      this.$store.dispatch('logIn', payload)
    }
  }
}
</script>

<style>
  #login{
    width:600px;
    height: 430px;
    border-radius: 10px;
    background-color: #30333E;
  }
  .login {
    padding-bottom: 565px;
  }
</style>