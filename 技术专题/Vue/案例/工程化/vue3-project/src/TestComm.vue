<script setup>
import { ref } from 'vue'

const name = ref('test name')
const setName = () => {
  name.value = 'test new name'
}
// 暴露给父组件
defineExpose({ name, setName })
</script>

<template>
  <div>test组件</div>
</template>

<style lang="scss" scoped></style>
