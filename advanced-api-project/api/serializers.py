from rest_framework import serializers
from .models import Author, Book
from datetime import date


#The BookSerializer takes a book model instance and converts it into a JSON representation and validates the publication year

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

        def validate_publication_year(self, data):
            #data represents the date entered in by user
            #current_year defines the current year

            current_year = date.today().year
            #if date entered is greater than current year return error other wise return date entered
            if data > current_year:
                raise serializers.ValidationError("Publication year cannot be in the future")
            return data

#creating nested serializer where nested books are under author. When an auhtor is retrieved we can their their books.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

