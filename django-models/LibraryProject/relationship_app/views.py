from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .models import Library
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
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
    model = Library
    template_name = "relationship_app/library_detail.html"


#Create a class-based view                                                  #Utilising the DetailView to display details for a specific library, listing all books available in that library.
class relationship_appDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"

    def get_context_data(self, **kwargs):
        """Injects additional context data specific to the book."""
        context = super().get_context_data(**kwargs)  # Get default context data
        book = self.get_object()  # Retrieve the current book instance
        context['average_rating'] = book.get_average_rating()

