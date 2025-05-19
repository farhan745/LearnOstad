from django.contrib import admin
from django.urls import path, include
from .views import ContactViewSet,AuthorViewSet,BookViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView


router = DefaultRouter()
router.register('contacts', ContactViewSet)
router.register('authors' , AuthorViewSet)

router.register('books', BookViewSet)
urlpatterns = [
    path("login/",TokenObtainPairView.as_view(),name="login"),
    path('', include(router.urls)),  # Include the URLs from the router object
]