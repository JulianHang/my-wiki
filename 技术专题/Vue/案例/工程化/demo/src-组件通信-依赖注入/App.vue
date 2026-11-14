<template>
  <div>
    <Son></Son>
  </div>
</template>

<script>
import Son from './components/Son.vue'
export default {
  data () {
    return {
    
    }
  },
  provide: {
    user: {name: '2', age: 20}
  },
  components: {
    Son
  }
}
</script>

<style lang="less" scoped></style>
