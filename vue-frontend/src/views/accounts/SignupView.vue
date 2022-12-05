<template>
  <div class="signup">
    <div class="container p-5">
      <div class="card col-md-3 m-auto p-3" id="signup" style="width: 20rem; text-align: center;">
        <div class="card-body">
          <h3 class="card-title" style="font-weight: bold;">회원가입</h3>
          <br>
          <form @submit.prevent="signUp">
              <div class="text-left ps-4">
                <label for="username" class="card-subtitle mb-2">아이디</label><br>
                <input type="text" id="username" v-model="username">
              </div>
              <br>
              <div class="text-left ps-4">
                <label for="password1" class="card-subtitle mb-2">비밀번호</label><br>
                <input type="password" id="password1" v-model="password1">
              </div>
              <br>
              <div class="text-left ps-4">
                <label for="password2" class="card-subtitle mb-2">비밀번호 재확인</label><br>
                <input type="password" id="password2" v-model="password2">
              </div>
              <br>
            <div class="d-grid col-11 mx-auto py-3">
              <input type="submit" class="btn btn-outline-light" value="SignUp">
            </div>

            <hr>
            <p class="py-1">이미 회원이십니까? <router-link :to="{ name: 'Login'}">로그인</router-link></p>
          </form>
        </div>
      </div>
    </div>

  </div>

</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username: username,
        password1: password1,
        password2: password2,
      }
      this.$store.dispatch('signUp', payload)
    },
    
  }
}
</script>

<style>
  #signup{
    width:600px;
    height: 520px;
    border-radius: 10px;
    background-color: #30333E;
    /* text-align: center; */
  }
  .signup {
    padding-bottom: 380px;
  }
</style>