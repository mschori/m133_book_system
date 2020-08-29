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
    form = BookForm(is_update=False)
    return render(request, 'book_manager/list_books.html', {'books': books, 'form': form})


def show_author(request, author_id):
    try:
        author = Author.objects.get(pk=author_id)
    except Author.DoesNotExist:
        messages.error(request, 'There is no author with this id!')
        return redirect(list_authors)
    form = AuthorForm(initial={
        'first_name': author.first_name,
        'last_name': author.last_name,
    })
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            author.first_name = form.cleaned_data['first_name']
            author.last_name = form.cleaned_data['last_name']
            author.image = form.cleaned_data['image']
            author.save()
    return render(request, 'book_manager/show_author.html', {'author': author, 'form': form})


def show_book(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        messages.error(request, 'There is no book with this id!')
        return redirect(list_books)
    form = BookForm(is_update=True, initial={
        'isbn': book.isbn,
        'title': book.title,
        'read': book.read,
        'authors': [i.id for i in book.authors.all()]
    })
    if request.method == 'POST':
        form = BookForm(request.POST, is_update=True)
        if form.is_valid():
            book.title = form.cleaned_data['title']
            print(book.title)
            # for author in form.cleaned_data['authors']:
            #     book.authors.add(Author.objects.get(pk=author.id))
            messages.success(request, 'Book successfully updated.')
    return render(request, 'book_manager/show_book.html', {'book': book, 'form': form})
