<script setup>
// 1. 导入函数
import { reactive } from 'vue'
import { ref } from 'vue'

// 2. 执行函数 传入一个对象类型的参数
const state = reactive({
  count: 0
})

const setCount = () => {
  state.count++
}

const num = ref(0)
const setNum = () => {
  // 脚本区域修改ref产生的响应式对象数据 比图通过.value属性
  num.value++
}
</script>

<template>
  <div>
    <button @click="setCount">{{ state.count }}</button>
  </div>
  <div>
    <button @click="setNum">{{ num }}</button>
  </div>
</template>
