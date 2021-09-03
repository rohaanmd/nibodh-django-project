from django.shortcuts import render
from django.http import HttpResponse
from . models import course , contact , order
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
# Create your views here.
import json

def Index(request):
    
    return render(request,"course\home.html")


def List(request):
    # Courses = course.objects.all()
    AllCat = course.objects.values("category") 
    cats = {var["category"] for var in AllCat }
    # for var in AllCat:
    # cats.append(var["category"])
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
    user = request.user

    newContact  =  contact(email=email ,name=name , desc=desc , phone=tel ,screenshot=File,author=user)
    newContact.save()

    return HttpResponse("Thank you")


def checkout(request):
    str = request.POST.get("cartJson")
    cart = json.loads(str)
    currentCart = cart


    totalPrice = 0 
    for id in cart:


        temp= cart[id]
        tempOb = course.objects.get(id=id)
        price = tempOb.price
        temp["price"]=price
        temp["totalItemPrice"] = price * temp["value"]
        totalPrice = totalPrice + temp["totalItemPrice"]
        currentCart[id] = temp 
    params = {
        "totalPrice" : totalPrice,
        "data": currentCart
    }
    return render(request,"course\checkout.html",params)

def submitcheckout(request):
    if(request.method=="POST"):
        jsonCart= request.POST.get("jsonCart")
        first_name= request.POST.get("first_name")
        last_name= request.POST.get("last_name")
        email= request.POST.get("email")
        address= request.POST.get("address")
        state= request.POST.get("state")
        zip= request.POST.get("zip")
        isSameBillingAddress= request.POST.get("isSameBillingAddress")
        if(isSameBillingAddress=="on"):
            isSameBillingAddress = True
        else:
            isSameBillingAddress = False
        newOrder = order(jsonCart=jsonCart,email=email, first_name=first_name ,last_name=last_name,state=state,zip=zip,address=address,isSameBillingAddress=isSameBillingAddress)
        newOrder.save()
        return HttpResponse("Thank you for ordering!!")
    else:
        return HttpResponse("You are on a wrong page. please <a href='/course/list'>Click here</a> to add items")

    return HttpResponse("Thank you")
    # return render(request,"course\contactus.html")


def loginView(request):
    username = request.POST.get('username')
    pass1 = request.POST.get('pass')
    print(username)
    print(pass1)
    user = authenticate(username = username , password = pass1)
    print(user)
    if user is not None:
        login(request , user)
        return HttpResponse("Login succ") 
    else:
        return HttpResponse("Login failed")    
    


def Loginn(request):

    return render(request,"course/login.html")


def signupView(request):
    
    
    return render(request,"course/signup.html")


def signup(request):
    username = request.POST.get('username')
    email = "roh@hh.com"
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    pass1 = request.POST.get('pass1')
    pass2 = request.POST.get('pass2')
    print(username )
    myUser = User.objects.create_user(username,email,pass1)
    myUser.save()
    
    
    return HttpResponse("signin suc")




def bloglist(request):
    
    
    return render(request,"course/bloglist.html")




def blogcreate(request):
    
    
    return render(request,"course/blogcreate.html")




def blogdetails(request):
    
    
    return render(request,"course/blogdetails.html")



