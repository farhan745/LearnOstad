from django.urls import path

from . import views
app_name = 'media'
urlpatterns = [
    path('',views.media_list,name = 'media_list'),
    path('upload/',views.media_upload,name = 'media_upload'),
    path('edit/<int:pk>/',views.media_edit,name = 'media_edit'),
    path('delete/<int:pk>/',views.media_delete,name = 'media_delete'),
]