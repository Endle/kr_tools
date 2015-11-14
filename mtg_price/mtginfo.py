from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
from mtg_price.models import Card_EN, Card_CN
from django.core.exceptions import ObjectDoesNotExist
import browser
import logging
logger = logging.getLogger(__name__)

def _nameCN_to_nameEN_slow(nameCN:str) -> str:
    url = "http://magiccards.info/query?q=!" + urllib.parse.quote(nameCN) + "&v=card&s=cname"
    logger.warn("Fetching MTG Info: %s" % url)
    code = browser.fetch(url)
    soup = BeautifulSoup(code, "lxml")
    not_found = soup.find_all(text="没有匹配的结果")
    if len(not_found) > 0:
        raise ValueError("MTG Info 没有匹配的结果")

    product = soup.find_all('td', class_='TCGPProductName')
    assert len(product) == 1
    return product[0].string

def nameCN_to_nameEN(nameCN:str) -> str:
    logger.warn("Translate card %s" % nameCN)
    try:
        card_cn = Card_CN.objects.get(cn=nameCN)
        result = card_cn.en.name
        logger.warn("Found %s in Django database" % result)
    except ObjectDoesNotExist:
        logger.warn("%s not found in previous database" % nameCN)
        result = _nameCN_to_nameEN_slow(nameCN)

        card_en = Card_EN.objects.create(name=result)
        card_cn = Card_CN.objects.create(en=card_en,cn=nameCN)
    return result

