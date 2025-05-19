from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

   # path('create_student/', views.create_student,name='create_student'),#! function Base
    path('create_student/', views.CreateStudent.as_view(),name='create_student'),#! Class Base
    #path('home/', views.home,name='home'),#? Function Base
    path('home/', views.StudentList.as_view(),name='home'), #? Class Base
    #path('edit/<int:id>/', views.update_student,name='update_student'),#! function Base
    path('edit/<int:id>/', views.UpdateStudentData.as_view(),name='update_student'),#! class Base
   # path('delete/<int:id>/', views.delete_student,name='delete_student'),#! function Base
   path('delete/<int:id>/', views.DeleteStudent.as_view(),name='delete_student'),
   #?SIgn up
   path('signup/', views.signup, name='signup'),
   #?Login
   path('login/', views.Login, name='user_login'),
   path('logout/', views.user_logout, name='user_logout'),
   path('profile/', views.profile, name='profile'),
]