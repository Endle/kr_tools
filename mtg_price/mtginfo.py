from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
from selenium import webdriver

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
    result = _nameCN_to_nameEN_slow(nameCN)
    return result

if __name__ == "__main__":
    result = nameCN_to_nameEN("塔莫耶夫")
    print(result)

