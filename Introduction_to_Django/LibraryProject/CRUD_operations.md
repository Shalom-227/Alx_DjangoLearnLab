# This file documents creates a specific operation in Django Shell

# open Django shell
python manage.py shell

# import Model Book
from bookshelf.models import Book

# this command will CREATE an instance of the Model, Book adding attributes and assigning their respective values
my_book = Book.objects.create(title = "1984", author = "George Orwell", publication_year = 1949)

#output: 

# confirm object creation and definition
Book.objects.all()
# output: <QuerySet [<Book: George Orwell>]>.



# this command will READ and display all attributes of the object, my_book
my_book = Book.objects.latest('id')
print(my_book.title)
print(my_book.author)
print(my_book.publication_year)

# output: <Book: George Orwell> 
#	  '1984' 
#	  'George Orwell' 
#	  1949


#UPDATE object attribute, title
my_book.title = "Nineteen Eighty-Four"
my_book.save()

#confirm update
Book.objects.get().title

# output: 'Nineteen Eighty-Four'

# delete object.
my_book.delete()
# output: (1, {'bookshelf.Book': 1})

#confirm deletion. Trying to retrieve book object.
Book.objects.all()

# output: <QuerySet []>

