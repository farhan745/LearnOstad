from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
                #path("home/", views.home,name = "home"),
               #path("", views.display),
             #  path("home/", views.home,name = "home"),#function Base view
               path("home/", views.StudentLists.as_view(),name = "home"),#class Base view
               #path("create/", views.create_student,name = "create_student"),#function create_student
               path("create/", views.CreateStudent.as_view(),name = "create_student"),#class base
               #path("edit/<int:id>/", views.update_student,name = "update_student"),#function Base
               path("edit/<int:id>/", views.UpdateStudentData.as_view(),name = "update_student"),#class Base
              #  path("delete/<int:id>/", views.delete_student,name = "delete_student"),#function Base
               path("delete/<int:id>/", views.DeleteStudent.as_view(),name = "delete_student"),#class Base
               ]
