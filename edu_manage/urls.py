from django.urls import path
from django.conf.urls import url


from . import views

urlpatterns = [
    url('login/', views.login, name='login'),
    url('course_info/', views.course_info, name='course_info')
]
