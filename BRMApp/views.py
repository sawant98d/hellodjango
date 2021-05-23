from django.contrib import auth
from django.forms import models
from django.http.response import HttpResponse, HttpResponseRedirect
from BRMApp.forms import NewBookForm
from django.shortcuts import render
from BRMApp.forms import NewBookForm, SearchForm
from django.http import HttpResponse, HttpResponseRedirect
from BRMApp import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



# Create your views here.



def userLogin(request):
    data = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            request.session['username'] = username
            return HttpResponseRedirect('/BRMApp/view-books/')
        else:
            data['error']='Username or password is incorrect'
            res = render(request, 'BRMApp/user_login.htm', data)
            return res
    else:
        return render(request, 'BRMApp/user_login.htm', data)

def userLogout(request):
    logout(request)
    return HttpResponseRedirect('/BRMApp/login/')

@login_required(login_url='/BRMApp/login/')
def search(request):
    form = SearchForm(request.POST)
    books = models.Book.objects.filter(title=form.data['title'])
    res = render(request, 'BRMApp/search_book.htm',{'form':form, 'books':books})
    return res

@login_required(login_url='/BRMApp/login/')
def searchBook(request):
    form = SearchForm()
    res = render(request, 'BRMApp/search_book.htm', {'form':form})
    return res


@login_required(login_url='/BRMApp/login/')
def deleteBook(request):
    bookid = request.GET['bookid']
    book = models.Book.objects.filter(id=bookid)
    book.delete()
    return   HttpResponseRedirect('/BRMApp/view-books')

@login_required(login_url='/BRMApp/login/')
def edit(request):
    if request.method == 'POST':
        form = NewBookForm(request.POST)
        book = models.Book()
        book.id = request.POST['bookid']
        book.title = form.data['title']
        book.price = form.data['price']
        book.author = form.data['author']
        book.publisher = form.data['publisher']
        book.save()
    return HttpResponseRedirect('BRMApp/view-books')

@login_required(login_url='/BRMApp/login/')
def editBook(request):
    book = models.Book.objects.get(id=request.GET['bookid'])
    fields = {'title':book.title, 'price':book.price, 'author':book.author, 'publisher':book.publisher}
    form = NewBookForm(initial=fields)
    res = render(request, 'BRMApp/edit_book.htm',{'form':form, 'book':book})
    return res

@login_required(login_url='/BRMApp/login/')
def viewBooks(request):
    books = models.Book.objects.all()
    username = request.session['username']
    res = render(request, 'BRMApp/view_books.htm', {'books':books,'username':username})
    return res

@login_required(login_url='/BRMApp/login/')
def newBook(request):
    form = NewBookForm()
    res = render(request, 'BRMApp/new_book.htm',{'form':form})
    return res

@login_required(login_url='/BRMApp/login/')
def add(request):
    if request.method == 'POST':
        form = NewBookForm(request.POST)
        book = models.Book()
        book.title = form.data['title']
        book.price = form.data['price']
        book.author = form.data['author']
        book.publisher = form.data['publisher']
        book.save()
    s = "Record stored <br> <a href='/BRMApp/view-books'>View all books</a>"
    return HttpResponse(s)
