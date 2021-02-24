import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import store from '../store'

const isAuthenticated = (to, from, next) => {
  if (store.getters['auth/isAuthenticated']) {
    next()
    return
  }
  next('/login')
}

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/disciplines',
    name: 'Disciplines',
    component: () => import('../views/Disciplines.vue')
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue')
  },
  {
    path: '/disciplines/:discipline',
    name: 'discipline',
    component: () => import('../views/DisciplineForms.vue')
  },
  // {
  //   path: '/disciplines/:discipline/:form_id',
  //   name: 'form',
  //   component: () => import('../views/Form.vue'),
  //   beforeEnter: isAuthenticated,
  // },
  {
    path: '/options',
    name: 'Options',
    component: () => import('../views/Options.vue'),
    beforeEnter: isAuthenticated,
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
