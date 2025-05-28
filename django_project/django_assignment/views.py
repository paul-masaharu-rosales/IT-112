from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    name = request.GET.get('user_name', 'New User')
    return render(request, 'base.html', {'user_name': name})
