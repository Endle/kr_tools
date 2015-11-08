from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
from selenium import webdriver

def nameCN_to_nameEN(nameCN:str) -> str:
    url = "http://magiccards.info/query?q=" + urllib.parse.quote(nameCN) + "&v=card&s=cname"
    header = {'GET': '',
                'User-Agent': "Mozilla/5.0 (Windows NT 6.2; rv:29.0) Gecko/20100101 Firefox/29.0",
                'Referer': "http://magiccards.info/",
            'Host': "magiccards.info",
    }

    driver = webdriver.Firefox()
    #driver.implicitly_wait(10)
    driver.get(url)
    code = driver.page_source
    #print(driver.page_source)
    driver.close()
    #req = urllib.request.Request(url, headers=header)
    #response = urllib.request.urlopen(req)
    #code = response.read()
    #print(code)
    soup = BeautifulSoup(code)
    ##print(soup.find_all('img', {'alt':'English'}, class_='flag2'))
    print(soup.find_all('div'))#, id='TCGPlayerPricingContainer'))
    ##print(soup.find_all(['br','u','b']))
    ##print(soup.find_all(text=re.compile("语言:")))

if __name__ == "__main__":
    nameCN_to_nameEN("塔莫耶夫")

