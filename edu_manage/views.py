from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from .models import C, D, E, O, S, T


def login(request):
    name = request.GET['name']
    psw = request.GET['psw']
    stu = S.objects.filter(xh=name, psw=psw)
    if stu:
        response = JsonResponse({"info": "yes"})
    else:
        response = JsonResponse({"info": "no"})
    return response
