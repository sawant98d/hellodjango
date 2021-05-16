from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def showResult(request):
    s = "<h1>This is show RESULT page</h1>"
    return HttpResponse(s)

def showTest(request):
    #s = "<h1>This is show TEST page</h1>"
    #res = render(request, 'exam/test.htm')
    que = "Where is Mumbai?"
    a = "Andra Pradesh"
    b =  "Gujrat"
    c = "Maharashtra"
    d = "Rajastan"
    e = "KARNATAKA"
    data = {'que':que, 'a':a, 'b':b, 'c':c, 'd':d, 
    'e':e}
    res = render(request, 'exam/test.htm', context=data)
    return res