<template>
  <div>
    <h2>App组件</h2>
    <p>这是App组件中的p标签</p>
    <hr />
    <MyTest></MyTest>
    <hr />
    <MyForm></MyForm>
    <button>重置</button>
  </div>
</template>

<script>
import MyTest from './components/MyTest.vue'
import MyForm from './components/MyForm.vue'
export default {
  data () {
    return {}
  },
  components: {
    MyTest,
    MyForm
  }
}
</script>

<style lang="less" scoped></style>
