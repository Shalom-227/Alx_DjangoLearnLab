from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [

    #custom views
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('home/', views.home, name='home'),
    path('posts/', views.post_list, name='posts'),

    #authentication views
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),

    #views for Post CRUD operations
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

    #views for Comment CRUD operations
    path("posts/<int:pk>/comments/", views.CommentListView.as_view(), name="comment_list"),
    path("post/<int:pk>/comments/new/", views.CommentCreateView.as_view(), name="comment_create"),
    path("comment/<int:pk>/update/", views.CommentUpdateView.as_view(), name="comment_edit"),
    path("comment/<int:pk>/delete/", views.CommentDeleteView.as_view(), name="comment_delete"),




        ]
