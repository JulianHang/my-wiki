// createApp 创建一个应用实例对象 new vue()
import { createApp } from 'vue'
import App from './App.vue'
// 1. 以APP作为参数生成一个Vue实例对象
// 2. 挂载到id为app的节点上
createApp(App).mount('#app')
