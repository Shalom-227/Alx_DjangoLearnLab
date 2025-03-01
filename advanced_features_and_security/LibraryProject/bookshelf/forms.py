from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'content']i

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
