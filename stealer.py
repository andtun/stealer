from bs4 import BeautifulSoup
import requests
import html5lib

PGNUM = 733
OUTPUT_NAME = "atlant-44.txt"
BOOK_URL = "http://litbook.net/book/17195/atlant-raspravil-plechi-trilogiya/page-%s/"


pgnum = PGNUM + 1
f = open(OUTPUT_NAME, 'w', encoding="utf-8")

for i in range(1,pgnum):
    url = BOOK_URL % i
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html5lib")
    
    allps = soup.find('div', {"class": "clear", "id": "book"})
    plist = allps.findAll("p")
    for p in plist:
        pa = BeautifulSoup(str(p)).text
        f.write(pa)
    print("Done", str(i)+"/"+str(PGNUM), "OR", str(int(i/PGNUM*100))+"%%")
    

f.close()
