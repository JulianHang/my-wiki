<template>
  <div>
    <h2>随便一个组件-1</h2>
    <p>{{ $store.state.uname }}</p>
    <p>{{ $store.state.sex }}</p>
    <p>{{ $store.getters.ccc }}</p>
    <p>{{ $store.getters.all }}</p>
    <button @click="$store.commit('abc', 5000)">更新sex</button>
    <br />
    <button @click="$store.dispatch('newSex', 20)">3s后更新sex</button>
  </div>
</template>

<script>
export default {}
</script>

<style lang="less" scoped></style>
