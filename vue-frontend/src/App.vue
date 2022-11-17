<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg bg-light">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">
          <img src="../src/assets/logo.png" alt="Logo" width="30" height="24" class="d-inline-block align-text-top">
          Movie
        </a>
      
        <router-link :to="{ name: 'Home' }">Home</router-link>
        <router-link :to="{ name: 'Movie' }">Movie</router-link>
        <router-link :to="{ name: 'Community' }">Community</router-link>
        <router-link :to="{ name: 'Profile', params: { username: username }  }">Profile</router-link>
        <!-- <router-link
          :to="{ name: 'Signup' }"
          :v-show="isLogin"
        >Signup</router-link>
        <router-link
          :to="{ name: 'Login' }"
          :v-show="isLogin"
        >Login</router-link> -->
        <!-- <router-link
          @click.native="logOut"
          :v-show="!this.$store.getters.isLogin"
        >Logout</router-link> -->
        <button @click="signUp" id="signup" :v-show="isLogin">Signup</button>
        <button @click="logIn" id="login" :v-show="isLogin">Login</button>
        <button @click="logOut" id="logout" :v-show="isLogin">Logout</button>
        <router-link :to="{ name: 'MovieDetail', params: { movie_id: '505642'} }">Detail</router-link>

        <form class="d-flex" role="search">
          <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
          <button class="btn btn-outline-dark" type="submit">Search</button>
        </form>

      </div>
    </nav>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  computed: {
    username(){
      return this.$store.state.username
    },
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  methods: {
    logOut() {
      this.$store.commit('LOGOUT')
    },
    // signUp() {
    //   this.$router.push({ name: 'Signup'})
    // },
    // logIn() {
    //   this.$router.push({ name: 'Login' })
    // },
    check() {
      console.log(this.isLogin)
    }
  },
  created() {
    this.check()
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: black;
  /* color: #2c3e50; */
}

/* nav {
  padding: 30px;
} */

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
