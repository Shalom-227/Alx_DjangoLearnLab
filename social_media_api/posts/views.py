from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

# Create your views here.


''' Custom permission to allow only the owner of a post or comment instance
    to edit or delete it. Using IsAuthenticatedOrReadOnly alone will allow 
    author A to delete and edit a post or comment instance from author B. 
    This is why we have define a custom permission  as well.'''
class IsOwnerOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class PostViewSet(ModelViewSet):
    #ModelViewSet provides all CRUD operations
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]
    pagination_class = PageNumberPagination  #use default pagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['author'] #exact match filter
    search_fields = ['title', 'content'] #search by title or content

    def perform_create(self, serializer):
        """Ensure the logged-in user is set as the author when creating a post."""
        serializer.save(author=self.request.user)

class CommentViewSet(ModelViewSet):
    #ModelViewSet provides all CRUD operations
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """Ensure the logged-in user is set as the author when creating a comment."""
        serializer.save(author=self.request.user)
