#!/bin/python3

from relationship_app.models import Author, Book, Library, Librarian

#Query all books by a specific author.

author = Author.objects.get(name = "")
print(author.book_set.all())

#List all books in a library.
library = Library.objects.get(name=library_name)
print(library.books.all())

#Retrieve the librarian for a library.
librarian = Librarian.objects.get(name=librarian_name)
print(librarian.library)

