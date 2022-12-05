<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg d-flex justify-content-between px-4">
      <!-- <div class="container-fluid"> -->
        <div class="row col-6">
          <a class="navbar-brand col-lg-3 col-12 text-center" href="http://localhost:8080/">
            <img src="../src/assets/logo.png" alt="Logo" class="d-inline-block align-text-top"
            style="width: 100px;"
            >
            <!-- <span class="col-6" style="color:white;"> Movie</span> -->
          </a>
          <router-link class="col-lg-2 col-12 mt-2 text-center fs-4" :to="{ name: 'Home' }">홈</router-link>
          <router-link class="col-lg-2 col-12 mt-2 text-center fs-4" :to="{ name: 'Movie' }">영화</router-link>
          <router-link class="col-lg-2 col-12 mt-2 text-center fs-4" :to="{ name: 'Community' }">게시판</router-link>
        </div>
      
        <div class="row">
          <span class="col-12 px-4 d-flex justify-content-between" v-if="!isLogin">
            <router-link class="px-3" :to="{ name: 'Signup' }">회원가입</router-link> 
            <router-link class="px-3" :to="{ name: 'Login' }">로그인</router-link>
          </span>
          <span class="nav-item dropdown col-12 px-4 d-felx justify-content-right" v-else>
            <a class="nav-link dropdown-toggle d-flex justify-content-around align-items-center" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              <p class="pe-3 mt-3 fs-4">{{ this.$store.state.username }}</p>
              <img src="@/assets/user.png" alt="profile" style="height:40px;">
            </a>
            <ul class="dropdown-menu">
              <li>
                <router-link class="dropdown-item" :to="{ name: 'MyProfile', params: { username: username }  }">프로필</router-link>
              </li>
              <li>
                <div class="dropdown-item" @click="logOut" v-show="isLogin" style="cursor: pointer;">로그아웃</div>
              </li>
            </ul>
          </span>
        <!-- </div> -->
      </div>
    </nav>
    <router-view></router-view>
    <!-- <div style="height: 80vh"></div> -->
    <footer>
      <p>ⓒ SNEEZE</p>
      <p>Chaeeun Lee | e-mail: chaen511@naver.com</p>
      <p>Jaegun Seo | e-mail: sjk1052005@gmail.com </p>
    </footer>
  </div>
</template>

<script>
export default {
  computed: {
    username(){
      return this.$store.state.username
    },
    isLogin(){
      return this.$store.getters.isLogin
    },
  },
  methods: {
    logOut() {
      this.$store.commit('LOGOUT')
    },
    logIn() {
      this.$router.push({ name: 'Login'})
    },
    signUp() {
      this.$router.push({ name: 'Signup'})
    },
  },
}
</script>

<style>

#all {
  margin: 0 auto;
  background: linear-gradient(0deg, rgba(45,47,59,1) 0%, rgba(8,9,14,1) 35%);
  background-size: cover;
  background-repeat: no-repeat;
  min-height: 100vh;
  position: relative;
}

#app {
  font-family: 'Nanum Gothic', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  height :100%;
  margin: 0; 
  color: white;
} 

nav {
  background-color: #08090E;
}

nav a {
  font-weight: bold;
  color: white;
  text-decoration: none;
}

nav a.router-link-exact-active {
  color: #0072D2;
  text-decoration: none;
}

.user:hover { 
  text-decoration:underline;
  color:#0072D2;
  cursor: pointer;
}

.link {
  color: white;
  text-decoration: none;
}

.link:hover {
  text-decoration:underline;
  color:#0072D2;
}

#background {
  width:800px;
  /* min-height: 600px; */
  height: auto;
  padding: 3%;
  margin-top: 50px;
  border-radius: 10px;
  background-color: #30333E;
}

footer {
  position: relative;
  /* float: left; */
  /* left: 5.00%; */
  width: 100%;
  /* margin: 10px 0px; */
  /* bottom: 0;
  width: 100%;
  position : fixed; */
  height: 150px;
  background-color: #08090E;
  color: white;
  margin: 20px 0 0 0;
  padding-top: 20px;
  text-align: center;
}
</style>
