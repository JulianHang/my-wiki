<template>
  <div>
    <p>{{ age }}</p>
  </div>
</template>

<script>
export default {
  name: 'SonPage',
  created() {
    this.say()
  },

  // props: ['age', 'visible', 'list', 'user', 'say', 'hi']
  // props 写成对象格式可以对接收的变量进行校验
  // 1. required: true  表示父组件必须传递这个值
  // 2. type: String | Number | Function
  //  2.1 type: [String, Number]
  // 3. default: ''
  //  3.1 默认值如果是对象或数组，要写成函数格式，函数中返回对象或数组
  props: {
    // 
    age: {
      default: 100,
      type: Number
    },
    visible: {},
    list: {},
    user: {
      default: () => {
        return {}
      }

    },
    say:{},
    hi: {}
  }
}
</script>

<style lang="less" scoped></style>
