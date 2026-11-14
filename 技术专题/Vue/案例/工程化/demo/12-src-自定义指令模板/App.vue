<template>
  <div class="box">
    <h3>需求1：让输入框立即获取焦点</h3>
    <div class="focus">
      <input type="text" />
    </div>
    <h3>需求2：Ajax请求数据，并设计loading指令</h3>
    <ul>
      <li class="news">
        <div class="left">
          <div class="title">5G渗透率持续提升，创新业务快速成长</div>
          <div class="info">
            <span>新京报</span>
            <span>2222-10-28 11:50:28</span>
          </div>
        </div>
        <div class="right">
          <img src="http://ajax-api.itheima.net/images/0.webp" alt="" />
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
// 安装 axios =>  npm i axios 或者 yarn add axios
// 安装如果报错，则加 --legacy-peer-deps 选项
// 接口地址：http://hmajax.itheima.net/api/news
// 请求方式：get
// 请求参数：无
export default {}
</script>

<style>
.box {
  width: 800px;
  min-height: 500px;
  position: relative;
}
.focus,
ul {
  border: 3px solid orange;
  border-radius: 5px;
  padding: 10px;
  margin: 10px;
}
.news {
  display: flex;
  height: 120px;
  width: 600px;
  margin: 0 auto;
  padding: 20px 0;
  cursor: pointer;
}
.news .left {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding-right: 10px;
}
.news .left .title {
  font-size: 20px;
}
.news .left .info {
  color: #999999;
}
.news .left .info span {
  margin-right: 20px;
}
.news .right {
  width: 160px;
  height: 120px;
}
.news .right img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>
