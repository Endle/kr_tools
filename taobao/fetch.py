# -*- coding: utf-8 -*-
import urllib.request
import re
from time import clock as now
import json

def trace(s:str):
    print(s)

class ItemData(object):
    '''返回单件商品的信息
    '''
    __slots__ = (
        "name", #商品名称
        "price"
    )
    def __repr__(self):
        return "%s: pirce %s" % (self.name, self.price)

start = 0

def taobao_item(pid:int):
    pid = str(pid)
    url = r'http://item.taobao.com/item.htm?spm=a217m.7288829.1997547445.4.d2BNzo&id=' + \
        str(pid)
    headers1 = {'GET': '',
                'Host': "item.taobao.com",
                'User-Agent': "Mozilla/5.0 (Windows NT 6.2; rv:29.0) Gecko/20100101 Firefox/29.0",
                'Referer': url}

    req = urllib.request.Request(url, headers=headers1)
    scode = urllib.request.urlopen(req).read().decode('gbk', 'ignore')

    global start
    print("fetch time: " + str(now()-start))

    trace(scode)

    name = None
    #name = re.search(r'<h3.*?data-title="(.*?)">\n?.*?\n?</h3>', scode).group(1)
    price = re.search(r'<em.*?class="tb-rmb-num">(.*?)</em>', scode).group(1)

    url = r'http://count.tbcdn.cn/counter3?keys=SM_368_sm-357839261,ICE_3_feedcount-%s,SM_368_dsr-357839261&callback=DT.mods.SKU.CountCenter.setReviewCount ' % (
        str(pid))
    req = urllib.request.Request(url, headers=headers1)
    scode = urllib.request.urlopen(req).read().decode('utf-8', 'ignore')
    try:
        pinglunshu = re.search(pid + r'":(\d*?),', scode).group(1)
    except:
        pinglunshu = '0'
    pingfen = re.search(r'SM_368_sm-.*?":(.*?),', scode).group(1)
    url = r'http://mdskip.taobao.com/core/initItemDetail.htm?cartEnable=false&callback=setMdskip&itemId=' + \
        str(pid)
    headers1 = {'GET': '',
                'Host': "mdskip.taobao.com",
                'User-Agent': "Mozilla/5.0 (Windows NT 6.2; rv:29.0) Gecko/20100101 Firefox/29.0",
                'Referer': 'http://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.12.UpuePQ&is_b=1&id=' + str(pid)}
    req = urllib.request.Request(url, headers=headers1)
    scode = urllib.request.urlopen(req).read().decode('utf-8', 'ignore')
    setcount = re.search(r'sellCount":(.*?)}', scode).group(1)
    kucun = re.search(r'"icTotalQuantity":(.*?),"', scode).group(1)
    # 返回价格、评论数、评分、月销量、总库存
    #return (pid, name, price, pinglunshu, pingfen, setcount, kucun)
    ret = ItemData()
    ret.name = name
    ret.price = price
    return ret

# 测试淘宝 Demo

if __name__ == "__main__":
    print('商品ID、价格、评论数、评分、月销量、总库存:')
    start = now()
    print(*gettao(42311048781))
    finish = now()
    tt = finish - start

    print('本次淘宝爬虫执行时间约为：', round(tt, 2), 's\n')

