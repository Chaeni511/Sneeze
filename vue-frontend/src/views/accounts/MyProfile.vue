<template>
  <div class="container my-profile">
    <!-- 프로필 -->
    <div class="row">
      <div class="col-sm-3 col-12">
        <img src="@/assets/user.png" alt="profile" style="width:150px;">
      </div>
      <div class="col-sm-9 col-12">
        <div class="col-12 d-flex justify-content-around pb-2">
          <h1>{{ user?.username }}</h1>
        </div>
        <div class="col-sm-12 divider text-center row d-flex justify-content-around" style="margin-bottom:20px">
            <div class="col-sm-3 col-12 follow-info" @click="open1">
              <h2><strong>{{ followersLength }}</strong></h2>                    
              <p><small>팔로워</small></p>
            </div>
            <div class="col-sm-3 col-12 follow-info" @click="open2">
              <h2><strong>{{ followingsLength }}</strong></h2>                    
              <p><small>팔로잉</small></p>
            </div>
            <div class="col-sm-3 col-12">
              <h2><strong>{{ user.like_movies?.length }}</strong></h2>                    
              <p><small>좋아요한 영화 수</small></p>
            </div>
        </div>            
      </div>
    </div>
    <br>
    <!-- 프로필 끝 -->

    <!-- 팔로잉 모달 -->
    <b-modal
      hide-footer
      v-model="show2"
      id="review-modal"
      size="sm"
      title="팔로잉"
      :header-bg-variant="headerBgVariant"
      :header-text-variant="headerTextVariant"
      :body-bg-variant="bodyBgVariant"
      :body-text-variant="bodyTextVariant"
      :footer-bg-variant="footerBgVariant"
      :footer-text-variant="footerTextVariant"
    >
      <section class="page-section" id="contact">
        <div class="control-group">
            <div v-for="(userId, idx) in user?.followings" :key="idx" style="cursor:pointer" class="content-font form-group floating-label-form-group controls mb-0 pb-2">
                <FollowingsView :userId="userId" />
            </div>
        </div>
      </section>
    </b-modal>
    <!-- 팔로잉 모달 끝 -->

    <!-- 팔로워 모달 -->
    <b-modal
      hide-footer
      v-model="show1"
      id="review-modal"
      size="sm"
      title="팔로워"
      :header-bg-variant="headerBgVariant"
      :header-text-variant="headerTextVariant"
      :body-bg-variant="bodyBgVariant"
      :body-text-variant="bodyTextVariant"
      :footer-bg-variant="footerBgVariant"
      :footer-text-variant="footerTextVariant"
    >
      <section class="page-section" id="contact">
        <div class="control-group">
            <div v-for="(userId, idx) in user?.followers" :key="idx" style="cursor:pointer" class="content-font form-group floating-label-form-group controls mb-0 pb-2">
                <FollowersView :userId="userId" />
            </div>
        </div>
      </section>
    </b-modal>
    <!-- 팔로워 모달 끝 -->
    
    <!-- 탭 -->
    <ul class="nav nav-tabs" id="myTab" role="tablist">
      <li class="nav-item" role="presentation">
        <button class="nav-link active" id="home-tab" data-bs-toggle="tab" data-bs-target="#home-tab-pane" type="button"
          role="tab" aria-controls="home-tab-pane" aria-selected="true">좋아요 영화</button>
      </li>
      <li class="nav-item" role="presentation">
        <button class="nav-link" id="profile-tab" data-bs-toggle="tab" data-bs-target="#profile-tab-pane" type="button"
          role="tab" aria-controls="profile-tab-pane" aria-selected="false">리뷰 영화</button>
      </li>

    </ul>
    <div class="tab-content" id="myTabContent">
      <div class="tab-pane fade show active" id="home-tab-pane" role="tabpanel" aria-labelledby="home-tab" tabindex="0">
        <br>
        <h2 class="title-font">{{ user?.username }}님이 좋아요 한 영화</h2>    
        <ul v-if="likeMovies" class="row popular-list">
          <MovieCardView
            v-for="movie in likeMovies"
            :key="movie.created_at"
            :movie="movie"
          />
        </ul>

      </div>
      <div class="tab-pane fade" id="profile-tab-pane" role="tabpanel" aria-labelledby="profile-tab" tabindex="0">        
        <br>
        <h2 class="title-font">{{ user?.username }}님이 리뷰한 영화</h2>    
        <ul v-if="reviewMovies" class="row popular-list">
          <MovieCardView
            v-for="movie in reviewMovies"
            :key="movie.created_at"
            :movie="movie"
          />
        </ul>

      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import MovieCardView from "@/components/MovieCardView"
import FollowersView from '@/components/FollowersView.vue'
import FollowingsView from '@/components/FollowingsView.vue'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: "MyProfile",
  data: function () {
    return {
      me: [],
      user: [],
      show1: false,
      show2: false,
      variants: ["light", "dark"],
      headerBgVariant: "dark",
      headerTextVariant: "white",
      bodyBgVariant: "dark",
      bodyTextVariant: "white",
      footerBgVariant: "danger",
      footerTextVariant: "dark",
      likeMovies: [],
      reviewMovies: [],
    }
  },
  created() {
    this.getMe()
  },
  components: {
    MovieCardView,
    FollowersView,
    FollowingsView,
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
          this.getMyName(res.data.pk)
        })
    },
    getMyName(my_pk) {
      axios({
        method: 'get',
        url: `${API_URL}/userinfo/user/${my_pk}/`,
      })
        .then(res => {
          this.user = res.data
          // console.log(res.data)
          this.getUserMovies(res.data.like_movies, res.data.reviews)
        })
    },
    getUserMovies(like_movies, reviews) {
      axios({
        method: 'post',
        url: `${API_URL}/movies/${this.user.id}/like/review/`,
        data: {
          like_movies,
          reviews,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
      })
        .then(res => {
          this.likeMovies = res.data[0]
          this.reviewMovies = res.data[1]
        })
    },
    open1: function () {
      this.show1 = true
    },
    open2: function () {
      this.show2 = true
    },
    close: function () {
      this.show1 = false
    },
    close2: function () {
      this.show2 = false
    },
  },
  computed: {
    followingsLength: function () {
      if (this.user.followings) {
        return this.user.followings.length
      } else {
        return 0
      }
    },
    followersLength: function () {
      if (this.user.followers) {
        return this.user.followers.length
      } else {
        return 0
      }
    },
  },
}
</script>

<style>
.containerSpecial{
  padding:1px;
  width:100%;
  margin:1px;
  text-align:center
}

@import url(http://fonts.googleapis.com/css?family=Lato:400,700);
.center {
    position: relative;
    top: 50px;
}
.profile 
{
min-height: 355px;
display: inline-block;
}
.divider 
{
border-top:1px solid rgba(0,0,0,0.1);
}
.follow-info:hover {
  cursor: pointer;
}
span.tags 
{
background: #404242;
border-radius: 2px;
color: #f5f5f5;
font-weight: bold;
padding: 4px 6px;
}
.my-profile {
  padding: 100px 0;
}
</style>