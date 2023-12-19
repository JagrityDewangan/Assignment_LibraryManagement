# Importing required libraries 
from django.urls import path
from . import views
urlpatterns = [
    path('books/',views.book_list, name='book_list'),
    path('borrow/', views.borrow_book, name='borrow_book'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('return/<int:borrow_id>/',views.return_book, name='return_book'),
]
