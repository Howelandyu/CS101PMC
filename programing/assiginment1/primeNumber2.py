primeNumberFoundCount=1
testNumber=3
print("2")
while primeNumberFoundCount<12:
    if testNumber%2==1:    #Check for odd number
        foundEvenDivisor=False
        for number in range(3,testNumber):
            if testNumber%number==0:
                testNumber+=1   #Found an even divisor
                # break
        print(testNumber)       #Found an prime number
        testNumber+=1           #Move on to the next testNumber
        primeNumberFoundCount+=1
    else:
        testNumber+=1