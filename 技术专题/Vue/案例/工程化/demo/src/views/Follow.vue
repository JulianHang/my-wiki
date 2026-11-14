<template>
  <div>
    <h3>关注的榜单</h3>
    <a href="javascript:;">新歌榜</a>
    <a href="javascript:;">热歌榜</a>
    <h3>关注的歌手</h3>
    <a href="javascript:;">张惠妹</a>
    <a href="javascript:;">薛之谦</a>
  </div>
</template>

<script>
export default {
  name: 'FollowPage',
}
</script>

<style lang="less" scoped>
div {
  padding: 15px;
}

h3 {
  margin: 0;
}

a {
  display: inline-block;
  margin: 10px;
  text-decoration: none;
  color: #424242;
}
</style>
