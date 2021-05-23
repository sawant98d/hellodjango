from django.forms import models
from django.http.response import HttpResponse, HttpResponseRedirect
from BRMApp.forms import NewBookForm
from django.shortcuts import render
from BRMApp.forms import NewBookForm, SearchForm
from django.http import HttpResponse, HttpResponseRedirect
from BRMApp import models

# Create your views here.

def search(request):
    form = SearchForm(request.POST)
    books = models.Book.objects.filter(title=form.data['title'])
    res = render(request, 'BRMApp/search_book.htm',{'form':form, 'books':books})
    return res


def searchBook(request):
    form = SearchForm()
    res = render(request, 'BRMApp/search_book.htm', {'form':form})
    return res

def deleteBook(request):
    bookid = request.GET['bookid']
    book = models.Book.objects.filter(id=bookid)
    book.delete()
    return   HttpResponseRedirect('/BRMApp/view-books')

def edit(request):
    if request.method == 'POST':
        form = NewBookForm(request.POST)
        book = models.Book()
        book.id = request.POST['bookid']
        book.title = request.data['title']
        book.price = request.data['price']
        book.author = request.data['author']
        book.publisher = request.data['publisher']
        book.save()
    return HttpResponseRedirect('BRMApp/view-books')


def editBook(request):
    book = models.Book.objects.get(id=request.GET['bookid'])
    fields = {'title':book.title, 'price':book.price, 'author':book.author, 'publisher':book.publisher}
    form = NewBookForm(initial=fields)
    res = render(request, 'BRMApp/edit_book.htm',{'form':form, 'book':book})
    return res

def viewBooks(request):
    books = models.Book.objects.all()
    res = render(request, 'BRMApp/view_books.htm', {'books':books})
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
