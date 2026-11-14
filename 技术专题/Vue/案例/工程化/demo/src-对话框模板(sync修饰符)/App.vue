<template>
  <div>
    <button @click="visible = true">删除</button>
    <MyDialog :visible.sync="visible"></MyDialog>
    <!-- 
      :属性.sync="变量"
      等同于 :属性="变量"  + @update:属性="xx"
    -->
  </div>
</template>

<script>
import MyDialog from './components/MyDialog.vue'
export default {
  data () {
    return {
      visible: false
    }
  },
  components: {
    MyDialog
  }
}
</script>

<style>
body {
  background-color: #b3b3b3;
}
</style>