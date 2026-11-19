<script setup>
const emit = defineEmits(['get-message'])
const sendMsg = () => {
  emit('get-message', 'this is son message')
}
</script>

<template>
  <div class="son">
    <h3>子组件son</h3>
    <button @click="sendMsg">触发自定义事件</button>
  </div>
</template>
