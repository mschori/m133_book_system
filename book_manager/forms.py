from django import forms
from .models import Author, Book


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.is_update = kwargs.pop('is_update')
        super(BookForm, self).__init__(*args, **kwargs)

    def clean_isbn(self):
        if self.is_update:
            return self.cleaned_data['isbn']
        else:
            if Book.objects.filter(pk=self.cleaned_data['isbn']).exists():
                raise forms.ValidationError('This isbn is alread in use.')
