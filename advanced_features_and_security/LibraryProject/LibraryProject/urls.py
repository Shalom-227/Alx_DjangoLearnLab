"""
URL configuration for LibraryProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from bookshelf.views import bookshelf_view
#from relationship_app.views import relationship_app_view, relationship_appListView, LibraryDetailView, list_books
#from relationship_app.views import RegisterView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
#:wqfrom relationship_app.views import register
from django.contrib.auth import views as auth_views
#from relationship_app.views import member_view, librarian_view
#from relationship_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookshelf/', bookshelf_view),
    path('relationship_app', bookshelf_view),
    path('library_detail/', bookshelf_view, name='library_detail'),
    #path('library_detail/', LibraryDetailView.as_view(), name='library_detail'),
    #path('list_books/', list_books, name="list_books"),
    path('login/', LoginView.as_view(template_name='bookshelf/login.html'), name='login'),
#    path('logout/', LogoutView.as_view(template_name ='bookshelf/logout.html'), name='logout'),
     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
     #path('librarian/', librarian_view, name='librarian_view'),
     #path('member/', member_view, name='member_view'),
     #path('add_book/', views.add_book, name='add_book'),
     #path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
     #path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
 #    path('', include("relationship_app.urls")),
     path('', include("bookshelf.urls"))
]
