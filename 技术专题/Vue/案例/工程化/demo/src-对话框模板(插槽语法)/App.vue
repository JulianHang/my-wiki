<template>
  <div>
    <MyDialog>
      <!-- 可以简写 -->
      <template v-slot:title>
          <h3>温馨提示</h3>
      </template>

      <template #default="obj">
        <p>你确定要删除啊？{{ obj.username }}</p>
      </template>

    </MyDialog>
  </div>
</template>

<script>
import MyDialog from './components/MyDialog.vue'
export default {
  data () {
    return {

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