from django.shortcuts import render
from django.http import HttpResponse
from . models import course
# Create your views here.


def Index(request):
    
    return render(request,"course\home.html")


def List(request):
    Courses = course.objects.all()
    params = {
        "data": Courses
    }
    return render(request,"course\index.html",params)

