<template>
  <div>
    <h2>随便一个组件-2</h2>
    <!-- <P>{{ sex }}</P> -->
    <P>{{ nianLing }}</P>
    <P>{{ uname }}</P>
    <button @click="abc(100)">更新年龄</button>
    <br />
    <button @click="newSex(200)">三秒后更新年龄</button>
  </div>
</template>

<script>
import { mapState, mapMutations, mapActions } from 'vuex'
export default {
  // data () {
  //   return {
  //     sex: 1777
  //   }
  // },
  computed: {
    // ...mapState(['sex', 'uname', 'list']),
    ...mapState('user', { nianLing: 'sex', uname: 'uname' }),
    ...mapState('todo', { list: 'uname' })
  },
  methods: {
    ...mapMutations(['abc']),
    ...mapActions(['newSex'])
  }
}
</script>

<style lang="less" scoped></style>
