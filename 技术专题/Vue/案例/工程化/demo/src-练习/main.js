import Vue from 'vue' // 导入Vue
import App from './App.vue' // 导入根组件

Vue.config.productionTip = false // 关闭温馨提示

// 全局注册组件（注册后，可以在任意组件中使用）
// 1.导入
import HmButton from './components/HmButton.vue'
// 2.全局注册组件
Vue.component('HmButton', HmButton)

// 实例化vue，并将App页面渲染后的结果挂载到app下（publish/index.html)
new Vue({
  // el: "app"  el等价于 .$mount("#app")
  render: h => h(App),
}).$mount('#app')
