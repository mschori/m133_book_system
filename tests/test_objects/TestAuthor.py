from book_manager.models import Author


class TestAuthor:
    first_name = 'J. R. R.'
    last_name = 'Tolkien'
    image = 'default.png'

    def __init__(self):
        try:
            Author.objects.get(first_name=self.first_name)
        except Author.DoesNotExist:
            Author.objects.create(
                first_name=self.first_name,
                last_name=self.last_name,
                image=self.image
            )

    def get_test_author(self):
        return Author.objects.get(first_name=self.first_name)
