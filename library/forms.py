from django import forms
from .models import *
from authentication.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError


class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ('image_url','title','author','category')
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(BookForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        book = super().save(commit=False)
        category_obj,created = Category.objects.get_or_create(category=book.category)
        print(self.request.__dir__())
        #book.created_by_user_id = self.request.user
        book.category_id = category_obj

        if commit:
            book.save()
        return book