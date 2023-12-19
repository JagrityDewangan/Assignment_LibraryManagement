from django.contrib import admin
from .models import Book, BorrowBook, User
myModels = [Book, BorrowBook, User]
admin.site.register(myModels)