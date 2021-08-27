from . import views
from django.urls import path 

urlpatterns = [

    path('',views.Index),
    path('list/',views.List),

]
