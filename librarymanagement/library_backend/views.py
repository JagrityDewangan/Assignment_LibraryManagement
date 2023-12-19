# Importing required Modules
from django.shortcuts import render,get_object_or_404, redirect
from .models import Book, BorrowBook, User
from .forms import BorrowBookForm, ReturnBookForm

# This function is calling the user view borrow_book 
def borrow_book(request):
    if(request.method) == "POST":
        form = BorrowBookForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data['user']
            user = get_object_or_404(User,id=id)
            borrowed_book = form.save(commit=False)
            borrowed_book.user = user
            borrowed_book.save()
        return redirect('book_detail', pk=borrowed_book.book.pk)
    else:
        form = BorrowBookForm()
    return render(request, 'borrow_book.html', {'form':form})

# This function is calling the user view return_book 
def return_book(request, borrow_id):
    borrowed_book = get_object_or_404(BorrowBook, pk=borrow_id)
    if request.method == "POST":
        form = ReturnBookForm(request.POST, instance=borrowed_book)
        if form.is_valid():
            borrowed_book = form.save(commit= False)
            borrowed_book.return_date = form.cleaned_data['return_date']
            borrowed_book.save()
            return redirect('book_detail',pk= borrowed_book.book.pk)
    else:
        form = ReturnBookForm(instance=borrowed_book)
    return render(request, 'return_book.html',{'form': form})

# This function is for showing borrow book with id
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book':book})

# This function is for listing all the books
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books':books}) 
