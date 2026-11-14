<template>
  <div>
    <h3>Test组件需求：找到下面的p标签，设置样式</h3>
    <p ref="abc">这是Test组件中的p标签</p>
  </div>
</template>

<script>
export default {
  mounted() {
    // 1.如果组件中，多个元素有相同的ref值，this.$refs.xxx 只找最后一个
    // 2.如果是通过循环出来的，多个元素有相同的ref值，this.$refs.xxx 找到全部
    this.$refs.abc.style.color = 'blue'
  }
}
</script>

<style lang="less" scoped></style>
