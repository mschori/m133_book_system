from django.urls import path
from . import views

urlpatterns = [
    path('authors', views.show_authors, name='authors'),
    path('books', views.show_books, name='books'),
]
