'''@api_view()
def movie_list(request):
    movies = models.MovieList.objects.all()
    serializer = serializers.MovieListSerializer(movies,many=True)
    return Response(serializer.data)*11th line'''
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status 
from watchlist_app import models
from . import serializers
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import viewsets 
import django_filters.rest_framework 
from . import pagination
#from rest_framework.permissions import IsAuthenticated
@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = models.MovieList.objects.all()
        serializer = serializers.MovieListSerializer(movies, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = serializers.MovieListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
@api_view(['GET', 'PUT','PATCH','DELETE'])
def movie_detail(request,id):
    movie = get_object_or_404(models.MovieList,id=id)
    #todo: GET [movie data show korar jonno get use hoy]
    if request.method == 'GET':
        serializer = serializers.MovieListSerializer(movie)
        return Response(serializer.data,status=status.HTTP_200_OK)
    #todo: PUT [update/edit jonno whole object patate hoy]
    elif request.method == 'PUT':
        serializer = serializers.MovieListSerializer(movie,data=request.data )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    #todo: DELETE[Shudu delete korar jonno delete use hoy]
    elif request.method == 'DELETE':
        movie.delete()
        return Response({"message" : "Movie deleted Success"})
    #todo:Patch[Shudu ekta part change korar jonno patch use hoy]
    elif request.method== "PATCH":
        serializer = serializers.MovieListSerializer(movie,data=request.data,partial=True )
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    
#!Class Base
#1. List of all movies,Create a new movie
class MovieListCreateView(generics.ListCreateAPIView):
    queryset = models.MovieList.objects.all()
    serializer_class = serializers.MovieListSerializer
#2. Single Movie/update/delete
class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.MovieList.objects.all()
    serializer_class = serializers.MovieListSerializer
    
#1. List of all Review,Create a new review
class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = models.Reviews.objects.all()
    serializer_class = serializers.ReviewSerializer
#2. Single Review/update/delete
class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Reviews.objects.all()
    serializer_class = serializers.ReviewSerializer
    
    
class MovieListViewSet(viewsets.ModelViewSet):
    
    queryset = models.MovieList.objects.prefetch_related('reviews')
    #* prefetch_related -> M2M, reverse foreign key relation
    serializer_class=serializers.MovieListSerializer
    pagination_class = pagination.MovieCursorPagination    

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = models.Reviews.objects.select_related('movie')
    serializer_class=serializers.ReviewSerializer
    #permission_classes = [permissions.IsReviewerOrReadOnly,IsAuthenticated]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['reviewer__username', 'rating']

    