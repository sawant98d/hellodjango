from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def greeting(request):
    s = "<h1>Hello and welcome to the first view of testapp</h1>"
    return HttpResponse(s)
