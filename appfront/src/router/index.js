import Vue from 'vue'
import Router from 'vue-router'
import IndexMain from '@/components/IndexMain'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/IndexMain',
      name: 'IndexMain',
      component: IndexMain
    }
  ]
})
