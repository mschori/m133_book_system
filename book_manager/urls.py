from django.urls import path
from . import views

urlpatterns = [
    path('authors', views.list_authors, name='authors'),
    path('books', views.list_books, name='books'),
    path('authors/<int:author_id>', views.show_author, name='show_author'),
]
