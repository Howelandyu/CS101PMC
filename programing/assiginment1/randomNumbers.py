from random import randint
quantityOfNumbers=int(input("How many numbers do you want: "))
for number in range(0,quantityOfNumbers):
    print("Random number %i:%i" %(number,randint(10,100)))