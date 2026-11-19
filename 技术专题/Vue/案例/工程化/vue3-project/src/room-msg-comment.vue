<script setup>
import { inject } from 'vue'

// 接收数据
const roomData = inject('data-key')
const countData = inject('count-key')
const setCount = inject('setCount-key')
</script>

<template>
  <div>
    底层组件
    <div>来自顶层组件中的数据为：{{ roomData }}</div>
    <div>来自顶层组件的响应式数据为：{{ countData }}</div>
  </div>
</template>

<style lang="scss" scoped></style>
