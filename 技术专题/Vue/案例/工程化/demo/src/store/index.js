// 1. 导入所需的包
import Vue from 'vue'
import Vuex from 'vuex'
import user from './module/user'
import todo from './module/todo'

// 2. 将Vuex注册为Vue的插件
Vue.use(Vuex)

// 3. 创建 store 实例对象
const store = new Vuex.Store({
  /* 这里配置Vuex */
  strict: true, //开启严格模式,防止小白在组件中直接修改state数据
  // 注册为模块
  modules: {
    user: user,
    todo: todo
  }
})

// 4. 导出 store 对象
export default store
