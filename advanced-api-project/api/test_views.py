from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from api.models import Book, Author
from datetime import datetime
from django.urls import reverse
from rest_framework.test import APITestCase



class BookAPITestCase(APIClient):
    def setUp(self):
        """Set up test data before each test."""
        self.client = APIClient()

        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpass")

        # Create a test author
        self.author = Author.objects.create(name="John Doe")

        # Create a test book
        self.book = Book.objects.create(
            title="Test Book",
            publication_year=2025,
            author=self.author
        )

        # Define API endpoints
        self.list_url = "/api/books/"
        self.detail_url = f"/api/books/{self.book.id}/"

        #url names to match url patterns
        lf.list_url = reverse("book-list")  # /api/books/
        self.detail_url = reverse("book-detail", kwargs={"pk": self.book.id})  # /api/books/1/
        self.create_url = reverse("book-create")  # /api/books/create/
        self.update_url = reverse("book-update", kwargs={"pk": self.book.id})  # /api/books/1/update/
        self.delete_url = reverse("book-delete", kwargs={"pk": self.book.id})  # /api/books/1/delete/

    def authenticate(self):
        """Authenticate user for protected routes."""
        self.client.force_authenticate(user=self.user)


#testing CRUD OPERATIONS

    def test_list_books(self):
        """Test to retrieve a list of books."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_book(self):
        """Test to retrieve a book by ID."""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test Book")

    def test_get_single_book(self):
        """Test retrieving a book by ID."""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test Book")

    def test_create_book(self):
        """Test creating a book (requires authentication)."""
        self.authenticate()
        data = {
            "title": "New Book",
            "publication_year": 2022,
            "author": self.author.id
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book(self):
        """Test to update a book (requires authentication)."""
        self.authenticate()
        data = {
            "title": "Updated Title",
            "publication_year": 2022,
            "author": self.author.id
        }
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Title")

    def test_delete_book(self):
        """Test deleting a book (requires authentication)."""
        self.authenticate()
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)





