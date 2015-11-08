from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    if request.method == 'GET':
        content = {}
        content["result"] = "Hello"
        getter = request.GET.dict()
        if getter['name']:
            content["result"] = "English name: " + getter['name']
        if getter['name_cn']:
            content['result'] += " Chinese name: " + getter['name_cn']
        return render(request, "base.html", content)