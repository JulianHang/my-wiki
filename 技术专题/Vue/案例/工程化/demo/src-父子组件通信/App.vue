<template>
  <div class="App">
    <!-- 
      父传子 
    -->

    <my-test v-for="item in goodsList" :key="item.id" :obj="item" @kanyidao="changprice"></my-test>
    
    

    
  </div>
</template>

<script>
import MyTest from './components/MyTest.vue';

export default {
  data() {
    return {
      goodsList: [
        {id: 1, name: '方便面', price: 2.5, info: 'x'},
        {id: 2, name: '火腿肠', price: 2.5, info: 'x'},
        {id: 3, name: '卤蛋', price: 2.5, info: 'x'}
      ]
    }
  },
  components: {
      MyTest: MyTest

  },
  methods: {
    changprice(id) {
      this.goodsList.find()
      
    }
  }
}
</script>

<style></style>
