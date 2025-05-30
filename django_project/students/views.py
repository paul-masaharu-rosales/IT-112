from django.shortcuts import render
from .models import Student
from django.http import JsonResponse

def getStudentByIndex(request):
    query = list(Student.objects.all().values())
    return JsonResponse(query)