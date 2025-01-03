from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile),
    # path('',views.home),
    # path('home/', views.home),
]