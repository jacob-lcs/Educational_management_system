from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from django.forms.models import model_to_dict
from .models import C, D, E, O, S, T


def login(request):
    name = request.GET['name']
    psw = request.GET['psw']
    stu = S.objects.filter(xh=name, psw=psw)
    if stu:
        response = JsonResponse({"info": "yes", "name": stu[0].xm})
    else:
        response = JsonResponse({"info": "no"})
    return response


def course_info(request):
    response = []
    courses = C.objects.all()
    for course in courses:
        response.append(model_to_dict(course))
    return HttpResponse(json.dumps(response), content_type="application/json")


def departments_info(request):
    response = []
    departments = D.objects.all()
    for department in departments:
        response.append(model_to_dict(department))
    return HttpResponse(json.dumps(response), content_type="application/json")


def my_courses(request):
    xh = request.GET['xh']
    response = []
    # res = {'xh': '', 'kh': '', 'km': '', 'pscj': '', 'kscj': '', 'zpcj': '', 'xq': '', 'jsm': ''}
    my_courses = E.objects.filter(xh=xh)
    for my_course in my_courses:
        # res['xh'] = my_course.xh
        # res['kh'] = my_course.kh
        # res['km'] = my_course.course.km
        # res['pscj'] = my_course.pscj
        # res['kscj'] = my_course.kscj
        # res['zpcj'] = my_course.zpcj
        # res['xq'] = my_course.xq
        # res['jsm'] = my_course.teacher.xm
        response.append(
            {'xh': my_course.xh, 'kh': my_course.kh, 'km': my_course.course.km, 'pscj': my_course.pscj, 'kscj': my_course.kscj, 'zpcj': my_course.zpcj,
             'xq': my_course.xq, 'jsm': my_course.teacher.xm})
    return JsonResponse(response, safe=False)
