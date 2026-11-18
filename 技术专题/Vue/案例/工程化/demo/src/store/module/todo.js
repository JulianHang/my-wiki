export default {
  namespaced: true, // 开启命名空间
  state: {
    list: [
      { id: 1, name: '吃饭', isDone: true },
      { id: 2, name: '睡觉', isDone: false },
      { id: 3, name: '听歌', isDone: true }
    ]
  },
  // mutations 是 vuex 中唯一可以修改 state 数据的方法
  // mutations,不支持异步更新,只能放同步代码
  mutations: {
    abc (state, n) {
      state.list = n
    }
  },
  // actions 里面放异步方法
  actions: {
    newSex (store, n) {
      setTimeout(() => {
        store.commit('abc', n)
      }, 3000)
    }
  },
  // getters 是vuex中的计算属性(和组件中的计算属性意义一样,但是不支持set修改)
  // 为了方便获取state中的数据;插件作者会给每个计算属性方法,传递一个 state 参数
  getters: {
    all (state) {
      return state.list.every(item => item.isDone === true)
    }
  }
}
