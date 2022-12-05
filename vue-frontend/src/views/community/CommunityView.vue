<template>
  <div class="container community">
    <div class="row justify-content-space-between">
      <h1 class="col align-right">게시판</h1>
      <div class="col-1" @click="goCreate">
        <img class="d-flex justify-content-end" src="@/assets/plus.png" style="width:45px; cursor: pointer;">
      </div>
    </div>
    <br>
    <div class="row d-flex justify-content-around text-center">
      <p class="col-3">제목</p>
      <p class="col-2">작성자</p>
      <p class="col-2">작성일</p>
    </div>
    <hr>
    <div>
      <CommunityListItem
        v-for="community in communities"
        :key="community.created_at"
        :community="community"
      />
    </div>
  </div>
</template>

<script>
import CommunityListItem from '@/components/community/CommunityListItem.vue'

export default {
  name:'CommunityView',
  data() {
    return {
      isLogin: this.$store.getters.isLogin,
    }
  },
  components: {
    CommunityListItem,
  },
  computed: {
    communities() {
      return this.$store.state.communities
    }
  },
  methods: {
    getCommunityList() {
      this.$store.dispatch('getCommunityList')
    },
    goCreate() {
      if (this.isLogin === false) {
        alert('게시글을 작성하시려면 로그인을 하세요!')
        return
      }
      this.$router.push({ name: 'CommunityCreate' })
    }
  },
  created() {
    this.getCommunityList()
  }
}
</script>

<style>
.community {
  padding-bottom: 450px;
}
</style>