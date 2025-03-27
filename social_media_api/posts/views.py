from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, status
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_frameworks import generics
from notifications.models import Notification  # Import for notifications

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


class PostViewSet(viewsets.ModelViewSet):
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

class CommentViewSet(viewsets.ModelViewSet):
    #ModelViewSet provides all CRUD operations
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """Ensure the logged-in user is set as the author when creating a comment."""
        serializer.save(author=self.request.user)

class FollowedPostsView(generics.ListAPIView):
    """
    View to show posts from users the authenticated user follows.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]  # Ensure user is logged in

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()  # Get users the current user follows
        return Post.objects.filter(author__in=following_users).order_by('-created_at')  # Get their posts

class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if created:
            # Generate notification
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                target=post
            )
            return Response({"message": "Post liked."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "You already liked this post."}, status=status.HTTP_400_BAD_REQUEST)


class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, post_id):
        post = generics.get_object_or_404(Post, id=post_id)
        like = Like.objects.filter(user=request.user, post=post)

        if like.exists():
            like.delete()
            return Response({"message": "Post unliked."}, status=status.HTTP_204_NO_CONTENT)
        return Response({"message": "You haven't liked this post."}, status=status.HTTP_400_BAD_REQUEST)
