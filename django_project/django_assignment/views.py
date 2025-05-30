from django.http import HttpResponse
from django.shortcuts import render
from students.models import Student
from django.http import JsonResponse
from django.core import serializers


def home(request):
    name = request.GET.get('user_name', 'New User')
    return render(request, 'base.html', {'user_name': name})


def getAllStudents(request):
    query = Student.objects.all()
    extra_details = list(query.values())
    return JsonResponse(extra_details, safe=False)

def getStudentIndex(request, id):
    object = Student.objects.filter(id=id)
    objectList = list(object.values())

    return JsonResponse(objectList, safe=False)
