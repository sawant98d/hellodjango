from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def showResult(request):
    s = "<h1>This is show RESULT page</h1>"
    return HttpResponse(s)

def showTest(request):
    #s = "<h1>This is show TEST page</h1>"
    res = render(request, 'exam/test.htm')
    return res