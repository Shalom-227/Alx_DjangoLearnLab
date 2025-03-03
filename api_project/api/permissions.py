from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import BasePermission


class BookList(APIView):
    #applying basic permissions, IsAuthenticated
    permission_classes = [IsAuthenticated]

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

#defining custom permission class
class IsBookAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
