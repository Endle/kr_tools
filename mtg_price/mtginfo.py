from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
from selenium import webdriver
from mtg_price.models import Card_EN, Card_CN
from django.core.exceptions import ObjectDoesNotExist

def _nameCN_to_nameEN_slow(nameCN:str) -> str:
    url = "http://magiccards.info/query?q=" + urllib.parse.quote(nameCN) + "&v=card&s=cname"
    header = {'GET': '',
                'User-Agent': "Mozilla/5.0 (Windows NT 6.2; rv:29.0) Gecko/20100101 Firefox/29.0",
                'Referer': "http://magiccards.info/",
            'Host': "magiccards.info",
    }

    driver = webdriver.PhantomJS()
    driver.get(url)
    code = driver.page_source
    driver.close()
    soup = BeautifulSoup(code, "lxml")
    product = soup.find_all('td', class_='TCGPProductName')
    assert len(product) == 1
    return product[0].string

def nameCN_to_nameEN(nameCN:str) -> str:
    try:
        card_cn = Card_CN.objects.get(cn=nameCN)
        print(card_cn)
        result = card_cn.en.name
    except ObjectDoesNotExist:
        result = _nameCN_to_nameEN_slow(nameCN)

        card_en = Card_EN.objects.create(name=result)
        card_cn = Card_CN.objects.create(en=card_en,cn=nameCN)
    return result

if __name__ == "__main__":
    result = nameCN_to_nameEN("塔莫耶夫")
    print(result)

