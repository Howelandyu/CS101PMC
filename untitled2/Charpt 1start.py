# from urllib.request import urlopen
# html=urlopen('http://www.pythonscraping.com/pages/page1.html')
# pageText=html.read( ).decode('UTF8')
# print(pageText)

from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen('http://www.pythonscraping.com/pages/page1.html')
bsObj=BeautifulSoup(html.read( ),"lxml")
print(bsObj.h1)