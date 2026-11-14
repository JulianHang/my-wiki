<template>
  <!-- 主体区域 -->
  <section id="app">
    <!-- 输入框 -->
    <todo-header @add="add"></todo-header>

    <!-- 列表区域 -->
    <todo-main :list="list" @del="del"></todo-main>
    
    <!-- 统计和清空 -->
    <todo-footer :list="list" @clear="clear"></todo-footer>
  </section>
</template>

<script>
import TodoHeader from './components/TodoHeader.vue';
import TodoMain from './components/TodoMain.vue';
import TodoFooter from './components/TodoFooter.vue';

export default {
  data () {
    return  {
      list: JSON.parse(localStorage.getItem('todolist')) || [
        {id: 1, name: '吃饭'},
        {id: 3, name: '自习'},
        {id: 4, name: '睡觉'},
      ]
    }
  },
  components: {
    TodoHeader: TodoHeader,
    TodoMain: TodoMain,
    TodoFooter: TodoFooter
  },
  methods: {
    del(id) {
      this.list = this.list.filter(item => id !== item.id)
    
    },
    add(name) {
      this.list.unshift({
        id: Date.now(),
        name: name
      })
    },
    clear() {
      this.list = []
    }
  },
  watch: {
    // list (val) {
    //   localStorage.setItem('todolist', JSON.stringify(val))
    // }
    list: {
      handler(val) {
        localStorage.setItem('todolist', JSON.stringify(val))
      },
      deep: true
    }
  }
}
</script>

<style>

</style>
