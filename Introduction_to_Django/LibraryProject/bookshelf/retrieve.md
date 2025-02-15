# This documents performs a specific operation in Django Shell

# open Django shell
python manage. shell

# this command retrieves and displays all attributes of the object, my_book
my_book = Book.objects.get(title="1984")
print(my_book.title)
print(my_book.author)
print(my_book.publication_year)

# output: <Book: George Orwell> '1984' 'George Orwell' 1949 
