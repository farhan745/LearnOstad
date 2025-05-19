from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.post_list,name="post_list"),
    path('post/<int:id>/',views.post_details,name="post_details"),
    path('post_edit/<int:id>/',views.post_edit,name="post_edit"),
    path('post_delete/<int:id>/',views.post_delete,name="post_delete"),
    path('login/',auth_views.LoginView.as_view(template_name="registration/login.html" ,next_page='post_list'),name="login"),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name="logout"),
    path('register/',views.signup_view,name="register"),
    path('post_create/',views.post_create,name="post_create"),
    path('like_post/<int:id>/',views.Like_post,name="like_post"),
    
]