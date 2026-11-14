<template>

    <header class="header">
        <h1>小黑记事本</h1>
        <input placeholder="请输入任务" class="new-todo" v-model="name"/>
        <button class="add" @click="post">添加任务</button>
    </header>

</template>

<script>
export default {
    data() {
        return {
            name: ''
        }
    },
    methods: {
        post() {
            // $emit写到JS区, 要用this.$emit
            this.$emit('add', this.name)
            this.name = ''
        }
    }

}
</script>

<style lang="scss" scoped></style>