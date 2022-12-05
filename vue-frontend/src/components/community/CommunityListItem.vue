<template>
  <div>
    <div class="row d-flex justify-content-around">
      <!-- {{ community.content }} -->
      <div class="col-3 ">
        <p 
          class="m-0 fw-bold fs-5 user"
          @click="goDetail"
        >{{ community.title }}</p>
        
      </div>
      <div class="col-2 text-center">
        <p 
          class="m-0 fw-bold fs-5 user"
          @click="goProfile"
          >{{ community.userName }}</p>
      </div>
      <div class="col-2 text-center">
        {{ community?.created_at }}
      </div>
    </div>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'CommunityListItem',
  props: {
    community: Object,
  },
  methods: {
    goProfile() {
      this.$router.push({ name: 'Profile', params: { user_pk: this.community.user }})
    },
    goDetail() {
      this.$router.push({ name: 'CommunityDetail', params: { community_pk: this.community.id } })
    },
  }
}
</script>

<style>
</style>