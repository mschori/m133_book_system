from django.shortcuts import render
from .models import Author, Book
from .forms import AuthorForm, BookForm
from django.contrib import messages


def show_authors(request):
    authors = Author.objects.all()
    form = AuthorForm()
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Author successfully created.')
    return render(request, 'book_manager/show_authors.html', {'authors': authors, 'form': form})


def show_books(request):
    books = Book.objects.all()
    form = BookForm()
    return render(request, 'book_manager/show_books.html', {'books': books, 'form': form})
