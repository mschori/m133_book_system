from django.test import TestCase
from .test_objects.TestUser import TestUser
from .test_objects.TestAuthor import TestAuthor
from .test_objects.TestBook import TestBook
from django.urls import reverse


class BookManagerViews(TestCase):
    def setUp(self):
        self.test_user = TestUser()
        self.test_author = TestAuthor()
        self.test_book = TestBook()

    def login_user(self):
        self.client.login(username=self.test_user.username, password=self.test_user.password)

    def check_template_use_base(self, response):
        self.assertTemplateUsed(response, 'base.html')

    def check_login_parts(self, response):
        self.assertTemplateUsed(response, 'registration/login.html')
        self.check_template_use_base(response)
        self.assertContains(response, 'name="username"')
        self.assertContains(response, 'name="password"')

    def test_check_redirect_to_login(self):
        for link in ['authors', 'books']:
            response = self.client.get(reverse(link), follow=True)
            self.check_login_parts(response)
        response = self.client.get(reverse('show_author', args=[self.test_author.get_test_author().id]), follow=True)
        self.check_login_parts(response)
        response = self.client.get(reverse('show_book', args=[self.test_book.get_test_book().isbn]), follow=True)
        self.check_login_parts(response)

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.check_login_parts(response)

    def test_list_authors(self):
        self.login_user()
        response = self.client.get(reverse('authors'))
        self.check_template_use_base(response)
        self.assertTemplateUsed(response, 'book_manager/list_authors.html')
        self.assertContains(response, self.test_author.first_name)
        self.assertContains(response, self.test_author.last_name)
        self.assertContains(response, 'Create new Author')
