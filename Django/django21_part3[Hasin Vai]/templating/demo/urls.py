from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", views.data, name="data"),
    path("loop/", views.loop, name="loop"),
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="reports"),
    path("reports/", views.reports, name="reports"),
]
