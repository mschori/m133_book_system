from django.shortcuts import render
from .models import Author, Book


def show_authors(request):
    authors = Author.objects.all()
    return render(request, 'book_manager/show_authors.html', {'authors': authors})


def show_books(request):
    books = Book.objects.all()
    return render(request, 'book_manager/show_books.html', {'books': books})
