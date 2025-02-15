# This documents creates a specific operation in Django Shell

# open Django shell
python manage.py shell

#import model book
from bookshelf.models import Book

my_book.delete()
# output: (1, {'bookshelf.Book': 1})

#confirm deletion
Book.objects.all()

# output: <QuerySet []>

