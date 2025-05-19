from django.contrib import admin
from django.urls import path,include
#todo 1: Signup
#todo 2: Login
#todo 3: Logout
#todo 4: Password Change
#todo 5: Session Storage
#todo 6: middleware
from . import views

urlpatterns = [
    path('signup/', views.user_sign_up,name='signup'),
    path('login/', views.user_login,name='login'),
    path('home/', views.home,name='home'),
    path('pass_change/', views.pass_change,name='pass_change'),
    path('logout/', views.user_logout,name='logout'),
]
