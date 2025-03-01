from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .models import Library
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden
from .models import UserProfile
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseForbidden
from .models import Article



# Create your views here.

def bookshelf_view(request):
    return HttpResponse("This is the bookshelf view")


def relationship_app_view(Request):
    return HttpResponse("This is the relationship_app view")


#Create a function-based view
def relationship_app_view(request):
    """Retrieves all books and renders a template displaying the list."""
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, 'relationship_app/list_books.html')

def list_books(request):
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, 'relationship_app/list_books.html')

#Create a class-based view 
#Utilising the ListView to display details for a specific library, listing all books available in that library.
class relationship_appListView(ListView):
    model = Library
    template_name = "bookshelf/library_detail.html"


#Create a class-based view utilising the DetailView to display a specific library                                                   #Utilising the DetailView to display details for a specific library, listing all books available in that library.
class LibraryDetailView(DetailView):
    model = Library
    template_name = "bookshelf/library_detail.html"

    def get_context_data(self, **kwargs):
        """Injects additional context data specific to the book."""
        context = super().get_context_data(**kwargs)  # Get default context data
        book = self.get_object()  # Retrieve the current book instance
        context['average_rating'] = book.get_average_rating()

#Using Django's built-in Class Based View, CreateView to build a register form 
class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

#Create a custom function-based view to build a register form
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'bookshelf/register.html', {'form':form})





@permission_required('bookshelf.can_view', raise_exception=True)
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'bookshelf/article_list.html', {'articles': articles})

@permission_required('bookshelf.can_create', raise_exception=True)
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('articles:article_list')  
    else:
        form = ArticleForm()  

    return render(request, 'bookshelf/article_create.html')

@permission_required('app_name.can_edit', raise_exception=True)
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        pass
    return render(request, 'articles/article_edit.html', {'article': article})

@permission_required('app_name.can_delete', raise_exception=True)
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('article_list')
    return render(request, 'articles/article_confirm_delete.html', {'article': article})
