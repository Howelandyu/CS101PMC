# print("Hellow World!")

# name=input("What is your name?")
# print( )
# print("Hellow %s" % name)

# number=int(input("Give me a number: "))
# print( )
# print("%i time 4=%i" % (number, number* 4))
#
# times=int(input("how many to do? "))
# print("345"* times)
#
# for number in range(0,10):
#     print(number)
#
# for number in range(0,10):
#     print("%i time 2=%i" % (number, number *2))
#
# print("Multiplication Tables:")
# for tableNumber in range(1,11):      # Outer Loop
#     print("\n%i's Table:" % tableNumber)
#     for multiplier in range(1,11):    #Inner Loop
#         print("%i times %i=%i" %(tableNumber,multiplier,tableNumber* multiplier))
#
# carColor='red'
# if carColor=="red":
#     print("I like red sport car!")
# else:
#     print("How boring!")
#
# carColor='red'
# carModel='sport'
# if carColor=="red"and carModel=='sport':
#     print("I like red sports car!")
# elif carColor=='red' and carModel !='sport':
#     print("I like red cars!")
# else:
#     print("How boring!")
#
# from random import randint
# quantityOfNumbers=int(input("How many numbers do you want: "))
# for number in range(0,quantityOfNumbers):
#     print("Random number %i:%i" %(number,randint(10,100)))
#
# name="Pine Manor College"
# new=[]
# newString=""
# for position in range(len(name)-1,-1,-1):
#     new.append(name[position])
#     # newString=newString+name[position]
#     newString+=name[position]
# print(new)
# print(newString)
#
# presidents=['Obama','Bush','Clinton','Bush','Regan','Carter']
# for name in presidents:
#     print("We had a president named President %s" %name)
#
# inputNumbers=[1,10,20,30,40,50,100]
# outputNumbers=[]
# for number in inputNumbers:
#     outputNumbers.append(number** 2)
# print(inputNumbers)
# print(outputNumbers)
# #
# products=[["Milk",1.95,3],["Bread",3.59,2],["Egg",1.98,1],["Cookies",1.95,10]]
# costOfGroceries=0
# for innerList in products:
#  print(innerList)
#  print("Please buy %i containers of %s costing $%5.2f" %(innerList[2],innerList[0],innerList[1]*innerList[2]))
#  costOfGroceries=costOfGroceries+innerList[1]*innerList[2]
# print("The total you will need is: $%5.2f" %costOfGroceries)
#
# primeNumberFoundCount=1
# testNumber=3
# print("2")
# while primeNumberFoundCount<12:
#     if testNumber %2==1:     #Check for odd number
#         numberIsPrime=True
#         for number in range(3,testNumber):
#            if testNumber % number==0:
#                testNumber+=1      #Found an even divisor
#                numberIsPrime=False
#                break
#         if numberIsPrime==True:
#             print(testNumber)     #Found a prime number
#             testNumber+=1         #Move on to the next testNumber
#             primeNumberFoundCount+=1
#     else:
#         testNumber+=1
#
#
# primeNumberFoundCount=1
# testNumber=3
# print("2")
# while primeNumberFoundCount<12:
#     if testNumber%2==1:    #Check for odd number
#         foundEvenDivisor=False
#         for number in range(3,testNumber):
#             if testNumber%number==0:
#                 testNumber+=1   #Found an even divisor
#                 # break
#         print(testNumber)       #Found an prime number
#         testNumber+=1           #Move on to the next testNumber
#         primeNumberFoundCount+=1
#     else:
#         testNumber+=1




