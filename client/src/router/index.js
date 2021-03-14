import { createRouter, createWebHistory } from 'vue-router'
import store from '../store'
import Home from '../views/Home.vue'
import Disciplines from '../views/Disciplines.vue'
import Login from '../views/Login.vue'
import Options from '../views/Options.vue'
import DisciplineForms from '../views/DisciplineForms.vue'

const isAuthenticated = (to, from, next) => {
    if (store.getters['auth/isAuthenticated'] == 'undefined') {
      next('/login')
    }
    else {
      store.dispatch('auth/TOKEN_VERIFY')
      .then(function(value) {
          next();
      },
      function(reason) {
          store.dispatch('auth/TOKEN_REFRESH')
          .then(function() {
              next();
          },
          function(reason) {
              next('/login')
          })
      });
    }
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
        component: Disciplines
    },
    {
        path: '/login',
        name: 'Login',
        component: Login
    },
    {
        path: '/disciplines/:discipline',
        name: 'discipline',
        component: DisciplineForms
    },
    {
        path: '/options',
        name: 'Options',
        component: Options,
        beforeEnter: isAuthenticated,
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router
