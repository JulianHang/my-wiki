<script setup>
import { provide, ref } from 'vue'
import RoomMsgItem from './room-msg-item.vue'

const count = ref(100)
const setCount = () => {
  count.value++
}

// 1. 顶层组件提供数据
provide('data-key', 'this is room data')
provide('count-key', count)
provide('setCount-key', setCount)

setTimeout(() => {
  count.value = 100
}, 3000)
</script>

<template>
  <div>
    顶层组件
    <RoomMsgItem></RoomMsgItem>
  </div>
</template>

<style lang="scss" scoped></style>
