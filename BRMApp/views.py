from django.forms import models
from django.http.response import HttpResponse
from BRMApp.forms import NewBookForm
from django.shortcuts import render
from BRMApp.forms import NewBookForm
from django.http import HttpResponse
from BRMApp import models

# Create your views here.

def viewBooks(request):
    books = models.Book.objects.all()
    res = render(request, 'BRMApp/view_book.htm', {'books':books})
    return res


def newBook(request):
    form = NewBookForm()
    res = render(request, 'BRMApp/new_book.htm',{'form':form})
    return res

def add(request):
    if request.method == 'POST':
        form = NewBookForm(request.POST)
        book = models.Book()
        book.title = form.data['title']
        book.price = form.data['price']
        book.auther = form.data['auther']
        book.publisher = form.data['publisher']
        book.save()
    s = "Record stored <br> <a href='/BRMApp/view-books'>View all books</a>"
    return HttpResponse(s)
