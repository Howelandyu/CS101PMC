list=[5, 1, 2, 3, 5, 4, 6, 5, 7, 8, 9, 5, 5, 5]
searchFor=5
preiousPosition=list.index(searchFor)
print(preiousPosition)
for repitions in range(1, list.count(searchFor)):
    thisPosition=list.index(searchFor, preiousPosition + 1)
    print(thisPosition)
    preiousPosition=thisPosition
