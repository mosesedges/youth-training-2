import datetime
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse('Hello World My People')


def greet(request):
    now = datetime.datetime.now()
    return render(request, 'hello/greet.html', {
        'name': now.month == 6 and now.day == 28
    })
