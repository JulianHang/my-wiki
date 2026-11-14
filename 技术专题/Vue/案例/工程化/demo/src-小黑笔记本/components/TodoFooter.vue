<template>

    <footer class="footer">
        <!-- 统计 -->
        <span class="todo-count">合 计:<strong> {{list.length}} </strong></span>
        <!-- 清空 -->
        <button class="clear-completed" @click="$emit('clear')">
            清空任务
        </button>
    </footer>

</template>

<script>
export default {
    props: ['list']
}
</script>

<style lang="scss" scoped></style>