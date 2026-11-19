<script setup>
import { onMounted, ref } from 'vue'
import TestComm from './TestComm.vue'

const h1Ref = ref(null)
const commRef = ref(null)

onMounted(() => {
  console.log(h1Ref.value)
  console.log(commRef.value)
})
</script>

<template>
  <h1 ref="h1Ref"></h1>
  <TestComm ref="commRef"></TestComm>
</template>
