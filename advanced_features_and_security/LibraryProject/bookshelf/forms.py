from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'content']
