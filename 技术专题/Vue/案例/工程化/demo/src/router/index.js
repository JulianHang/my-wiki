// 导入所需模块
import Vue from 'vue'
import VueRouter from 'vue-router'


// 调用user函数，将VueRouter安装为vue插件
Vue.use(VueRouter)

import DisCover from '@/views/DisCover.vue'
import MyMusic from '@/views/MyMusic.vue'
import Follow from '@/views/Follow.vue'


// 配置路由规则
const  routes = [
    {path: '/discover', component: DisCover},
    {path: '/mymusic', component: MyMusic},
    {path: '/follow', component: Follow}
]

// 创建路由的实例对象
const router = new VueRouter({
    // 路由的配置
    routes
})

// 导出路由的实例对象
export default router