from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import C, D, E, O, S, T


def index(request):
    student_list = S.objects.order_by('xh')
    template = loader.get_template('edu_manage/index.html')
    context = {
        'student_list': student_list,
    }
    return HttpResponse(template.render(context, request))
