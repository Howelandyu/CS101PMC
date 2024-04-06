import urllib.request
wed=urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345')
html=wed.read()
print(html)
for 



