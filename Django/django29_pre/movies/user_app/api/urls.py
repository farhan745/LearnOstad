from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views as auth_views
from rest_framework.routers import DefaultRouter
from . import views as custom_views

router = DefaultRouter()
router.register('register', custom_views.RegistrationViewSet, basename='register')  # Fix: Typo corrected in view name

urlpatterns = [
    path('login/', auth_views.obtain_auth_token),  # Fix: Explicit naming for 'auth_views'
    path('', include(router.urls)),  # Fix: Directly pass 'router.urls'
    path('logout/',custom_views.LogoutView.as_view()),  
]