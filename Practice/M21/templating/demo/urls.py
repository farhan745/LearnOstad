from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('contact/',views.contact,name="contact"),
    path('about/',views.about,name="about"),
    path('report/',views.report,name="report"),
    path('data/',views.data,name="data"),
    path('loop/',views.loop,name="loop")
    
]