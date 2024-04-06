__author__ = "Arana Fireheart"

from urllib.request import urlopen
from re import search, sub
from bs4 import BeautifulSoup
# html = urlopen("https://nccd.cdc.gov/NPAO_DTM/LocationSummary.aspx?statecode=94")
# html = urlopen("http://data.html")
with open("data.html", 'r') as dataFile:
    bsObj = BeautifulSoup(dataFile, "lxml")

print(bsObj.find("tr", {"class":"RepeaterItemLev2"}).find("th").text)
for entry in bsObj.findAll("tr", {"class":"RepeaterItemLev3"}):
    itemToPrint = entry.text.strip().replace('\n', '')
    itemToPrint = sub(r'\t+', '\t', itemToPrint)
    dataItems = itemToPrint.split('\t')
    print(dataItems)
pass