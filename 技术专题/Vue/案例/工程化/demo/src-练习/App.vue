<template>
  <div class = "app">
    <HmHeader></HmHeader>
    <HmMain/>
    <hm-footer/>

    
  </div>
</template>

<script>
/**
 * 1. 导入
 * 2. 注册组件-注册成html标签（这样标签就代表组件了）
 * 3. 页面中使用 <HmHeader></HmHeader>
 */
import HmHeader from './components/HmHeader.vue'
import HmMain from './components/HmMain.vue'
import HmFooter from './components/HmFooter.vue'

export default {
  
  // 注册组件
  components: {
    // 标签名: 导入的变量名
    HmHeader: HmHeader,
    HmMain: HmMain,
    HmFooter: HmFooter

  }
}
</script>

<style lang="less" scoped>
.app {
  padding: 10px;
  background-color: #87cccb;
}
</style>