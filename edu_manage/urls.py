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
    url('del_course/', views.del_course, name='del_course'),
    url('stu_information/', views.stu_information, name='stu_information'),
    url('find_course_teacher/', views.find_course_teacher, name='find_course_teacher'),
    url('find_student_course/', views.find_student_course, name='find_student_course')
]
