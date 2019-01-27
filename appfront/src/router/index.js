import Vue from 'vue'
import Router from 'vue-router'
import login from '@/components/login'
import home from '@/components/home'
import Course_information from '@/components/Course_information'
import departments_informations from '@/components/departments_informations'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'login',
      component: login
    },
    {
      path: '/home',
      name: 'home',
      component: home
    },
    {
      path: '/Course_information',
      name: 'Course_information',
      component: Course_information
    },
    {
      path: '/departments_informations',
      name: 'departments_informations',
      component: departments_informations
    }
  ]
})
