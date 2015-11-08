from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import re

def nameCN_to_nameEN(nameCN:str) -> str:
    url = "http://magiccards.info/query?q=" + urllib.parse.quote(nameCN) + "&v=card&s=cname"
    header = {'GET': '',
                'User-Agent': "Mozilla/5.0 (Windows NT 6.2; rv:29.0) Gecko/20100101 Firefox/29.0",
                'Referer': "http://magiccards.info/",
            'Host': "magiccards.info",
#User-Agent: Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0
            #'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            #'Accept-Language': "en-US,en;q=0.5",
            #'Accept-Encoding': "gzip, deflate",
#DNT: 1
#Referer: http://magiccards.info/query?q=%E5%A1%94%E8%8E%AB%E8%80%B6%E5%A4%AB&v=spoiler&s=cname
#Cookie: __utma=21835108.906431547.1446964839.1446968177.1446970136.3; __utmc=21835108; __utmz=21835108.1446964839.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); lang=cn; __utmb=21835108.7.10.1446970136; __utmt=1
#Connection: keep-alive
#Cache-Control: max-age=0
    }
    req = urllib.request.Request(url, headers=header)
    response = urllib.request.urlopen(req)
    #code = response.read().decode('utf-8')
    code = response.read()
    print(code)
    soup = BeautifulSoup(code)
    #print(soup.find_all('img', {'alt':'English'}, class_='flag2'))
    print(soup.find_all('div'))#, id='TCGPlayerPricingContainer'))
    #print(soup.find_all(['br','u','b']))
    #print(soup.find_all(text=re.compile("语言:")))

if __name__ == "__main__":
    nameCN_to_nameEN("塔莫耶夫")

