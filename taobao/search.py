if __name__ == '__main__':
    import sys
    sys.path.append("../")

import urllib.parse
import browser
import time
from bs4 import BeautifulSoup
from bs4 import element
from taobao.fetch import ItemData


def _get_url(name:str)->str:
    url_component = [
        "https://s.taobao.com/search",
        "?q=",
        urllib.parse.quote_plus(name),
        "&imgfile=&js=1&stats_click=search_radio_all%3A1",
        "&initiative_id=staobaoz_",
        time.strftime("%Y%m%d"),
        "&ie=utf8&style=list",
    ]
    return "".join(url_component)

def _solve_item(bs_item) -> ItemData:
    assert type(bs_item) is element.Tag
    assert list(bs_item["class"]) == ['item', 'g-clearfix']
    item = ItemData()
    col2 = col3 = None
    for i in bs_item.contents:
        if type(i) == element.NavigableString: continue
        if list(i["class"]) == ["col", "col-2"]: col2 = i
        if list(i["class"]) == ["col", "col-3"]: col3 = i
    assert col2 != None
    assert col3 != None

    assert type(col2) is element.Tag
    a = col2.a
    assert type(a) is element.Tag
    assert a["class"] == ["J_ClickStat"]
    item.link = "http:" + a["href"] # Hacky, 不明白为何需要加前缀
    item.name = "".join(a.stripped_strings)

    redundancy_div = col3.div
    price_span = redundancy_div.span
    assert price_span["class"] == ["price", "g_price", "g_price-highlight"]
    item.price = float(price_span.strong.string)
    shipping_div = None
    for i in col3.contents:
        if type(i) == element.NavigableString: continue
        try:
            if list(i["class"]) == ["ship"]: shipping_div = i
        except KeyError:
            continue
    if shipping_div != None:
        shipping_price = shipping_div.string.split()[-1]
    else:
        shipping_price = 0.0 #包邮
    item.shipping_cost = float(shipping_price)

    return item

def search(name:str)->[ItemData]:
    url = _get_url(name)
    code = browser.fetch(url)
    soup = BeautifulSoup(code, "lxml")
    item_list = soup.find_all('div', class_='list')
    assert type(item_list) is element.ResultSet
    assert len(item_list) == 1
    redundancy_child = item_list[0].div.contents #<div class="items g-clearfix">

    item_list = [] # list of ItemData
    for item in redundancy_child:
        if str(item).strip() == "":
            continue
        item_list.append(_solve_item(item))
    return(str(redundancy_child))

if __name__ == '__main__':
    ret = search("众神之怒 万智牌")
    print(ret)
