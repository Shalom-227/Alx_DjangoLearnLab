# This document performs a specific operation in Django Shell

# open Django shell
python manage.py shell

#update object attribute title
my_book.title = "Nineteen Eighty-Four"

#confirm update
Book.objects.get().title

# output: 'Nineteen Eighty-Four'
                                                                       ~                                               
