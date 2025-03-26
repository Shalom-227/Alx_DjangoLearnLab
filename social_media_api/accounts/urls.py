from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
        #generate and use authentication token
        path('api-token-auth/', obtain_auth_token, name = 'api_token_auth'),

       #creating views for authentication
       path('register/', views.RegisterView.as_view(), name='register'),
       path('login/', views.LoginView.as_view(), name='login'),
       path('logout/', views.LogoutView.as_view(), name='logout'),
       path('profile/', views.UserProfileView.as_view(), name='profile'),
        ]
