#!/bin/python3

from relationship_app.models import Author, Book, Library, Librarian

#Query all books by a specific author.

author = Author.objects.get(name = "")
print(author.book_set.all())

#List all books in a library.
library = Library.objects.get()
print(library.books.all())

#Retrieve the librarian for a library.
library = Library.objects.get()
print(library.librarian)

