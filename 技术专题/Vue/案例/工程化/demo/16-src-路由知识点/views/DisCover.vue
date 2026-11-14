<template>
  <div class="box">
    <!-- 发现音乐 -->
    <div class="link">
      <a href="#">推荐</a>
      <a href="#">排行榜</a>
      <a href="#">歌手</a>
    </div>
    <div class="content">

    </div>
  </div>
</template>

<script>
export default {
  name: 'FoundMusic'
}
</script>

<style lang="less" scoped>
.box {
  padding: 15px;
}

.link {
  a {
    padding-right: 10px;
    text-decoration: none;
    color: #424242;
  }
}

.content {
  padding: 10px;
}
</style>
