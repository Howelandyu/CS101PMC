# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# html=urlopen('http://www.pythonscraping.com/pages/page1.html')
# bsObj=BeautifulSoup(html.read( ),"lxml")
# print(bsObj.h1)



from urllib.request import urlopen
from bs4 import BeautifulSoup
from html.parser import HTMLParser
def strip_tags(htmlWed):
    htmlWed = htmlWed.strip()
    htmlWed = htmlWed.strip("\n")
    result = []
    chara = HTMLParser()
    chara.handle_data = result.append
    chara.feed(htmlWed)
    chara.close()
    return "".join(result)
html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bsObj=BeautifulSoup(html.read( ),"lxml")
headingsList  = bsObj.findAll("h1")
for heading in headingsList:
    print(heading.get_text())
pass