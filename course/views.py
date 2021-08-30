from django.shortcuts import render
from django.http import HttpResponse
from . models import course , contact
# Create your views here.


def Index(request):
    
    return render(request,"course\home.html")


def List(request):
    # Courses = course.objects.all()
    AllCat = course.objects.values("category") 
    cats = {var["category"] for var in AllCat }
    # for var in AllCat:
    #     cats.append(var["category"])
    # cats = set(cats)    
    Courses = {}
    for val in cats:
        Courses[val] = course.objects.filter(category=val)
    params = {
        "data": Courses
    }
    
    return render(request,"course\index.html",params)


def Detail(request,id):
    # name = request.GET.get("id")

    try:
        params = {"data":course.objects.get(id=id),"error":"null"}
    except:
        params = {"data":{},"error":"Course not found"}

    return render(request,"course\singlecourse.html", params)


def contactUs(request):
    return render(request,"course\contactus.html")


def contactSubmit(request):
    email = request.POST.get("email")
    name = request.POST.get("name")
    tel = request.POST.get("phone")
    desc = request.POST.get("desc")
    File =request.POST.get("screenshot")

    newContact  =  contact(email=email ,name=name , desc=desc , phone=tel ,screenshot=File)
    newContact.save()

    return HttpResponse("Thank you")
