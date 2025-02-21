from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Library
from django.views.generic.list import ListView
# Create your views here.
#def relationship_app_view(Request):
#    return HttpResponse("This is the relationship_app view")


#Create a function-based view
def relationship_app_view(request):
    """Retrieves all books and renders a template displaying the list."""
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, 'relationship_app/list_books.html')


#Create a class-based view 
#Utilising the ListView to display details for a specific library, listing all books available in that library.
class relationship_appListView(ListView):
    model = Book
    template_name = "relationship_app/library_detail.html"
