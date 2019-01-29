from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url('login/', views.login, name='login'),
    url('course_info/', views.course_info, name='course_info'),
    url('departments_info/', views.departments_info, name='departments_info'),
    url('my_courses/', views.my_courses, name='my_courses'),
    url('open_schedule/', views.open_schedule, name='open_schedule'),
    url('my_schedule/', views.my_schedule, name='my_schedule'),
    url('add_course/', views.add_course, name='add_course'),
    url('del_course/', views.del_course, name='del_course')
]
