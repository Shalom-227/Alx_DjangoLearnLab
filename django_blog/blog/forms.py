from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, Post, Comment, Tag



#extending UserCreationForm to create registration form that includes email field
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields = ['bio', 'image', 'email', 'user']

class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False)

    class Meta:
        fields = ['title', 'content', 'author', 'tags']


    def save(self, commit=True):
        instance = super().save(commit=False)
        tag_names = self.cleaned_data['tags']
        instance.save()
        instance.tags.set(*[tag.strip() for tag in tag_names.split(",")])
        return instance

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Leave a comment...'}),
        }
