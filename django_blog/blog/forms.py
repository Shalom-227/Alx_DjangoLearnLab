from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, Post



#extending UserCreationForm to create registration form that includes email field
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields = ['bio', 'image']

class PostForm(forms.ModelForm):

    class Meta:
        fields = ['title', 'content', 'author']
