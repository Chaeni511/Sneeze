<template>
  <div>
    <CommunityCommentItem
    />
  </div>
</template>

<script>
import CommunityCommentItem from '@/components/community/CommunityCommentItem'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommunityComment',
  components: {
    CommunityCommentItem,
  },
  data() {
    return {
      comments: null,
      communityId: this.$route.params.community_pk
    }
  },
  methods: {
    getCommunityComment() {
      axios({
        method: 'get',
        url: `${API_URL}/community/comments/${this.communityId}`
      })
        .then(res => {
          // console.log(res)
          this.comments = res.data
        })
    }
  }
}
</script>

<style>

</style>