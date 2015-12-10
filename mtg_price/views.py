from django.shortcuts import render
from django.http import HttpResponse
import logging
logger = logging.getLogger(__name__)
from mtg_price.mtginfo import *

# Create your views here.

def solve(content):
    if 'chinese' in content and content['chinese'] != "":
        try:
            content['english'] = nameCN_to_nameEN(content['chinese'].strip())
        except ValueError:
            content['result'] = "No such Card: " + content['chinese']
            return
    elif 'english' in content:
        try:
            content['chinese'] = nameEN_to_nameCN(content['english'].strip())
        except ValueError:
            content['result'] = "No such card: " + content['english']
            return
    else:
        raise ValueError("Neither english nor chinese name is found")

    content['result'] = "English name: " + content['english']
    content['result'] += " Chinese name: " + content['chinese']
    content['tcgplayer'] = get_tcg_price(content['chinese'])
    content['taobao'] = get_taobao_price(content['chinese'])

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
            logger.warn("Try to solve")
            solve(content)
        return render(request, "base.html", content)
