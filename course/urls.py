from . import views
from django.urls import path 

urlpatterns = [
    
    path('',views.Index),
    path('list/',views.List),
    path('detail/<int:id>',views.Detail),
    path('contactus/',views.contactUs),
    path('contactsubmit/',views.contactSubmit),
    path('checkout/',views.checkout),
    path('submitcheckout/',views.submitcheckout),
    path('form/login/',views.Loginn),
    path('login/',views.loginView),
    path('signup/',views.signup),
    path('form/signup/',views.signupView),
    path('bloglist/',views.bloglist),
    path('blogcreate/',views.blogcreate),
    path('blogdetails/',views.blogdetails),
    
]
