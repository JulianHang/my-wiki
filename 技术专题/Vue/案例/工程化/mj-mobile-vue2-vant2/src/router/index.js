import Article from '@/views/Article.vue'
import Collect from '@/views/Collect.vue'
import Like from '@/views/Like.vue'
import User from '@/views/User.vue'
import Detail from '@/views/Detail.vue'
import Home from '@/views/Home.vue'
import Login from '@/views/Login.vue'
import Register from '@/views/Register.vue'
import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/register',
    name: 'register',
    component: Register
  },
  {
    path: '/detail',
    name: 'detail',
    component: Detail
  },
  {
    path: '/',
    name: '',
    component: Home,
    redirect: '/article',
    children: [
      {
        path: 'article',
        component: Article
      },
      {
        path: 'collect',
        component: Collect
      },
      {
        path: 'like',
        component: Like
      },
      {
        path: 'user',
        component: User
      }
    ]
  }
]

const router = new VueRouter({
  routes
})

export default router
