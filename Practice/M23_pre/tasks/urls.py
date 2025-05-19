from django.urls import path
from .import views

urlpatterns = [
    path('', views.loginpage, name='login'),
    path('home', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('add_task', views.add_task, name='add_task'),
    path('completed', views.completed, name='completed'),
    path('remaining', views.remaining, name='remaining'),
    path('detail/<str:task_id>', views.task_detail, name='task_detail'),
    path('delete_task/<str:task_id>', views.delete_task, name='delete'),
    path('toggle_complete/<str:task_id>', views.toggle_complete, name='toggle_complete'),
    path('remove_task/<str:task_id>', views.remove_task, name='remove_task'),
]