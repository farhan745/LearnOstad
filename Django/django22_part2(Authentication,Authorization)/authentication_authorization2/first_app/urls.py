from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('signup/',views.user_signup,name = 'signup' ),
    path('login/',views.user_login,name = 'login' ),
    path('logout/',views.user_logout,name = 'logout' ),
    path('pass_change/',views.password_change,name = 'password-change' ),
]