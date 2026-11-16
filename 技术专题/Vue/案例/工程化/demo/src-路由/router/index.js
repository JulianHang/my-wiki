// 导入所需模块
import Vue from 'vue'
import VueRouter from 'vue-router'


// 调用user函数，将VueRouter安装为vue插件
Vue.use(VueRouter)

import DisCover from '@/views/DisCover.vue'
import MyMusic from '@/views/MyMusic.vue'
import Follow from '@/views/Follow.vue'
import Recommend from '@/views/Recommend.vue'
import TopList from '@/views/TopList.vue'
import ArtList from '@/views/ArtList.vue'
import NotFound from '@/views/NotFound.vue'


// 配置路由规则
const  routes = [
    // 直接写到这个数组的路由规则，级别最大，叫做一级路由
    // 一级路由组件，只能写在APP.vue中
    {path: '/discover', component: DisCover, children: [
        // 二级路由的path，可以不写/
        // 二级路由的访问地址会和一级路由拼接，比如/discover/tuijian
        {path: '', redirect: 'tuijian'}, // 二级路由的默认路由
        {name: 'tj', path: 'tuijian', component: Recommend},
        // ?  -> 同一条路由同时匹配不带参数和带参数的路径
        {name: 'phb', path: 'toplist/:name?', component: TopList},
        {name: 'art', path: 'artlist', component: ArtList},
    ]},
    {path: '/mymusic', component: MyMusic},

    {path: '/follow', component: Follow},
    {path: '*', component: NotFound}
]

// 创建路由的实例对象
const router = new VueRouter({
    // 路由的配置
    routes,
    // mode: 'history'
    linkActiveClass: 'a',
    linkExactActiveClass: 'b'
})

// 导航守卫
// router.beforeEach((to, from, next) => {

// })

// 导出路由的实例对象
export default router