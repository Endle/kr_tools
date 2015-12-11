if __name__ == '__main__':
    import sys
    sys.path.append("../")

import urllib.parse
import browser
import time
from bs4 import BeautifulSoup


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

def search(name:str)->str:
    url = _get_url(name)
    code = browser.fetch(url)
    with open("/dev/shm/page.html", 'w') as fout:
        fout.write(code)
    return "stub html"
    soup = BeautifulSoup(code, "lxml")
    #item_list = soup.find_all('div', class_='list')
    #print(item_list)



if __name__ == '__main__':
    ret = search("众神之怒 万智牌")
    print(ret)
