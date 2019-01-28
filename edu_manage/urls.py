from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url('login/', views.login, name='login'),
    url('course_info/', views.course_info, name='course_info'),
    url('departments_info/', views.departments_info, name='departments_info'),
    url('my_courses/', views.my_courses, name='my_courses')
]
