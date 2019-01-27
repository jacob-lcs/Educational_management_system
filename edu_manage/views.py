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
    courses = C.objects.filter(kaike=True)
    for course in courses:
        response.append(model_to_dict(course))
    return HttpResponse(json.dumps(response), content_type="application/json")


def departments_info(request):
    response = []
    departments = D.objects.all()
    for department in departments:
        response.append(model_to_dict(department))
    return HttpResponse(json.dumps(response), content_type="application/json")
