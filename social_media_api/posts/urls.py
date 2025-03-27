from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views



router = DefaultRouter() #creates router and register ViewSet with it
router.register(r'posts', views.PostViewSet, basename='post')
router.register(r'comments', views.CommentViewSet, basename='comment')

urlpatterns = [
        
       path('', include(router.urls)),
       path('feed/', views.FollowedPostsView.as_view(), name='followed-posts'),
        ]
