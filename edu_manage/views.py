from django.http import HttpResponse, JsonResponse
import json
from django.forms.models import model_to_dict
from .models import C, D, E, O, S, T


def login(request):
    name = request.GET['name']
    psw = request.GET['psw']
    stu = S.objects.filter(xh=name, psw=psw)
    if stu:
        response = JsonResponse({"info": "yes", "name": stu[0].xm, "TeacherorStudent": "0"})
    else:
        teacher = T.objects.filter(gh=name, psw=psw)
        if teacher:
            response = JsonResponse({"info": "yes", "name": teacher[0].xm, "TeacherorStudent": "1"})
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
    my_courses = E.objects.filter(xh=xh)
    for my_course in my_courses:
        if my_course.xq != '2018-2019春季':
            response.append(
                {'xh': my_course.xh, 'kh': my_course.kh, 'km': my_course.course.km, 'pscj': my_course.pscj,
                 'kscj': my_course.kscj, 'zpcj': my_course.zpcj,
                 'xq': my_course.xq, 'jsm': my_course.teacher.xm})
    return JsonResponse(response, safe=False)


def open_schedule(request):
    response = []
    open_schedules = O.objects.all()
    for open_schedule in open_schedules:
        response.append(
            {'kh': open_schedule.kh, 'km': open_schedule.course.km, 'gh': open_schedule.gh, 'sksj': open_schedule.sksj,
             'xf': open_schedule.course.xf, 'xs': open_schedule.course.xs, 'jsm': open_schedule.teacher.xm})

    return JsonResponse(response, safe=False)


def my_schedule(request):
    xh = request.GET['xh']
    response = []
    my_schedules = E.objects.filter(xh=xh)

    for my_schedule in my_schedules:
        if my_schedule.xq == '2018-2019春季':
            sksj = O.objects.filter(kh=my_schedule.kh, gh=my_schedule.gh)[0].sksj
            response.append(
                {'kh': my_schedule.kh, 'km': my_schedule.course.km,
                 'sksj': sksj,
                 'xf': my_schedule.course.xf, 'xs': my_schedule.course.xs, 'jsm': my_schedule.teacher.xm})

    return JsonResponse(response, safe=False)


def add_course(request):
    kh = request.GET['kh']
    gh = request.GET['gh']
    xh = request.GET['xh']
    c_id = C.objects.filter(kh=kh)[0].id
    t_id = T.objects.filter(gh=gh)[0].id
    courses = O.objects.filter(kh=kh, gh=gh)
    for course in courses:
        e = E(xh=xh, xq='2018-2019春季', kh=course.kh, gh=gh, course_id=c_id, teacher_id=t_id)
        e.save()

    return JsonResponse({"res": 'OK'})


def del_course(request):
    kh = request.GET['kh']
    jsm = request.GET['jsm']
    gh = T.objects.filter(xm=jsm)[0].gh
    courses = E.objects.filter(kh=kh, gh=gh)
    courses.delete()
    return JsonResponse({"res": 'OK'})


def stu_information(request):
    xh = request.GET['xh']
    response = []
    infos_stu = S.objects.filter(xh=xh)
    for info_stu in infos_stu:
        response.append(model_to_dict(info_stu))
    return JsonResponse(response, safe=False)


def find_course_teacher(request):
    gh = request.GET['gh']
    courses = O.objects.filter(gh=gh)
    response = []
    for course in courses:
        response.append(
            {'kh': course.kh, 'km': course.course.km})
    return JsonResponse(response, safe=False)


def find_student_course(request):
    kh = request.GET['kh']
    gh = request.GET['gh']
    student_ids = E.objects.filter(kh=kh, xq='2018-2019春季', gh=gh)
    response = []
    for student_id in student_ids:
        print(student_id.xh)
        student_name = S.objects.filter(xh=student_id.xh)
        response.append(
            {'xh': student_id.xh, 'xm': student_name[0].xm, 'pscj': student_id.pscj, 'kscj': student_id.kscj,
             'zpcj': student_id.zpcj})

    return JsonResponse(response, safe=False)


def input_geade(request):
    xh = request.GET['xh']
    kh = request.GET['kh']
    gh = request.GET['gh']
    pscj = request.GET['pscj']
    kscj = request.GET['kscj']
    zpcj = str(int(float(request.GET['zpcj'])))
    if pscj!='' and kscj!='' and  zpcj!='':
        E.objects.filter(xh=xh, kh=kh, gh=gh).update(pscj=pscj, kscj=kscj, zpcj=zpcj)
        return JsonResponse({"res": 'OK'})
    else:
        return JsonResponse({"res": 'NO'})


def find_grade(request):
    kh = request.GET['kh']
    gh = request.GET['gh']
    student_ids = E.objects.filter(kh=kh, xq='2018-2019春季', gh=gh)
    response = []
    for student_id in student_ids:
        print(student_id.xh)
        zpcj = student_id.zpcj
        if zpcj == None:
            zpcj = "-1"
        response.append({'zpcj': zpcj})
    return JsonResponse(response, safe=False)

