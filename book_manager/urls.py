from django.urls import path
from . import views

urlpatterns = [
    path('authors', views.list_authors, name='authors'),
    path('books', views.list_books, name='books'),
    path('authors/<int:author_id>', views.show_author, name='show_author'),
    path('books/<str:book_id>', views.show_book, name='show_book'),
    path('authors/<int:author_id>/delete', views.delete_author, name='delete_author'),
    path('books/<str:book_id>/delete', views.delete_book, name='delete_book'),
]
