# This documents creates a specific operation in Django Shell

# open Django shell
python manage.py shell

# import Model
from bookshelf.models import Book

# this command will creates an instance of the Model, Book adding attributes and assigning their respective values
my_book = Book.objects.create(title = "1984", author = "George Orwell", publication_year = 1949)

# confirm object creation and definition
Book.objects.all()
# output: <QuerySet [<Book: George Orwell>]>. 
