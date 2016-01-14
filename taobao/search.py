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
    item = ItemData()
    #col2 = bs_item.find_all("div", class="col-2")
    #print(col2)
    print("---------------")
    #col3 = bs_item.fetch
    print("=============")
    return item

def search(name:str)->str:
    url = _get_url(name)
    #code = browser.fetch(url)
    #with open("/dev/shm/page.html", 'w') as fout:
        #fout.write(code)
    code = open("/dev/shm/page.html").read()
    soup = BeautifulSoup(code, "lxml")
    item_list = soup.find_all('div', class_='list')
    assert type(item_list) is element.ResultSet
    assert len(item_list) == 1
    redundancy_child = item_list[0].div.contents #<div class="items g-clearfix">
    with open("/dev/shm/result.html", "w") as fout:
        fout.write(str(redundancy_child))

    item_list = [] # list of ItemData
    for item in redundancy_child:
        if str(item).strip() == "":
            continue
        item_list.append(_solve_item(item))
    print(item_list)
    return(str(redundancy_child))



if __name__ == '__main__':
    ret = search("众神之怒 万智牌")
    print(ret)
