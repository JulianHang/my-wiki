<template>
  <div>
    <Son  :visible="visible"  :list="list"  :say="say" :hi="hi"></Son>
  </div>
</template>

<script>
import Son from './components/Son.vue'
export default {
  data () {
    return {
      age: 20,
      visible: true,
      list: ['a', 'b'],
      user: {
        name: 'zs', sex: '男'
      },
      say() {
        console.log(123);
        
      },
      hi() {
        console.log(456);
        
      }
    }
  },
  components: {
    Son
  }
}
</script>

<style lang="less" scoped></style>
