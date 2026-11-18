import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

// 导入所有组件
// 与按需导入方式相比，只能选其中一个，不能混着导入
import Vant from 'vant'
import 'vant/lib/index.css'
Vue.use(Vant)

// 按需导入组件
// import { Tabbar, TabbarItem, Toast } from 'vant'

// Vue.use(Tabbar)
// Vue.use(TabbarItem)
// Vue.use(Toast)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
