import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/Home'
import Classificados from '@/components/Classificados'
import Buscas from '@/components/Buscas'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: HelloWorld
    },
    {
      path: '/classificados',
      name: 'Classificados',
      component: Classificados
    },
    {
      path: '/buscas',
      name: 'Buscas',
      component: Buscas
    }
  ]
})
