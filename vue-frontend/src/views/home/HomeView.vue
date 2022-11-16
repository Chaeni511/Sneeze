<template>
  <div>
    <h1>HOME</h1>
    <CarouselList/>
    <RecommendationView/>
  
  </div>
</template>

<script>
import CarouselList from '@/components/CarouselList'
import RecommendationView from '@/views/home/RecommendationView'

export default {
  name: 'HomeView',
  components: {
    CarouselList,
    RecommendationView
  },
  methods: {
    getMovies() {
      // if (this.isLogin) {
        this.$store.dispatch('getMovies')
      // } else {
        //   alert('로그인이 필요한 서비스 입니다.')
      //   this.$router.push({ name: 'LogInView'})
      },
      getTop5Movies() {
        // if (this.isLogin) {
          this.$store.dispatch('getTop5Movies')
        // } else {
          //   alert('로그인이 필요한 서비스 입니다.')
        //   this.$router.push({ name: 'LogInView'})
        },
    },
    created() {
      this.getMovies()
      this.getTop5Movies()
    },
    
  }
    
// }

</script>

<style>

</style>