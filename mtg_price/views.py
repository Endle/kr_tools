from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def template():
    fin = open("home.html")
    html = fin.read()
    fin.close()
    return html

def home(request):
    #html = template
    #return HttpResponse("hello")
    return render(request, "base.html")

