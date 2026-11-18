export default {
  namespaced: true, // 开启命名空间
  state: {
    sex: 23,
    uname: 'badWoman'
  },
  // mutations 是 vuex 中唯一可以修改 state 数据的方法
  // mutations,不支持异步更新,只能放同步代码
  mutations: {
    abc (state, n) {
      state.sex = n
    }
  },
  // actions 里面放异步方法
  actions: {
    newSex (store, n) {
      setTimeout(() => {
        store.commit('abc', n)
      }, 3000)
    }
  }
}
