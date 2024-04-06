from re import sub
from urllib.request import urlopen
from bs4 import BeautifulSoup
# html = urlopen('http://www.google.com')
html = urlopen('https://www.cpubenchmark.net/cpu_list.php')
bsObj=BeautifulSoup(html,"lxml")
performanceData=[ ]
for sibling in bsObj.find("table", {"id": "cputable"}).tbody.tr.next_siblings:
     if sibling !='\n':
         rowDataLIst=list(sibling.findAll('td'))
         cpuData=[ ]
         for item in rowDataLIst:
             cpuData.append(item.text)
         performanceData.append(cpuData)
         print(cpuData)