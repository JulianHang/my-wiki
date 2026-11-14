<template>
  <div>
    <!-- 歌手列表 -->
    <h2>入驻歌手</h2>
    <div class="list">
      <div class="item" v-for="item in list" :key="item.id">
        <img :src="item.smallImg" />
        <p>
          <a href="javascript:;">
            {{ item.name }}
          </a>
        </p>
      </div>
    </div>
    <div class="conent">
      <img src="" alt="" />
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      list: [
        {
          id: 1,
          name: '张惠妹',
          smallImg: require('../assets/zhanghuimei-small.jpg'),
          bigImg: require('../assets/zhanghuimei-big.jpg')
        },
        {
          id: 2,
          name: '邓紫棋',
          smallImg: require('../assets/dengziqi-small.jpg'),
          bigImg: require('../assets/dengziqi-big.jpg')
        },
        {
          id: 3,
          name: '汪苏泷',
          smallImg: require('../assets/wangsulong-small.jpg'),
          bigImg: require('../assets/wangsulong-big.jpg')
        },
        {
          id: 4,
          name: '薛之谦',
          smallImg: require('../assets/xuezhiqian-small.jpg'),
          bigImg: require('../assets/xuezhiqian-big.jpg')
        }
      ]
      // current: {}
    }
  }
}
</script>

<style lang="less" scoped>
.list {
  width: 580px;
  display: flex;
  justify-content: space-between;

  .item {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  a {
    text-decoration: none;
    color: #424242;
  }
}
</style>
