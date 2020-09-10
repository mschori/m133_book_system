from book_manager.models import Book
from .TestAuthor import TestAuthor


class TestBook:
    isbn = '35924547-5'
    title = 'Der Herr der Ringe'
    read = False
    test_author = TestAuthor()

    def __init__(self):
        try:
            Book.objects.get(title=self.title)
        except Book.DoesNotExist:
            book = Book.objects.create(
                isbn=self.isbn,
                title=self.title,
                read=self.read
            )
            book.authors.add(self.test_author.get_test_author())

    def get_test_book(self):
        return Book.objects.get(title=self.title)
