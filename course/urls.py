from . import views
from django.urls import path 

urlpatterns = [
    
    path('',views.Index),
    path('list/',views.List),
    path('detail/<int:id>',views.Detail),
    path('contactus/',views.contactUs),
    path('contactsubmit/',views.contactSubmit),
    path('checkout/',views.checkout),
    
]
