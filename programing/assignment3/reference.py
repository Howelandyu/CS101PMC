def changeMe(myList):
    """This changes a passed list into this function"""
    myList.append([1,2,3,4])
    print("Values inside the function: ",myList)
    return

myList=[10,20,30]
changeMe(myList)
print("Values outside the function: ",myList)