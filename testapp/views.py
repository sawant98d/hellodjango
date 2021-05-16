from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def greeting(request):
    s = "<h1>Hello and welcome to the first view of testapp</h1>"
    return HttpResponse(s)

def showContact(request):
    s = "<h1>Contact Page</h1>"
    s += "<p>website: abc.com</p>"
    s += "<p>Contact: 987654321</p>"
    s += "<p>Email: abc@gmail.com</p>"
    return HttpResponse(s)

def about(request):
    #s = "<h1>This is an about page</h1>"
    #l = [10,20,30]
    data = {'msg':'this is message from views.py lol for quote filter test purpose'}
    res = render(request, 'testapp/about.htm', data)
    return res