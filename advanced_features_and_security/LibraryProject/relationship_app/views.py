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


# Create your views here.
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
    template_name = "relationship_app/library_detail.html"


#Create a class-based view utilising the DetailView to display a specific library                                                   #Utilising the DetailView to display details for a specific library, listing all books available in that library.
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"

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

    return render(request, 'relationship_app/register.html', {'form':form})


# Helper function to check if the user is an Admin
def is_admin(user):
    return user.userprofile.role == UserProfile.ADMIN

# Admin view
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')  # Template for the admin view

# Helper function to check if the user is a Librarian
def is_librarian(user):
    return user.userprofile.role == UserProfile.LIBRARIAN

# Librarian view                                                      @user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')  # Template for the librarian view


# Helper function to check if the user is a Member
def is_member(user):
    return user.userprofile.role == UserProfile.MEMBER

# Member view
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')  # Template for the member view


#Adding Book View
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        Book.objects.create(title=title, author=author)
        
        return redirect('book_list')
    return render(request, 'relationship_app/add_book.html')

# Editing Book View
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.save()
        return redirect('book_list')
    return render(request, 'relationship_app/edit_book.html', {'book': book})

# Deleting Book View
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'relationship_app/delete_book.html', {'book': book})

