primeNumberFoundCount=1
testNumber=3
print("2")
while primeNumberFoundCount<12:
    if testNumber %2==1:     #Check for odd number
        numberIsPrime=True
        for number in range(3,testNumber):
           if testNumber % number==0:
               testNumber+=1      #Found an even divisor
               numberIsPrime=False
               break
        if numberIsPrime==True:
            print(testNumber)     #Found a prime number
            testNumber+=1         #Move on to the next testNumber
            primeNumberFoundCount+=1
    else:
        testNumber+=1