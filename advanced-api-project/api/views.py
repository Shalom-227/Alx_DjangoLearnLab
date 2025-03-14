from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from .models import Book, Author
from .serializers import BookSerializer
from datetime import datetime
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.permissions import BasePermission
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class ListView(generics.ListAPIView):
    #list all books
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    #permissions not set allowing unauthenticated users read-only access

    # Add filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # List of # Fields that can be filtered
    filterset_fields = ["title", "author", "publication_year"]
    # List of Fields that can be searched using '?search=keyword'
    search_fields = ["title", "author"]
    # Fields that can be used for sorting using '?ordering=title'
    ordering_fields = ["title", "publication_year"]


class DetailView(generics.RetrieveAPIView):
    #retrieves a single book by ID
    queryset = Book.objects.all()
    serializer_class = BookSerializer
     #permissions not set allowing unauthenticated users read-only access


class CreateView(generics.CreateAPIView):
    #creates a new book
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    #only authenticated user can create book instance
    permissions_classes = [permissions.IsAuthenticated]

    #overriding the default perform_create() function to ensure book objects created are not beyond publication year i.e publication year cannot be in the future
    def perfom_create(self, serializer):
        publication_year = serializer.validated_data.get("publication_year")
        current_year = datetime.now().year

        if publication_year > current_year:
            raise serializers.ValidationError({"publication_year": "Publication year cannot be in the future."})
        serializer.save()

#integrating permission checks directly in the view file for UpdateView
#if user is the owner of the book instance permission to edit or update is allowed but if user is not owner user can only view but not edit.
class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True  
        return obj.owner == request.user

 
class UpdateView(generics.UpdateAPIView):
    #updates an existing book
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    #only authenticated user can update book instance
    permissions_classes = [permissions.IsAuthenticated]

    #overriding the default perform_update() function to ensure that when book objects are updated publication year cannot be in the future
    def perform_update(self, serializer):
        publication_year = serializer.validated_data.get("publication_year")
        current_year = datetime.now().year

        if publication_year > current_year:
            raise serializers.ValidationError({"publication_year": "Publication year cannot be in the future."})
        serializer.save()

#only authenticated user can delete a book instance
class DeleteView(generics.DestroyAPIView):
    #deletes a book
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    #only authenticated user can delete object instance
    permissions_classes = [permissions.IsAuthenticated]
