from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('movies', views.MovieListViewSet,basename='movielist')
router.register('reviews', views.ReviewViewSet,basename='reviewlist')
urlpatterns = [
      path('',include(router.urls)),
#     path('movie/', views.movie_list,name="movie_list"),
#     path('movie/<int:id>/', views.movie_detail,name="movie_list"),
    # path('movie/', views.MovieListCreateView.as_view(),name="movie_list"),
    # path('movie/<int:pk>/', views.MovieDetailView.as_view(),name="movie_detail"),path('review/', views.ReviewListCreateView.as_view(),name="review_list"),
    # path('review/<int:pk>/', views.ReviewDetailView.as_view(),name="review_detail"),
]