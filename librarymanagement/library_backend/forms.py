# Importing required modules
from django import forms
from .models import BorrowBook, Book, User

# This class is for Borrow book form
class BorrowBookForm(forms.ModelForm):
    class Meta: 
        model = BorrowBook
        fields =  ['user', 'book', 'borrow_date']
        def __init__(self, *args, **kwargs) :
            super().__init__(*args,**kwargs)
    book = forms.ChoiceField(choices=[(book.id, book.title) for book in Book.objects.all()])
    user = forms.ChoiceField(choices=[(user.id, user.email) for user in User.objects.all()])

# This class is for showing return date
class ReturnBookForm(forms.ModelForm):
    class Meta:
        model = BorrowBook
        fields = ['return_date']