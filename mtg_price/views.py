from django.shortcuts import render
from django.http import HttpResponse
from mtg_price.mtginfo import nameCN_to_nameEN

# Create your views here.

def solve(content):
    if 'chinese' in content:
        try:
            content['english'] = nameCN_to_nameEN(content['chinese'].strip())
        except ValueError:
            content['result'] = "No such Card!"
            return
        content['result'] = "English name: " + content['english']
        content['result'] += " Chinese name: " + content['chinese']

def home(request):
    if request.method == 'GET':
        content = {}
        content["result"] = "Hello"
        solve_flag = False
        getter = request.GET.dict()
        if 'name' in getter and getter['name']:
            content["english"] = getter['name']
            solve_flag = True
        if 'name_cn' in getter and getter['name_cn']:
            content["chinese"] = getter['name_cn']
            solve_flag = True
        if solve_flag:
            solve(content)
        return render(request, "base.html", content)
