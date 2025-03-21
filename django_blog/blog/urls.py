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
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),    


        ]
