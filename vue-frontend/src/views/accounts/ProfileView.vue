<template>
  <div class="container">
    <div class="container" style="margin-bottom:30px">
      <div class="row">
          <div class="well profile">
            <div class="row">
              <div class="col-sm-3 col-12">
                <img src="@/assets/user.png" alt="profile" style="width:150px;">
              </div>
              <div class="col-sm-9 col-12">
                <div class="col-12 d-flex justify-content-around">
                  <h2 class="title-font" style="margin-bottom: 30px">{{ user.username }}님의 프로필</h2>
                </div>
                <div class="col-sm-12 divider text-center row d-flex justify-content-around">
                  <div class="col-sm-3 col-12 follow-info" @click="open1">
                    <h2><strong>{{followersLength}}</strong></h2>                    
                    <p><small>팔로워</small></p>
                  </div>
                  <div class="col-sm-3 col-12 follow-info"  @click="open2">
                    <h2><strong>{{followingsLength}}</strong></h2>                    
                    <p><small>팔로잉</small></p>
                  </div>
                  <div class="col-sm-4 col-12">
                    <h2><strong v-if="user.followings">{{ user.like_movies.length }}</strong></h2>                    
                    <p><small>좋아요한 영화 수</small></p>
                  </div>
              </div>
            </div>
            <div class="row ms-4 py-4">
              <div v-if="isFollowing" class="">{{ user.username }}님을 팔로우 중 입니다.</div>
              <div v-else><br></div>
            </div>    
            <div class="row mx-2">
              <div v-if="isLogin">
                <div v-if="me.username === user.username">
                  <!-- <br> -->
                </div>
                <div class="py-2" v-else>
                  <div class="d-grid gap-2 col-12 mx-auto">
                    <button v-if="isFollowing" @click="follow" class="btn btn-secondary">언팔로우</button>
                    <button v-else @click="follow" class="btn btn-primary">팔로우</button>
                  </div>
                </div>
              </div>
              <!-- <div v-else> </div> -->
            </div>        
          </div>
        </div>                 
      </div>
    </div>
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
            <div v-for="(userId, idx) in user.followings" :key="idx" style="cursor:pointer" class="content-font form-group floating-label-form-group controls mb-0 pb-2">
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
            <div v-for="(userId, idx) in user.followers" :key="idx" style="cursor:pointer" class="content-font form-group floating-label-form-group controls mb-0 pb-2">
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
        <h2 class="title-font">{{ user.username }}님이 좋아요 한 영화</h2>    
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
        <h2 class="title-font">{{ user.username }}님이 리뷰한 영화</h2>    
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
import FollowingsView from '@/components/FollowingsView.vue'
import FollowersView from '@/components/FollowersView.vue'


const API_URL = 'http://127.0.0.1:8000'

export default {
  name: "ProfileView",

  components: {
    MovieCardView,
    FollowingsView,
    FollowersView,
  },
  data() {
    return {
      me: [],
      user: [],
      likeMovies: [],
      reviewMovies: [],
      user_pk: this.$route.params.user_pk,
      movies: this.$store.state.movies,
      isFollowing: false,
      isLogin: this.$store.getters.isLogin,

      show1: false,
      show2: false,
      variants: ["light", "dark"],
      headerBgVariant: "dark",
      headerTextVariant: "white",
      bodyBgVariant: "dark",
      bodyTextVariant: "white",
      footerBgVariant: "danger",
      footerTextVariant: "dark",
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
          this.getMyName()
        })
    },
    getMyName() {
      axios({
        method: 'get',
        url: `${API_URL}/userinfo/user/${this.user_pk}/`,
      })
        .then(res => {
          this.user = res.data
          this.isFollow()
          this.getUserMovies(res.data.like_movies, res.data.reviews)
        })
        .catch(err => { console.log(err) })
    },
    getUserMovies(like_movies, reviews) {
      
      axios({
        method: 'post',
        url: `${API_URL}/movies/${this.user_pk}/like/review/`,
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
    follow() {
      axios({
        method: 'post',
        url: `${API_URL}/userinfo/follow/${this.me.pk}/${this.user_pk}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
      })
        .then((res) => {
          this.isFollowing = res.data
          this.getMyName()
        })
    },
    isFollow() {
      if (this.isLogin === false) {
        return
      } else if (this.me.username === this.user.username) {
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/userinfo/is_follow/${this.me.pk}/${this.user_pk}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
      })
        .then((res) => {
          this.isFollowing = res.data
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
    // isFollowing: function () {
    //   return this.following
    // },
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
.emphasis 
{
border-top: 4px solid transparent;
}
.emphasis:hover 
{
border-top: 4px solid #1abc9c;
}
.emphasis h2
{
margin-bottom:0;
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

</style>







