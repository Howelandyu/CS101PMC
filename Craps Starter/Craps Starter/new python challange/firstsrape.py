# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# # html=urlopen('https://nccd.cdc.gov/NPAO_DTM/LocationSummary.aspx?statecode=94')
# # html=urlopen('data.html')
# with open('data2.html','rb') as dataFile:
#     bsObj=BeautifulSoup(dataFile,"lxml")
# # bsObj.find("tr",{"class":})
# print(bsObj.find("tr",{"class":"RepeaterItemLev2"}).find("th").text)
# for entry in bsObj.findAll("tr",{"class":"RepeaterItemLev3"}):
#     print(entry.text)
# pass

# from re import sub
# from urllib.request import urlopen
# from bs4 import BeautifulSoup# html=urlopen('https://nccd.cdc.gov/NPAO_DTM/LocationSummary.aspx?statecode=94')
# # html=urlopen('data.html')
# with open('data.html','rb') as dataFile:
#     bsObj=BeautifulSoup(dataFile,"lxml")
# # bsObj.find("tr",{"class":})
# print(bsObj.find("tr",{"class":"RepeaterItemLev2"}).find("th").text)
# for entry in bsObj.findAll("tr",{"class":"RepeaterItemLev3"}):
#     for dataItem in entry.findAll("td"):
#         itemToPrint=entry.text.strip( ).replace('\n',' ')
#         itemToPrint=sub(r'\t+','\t',itemToPrint)
#         dtatItem=itemToPrint.split('\t')
#         print(dataItem)
# pass




# from re import sub
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# html=urlopen('https://www.cpubenchmark.net/cpu_list.php')
# bsObj=BeautifulSoup(html,"lxml")
# for sibling in bsObj.find("table", {"id": "cputable"}).tbody.tr.next_sibilings:
#      currentElement=sibling.tr
#      print(currentElement)
# pass


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
pass

