<script setup>
import { ref } from 'vue'
import { computed } from 'vue'

const list = ref([1, 2, 3, 4, 5, 6, 7])

const computedList = computed(() => {
  return list.value.filter(item => item > 2)
})
</script>

<template>
  <div>原始响应数组{{ list }}</div>
  <div>计算属性数组 {{ computedList }}</div>
</template>
