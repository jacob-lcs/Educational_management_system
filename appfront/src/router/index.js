import Vue from 'vue'
import Router from 'vue-router'
import login from '@/components/login'
import home from '@/components/home'
import Course_information from '@/components/Course_information'
import departments_informations from '@/components/departments_informations'
import my_courses from '@/components/my_courses'
import select_courses from  '@/components/select_courses'
import my_schedule from '@/components/my_schedule'
import stu_information from '@/components/stu_information'

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
    },
    {
      path: '/my_courses',
      name: 'my_courses',
      component: my_courses
    },
    {
      path: '/select_courses',
      name: 'select_courses',
      component: select_courses
    },
    {
      path: '/my_schedule',
      name: 'my_schedule',
      component: my_schedule
    },
    {
      path: '/stu_information',
      name: '/stu_information',
      component: stu_information
    }
  ]
})
