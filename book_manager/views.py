from django.shortcuts import render, redirect
from .models import Author, Book
from .forms import AuthorForm, BookForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required()
def list_authors(request):
    authors = Author.objects.all()
    form = AuthorForm()
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Author successfully created.')
    return render(request, 'book_manager/list_authors.html', {'authors': authors, 'form': form})


@login_required()
def list_books(request):
    books = Book.objects.all()
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book successfully created.')
    return render(request, 'book_manager/list_books.html', {'books': books, 'form': form})


@login_required()
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
        form = AuthorForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            author.first_name = form.cleaned_data['first_name']
            author.last_name = form.cleaned_data['last_name']
            author.image = form.cleaned_data['image']
            author.save()
    return render(request, 'book_manager/show_author.html', {'author': author, 'form': form})


@login_required()
def show_book(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        messages.error(request, 'There is no book with this id!')
        return redirect(list_books)
    form = BookForm(initial={
        'isbn': book.isbn,
        'title': book.title,
        'read': book.read,
        'authors': [i.id for i in book.authors.all()]
    })
    if request.method == 'POST':
        old_book_isbn = book.isbn
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            new_book_isbn = form.cleaned_data['isbn']
            if new_book_isbn != old_book_isbn:
                if Book.objects.filter(isbn=new_book_isbn).exists():
                    messages.error(request, 'This ISBN is already in use!')
                    return redirect('show_book', book_id=book_id)
                else:
                    new_book = Book.objects.create(
                        isbn=form.cleaned_data['isbn'],
                        title=form.cleaned_data['title'],
                        read=form.cleaned_data['read'],
                    )
                    new_book.authors.add(*[i.id for i in form.cleaned_data['authors'].all()])
                    Book.objects.get(isbn=old_book_isbn).delete()
                    messages.success(request, 'Book successfully updated.')
                    return redirect('show_book', book_id=new_book_isbn)
            else:
                form.save()
            messages.success(request, 'Book successfully updated.')
    return render(request, 'book_manager/show_book.html', {'book': book, 'form': form})


@login_required()
def delete_author(request, author_id):
    try:
        author = Author.objects.get(pk=author_id)
        if Book.objects.filter(authors=author):
            messages.error(request, 'This author has still books registered.')
        else:
            author.delete()
            messages.success(request, 'Author successfully deleted.')
    except Author.DoesNotExist:
        messages.error(request, 'There is no author with this ID.')
    return redirect('authors')


@login_required()
def delete_book(request, book_id):
    try:
        book = Book.objects.get(isbn=book_id)
        book.delete()
        messages.success(request, 'Book successfully deleted.')
    except Book.DoesNotExist:
        messages.error(request, 'There is no book with this ISBN.')
    return redirect('books')
