from bs4 import BeautifulSoup
import urllib.request
import urllib.parse

def nameCN_to_nameEN(nameCN:str) -> str:
    url = "http://magiccards.info/query?q=" + urllib.parse.quote(nameCN) + "&v=card&s=cname"
    response = urllib.request.urlopen(url)
    print(response.decode())
    soup = BeautifulSoup(response)
    #print(soup.find_all('img', {'alt':'English'}, class_='flag2'))
    print(soup.find_all('div'))

if __name__ == "__main__":
    nameCN_to_nameEN("塔莫耶夫")

