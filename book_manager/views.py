from django.shortcuts import render, redirect
from .models import Author, Book
from .forms import AuthorForm, BookForm
from django.contrib import messages


def list_authors(request):
    authors = Author.objects.all()
    form = AuthorForm()
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Author successfully created.')
    return render(request, 'book_manager/list_authors.html', {'authors': authors, 'form': form})


def list_books(request):
    books = Book.objects.all()
    form = BookForm()
    return render(request, 'book_manager/list_books.html', {'books': books, 'form': form})


def show_author(request, author_id):
    try:
        author = Author.objects.get(pk=author_id)
    except Author.DoesNotExist:
        messages.error(request, 'There is no author with this id!')
        return redirect(list_authors)
    return render(request, 'book_manager/show_author.html', {'author': author})
