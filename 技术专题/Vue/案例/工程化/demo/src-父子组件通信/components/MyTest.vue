<template>
    <div>
        <h2>商品名称：{{obj.name}}</h2>
        <p>商品单价：{{obj.price}}</p>
        <p>商品描述信息：{{obj.info}}</p>
        <button @click="$emit('kanyidao', obj.id)">砍一刀</button>
    </div>
</template>

<script>
export default {
    props: ['obj'],
    
}
</script>

<style lang="scss" scoped>

</style>