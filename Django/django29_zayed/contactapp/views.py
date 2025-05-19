from django.shortcuts import render
from rest_framework import viewsets
from .models import Contact,Author,Book
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ContactSerializer,AuthorSerializer,BookSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework.filters import SearchFilter
# Create your views here.
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_fields = ["id","title"]
    #! make lite widgets from this game 
    
    search_fields = ["title"]
    
class IsOwnerOrReadOnly(permissions.BasePermission):
    '''Custom permission to only allow owners of an object to edit it'''
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        #! Write permissions are only allowed to the owner
        return obj.user == request.user
'''from django_filters import FilterSet,NumberFilter   
class BookFilter(FilterSet):
    min_price = NumberFilter(field_name="price",lookup_expr="gte")
    max_price = NumberFilter(field_name="price",lookup_expr="gte")
    class Meta:
        models = Book
        fields = ["min_price","max_price"]'''