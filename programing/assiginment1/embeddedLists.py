 products=[["Milk",1.95,3],["Bread",3.59,2],["Egg",1.98,1],["Cookies",1.95,10]]
costOfGroceries=0
for innerList in products:
    print(innerList)
    print("Please buy %i containers of %s costing $%5.2f" %(innerList[2],innerList[0],innerList[1]*innerList[2]))
    costOfGroceries=costOfGroceries+innerList[1]*innerList[2]
print("The total you will need is: $%5.2f" %costOfGroceries)