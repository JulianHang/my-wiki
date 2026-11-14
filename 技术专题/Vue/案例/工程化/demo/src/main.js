import Vue from 'vue'
import App from './App.vue'
// 导入路由模块，如果导入的是index.js，可以忽略不屑
import router from '@/router'

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  // 挂载路由模块
  router
}).$mount('#app')
