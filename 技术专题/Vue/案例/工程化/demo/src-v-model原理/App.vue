<template>
  <div>
    <h3>需求1：不用v-model实现双向绑定</h3>
    <input type="text" :value="uname" @input="changeValue"/>
    <hr />

    <h3>需求2：实现输入框组件的v-model</h3>
    <!-- 子组件需要接收value属性，并触发input事件 -->
    <!-- <MyInput :value="age" @a="changeAge"></MyInput> -->
    <MyInput v-model="age"></MyInput>
    <hr />

    <h3>需求3：实现下拉框组件的v-model</h3>
    <MySelect></MySelect>
  </div>
</template>

<script>
import MyInput from './components/MyInput.vue'
import MySelect from './components/MySelect.vue'
export default {
  data () {
    return {
      uname: "s",
      age: 20
    }
  },
  components: {
    MyInput,
    MySelect
  },
  methods: {
    changeValue(e) {
      this.uname = e.target.value
    },
    changeAge(age) {
      this.age = age
    }
  }
}
</script>

<style lang="less" scoped></style>
