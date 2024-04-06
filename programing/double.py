# from random import randint
# luckyNumber=randint(1,10)
# guessNumber=1
# print(luckyNumber)
# while guessNumber<=5:
#     guess=int(input("What is your number?"))
#     if guess ==luckyNumber:
#         print("Hooray!")
#         break
#     guessNumber+=1
#
# if guessNumber>=6:
#     print("Better lucky next time.")
#
def double(numberToDouble):
    '''Reture tiwce the value of the number passed'''
    doubleToDouble=numberToDouble*2
    return doubleToDouble

answer=double(13)
print(answer)
print(double(12.3))
print(double(-12.3))
print("Hello")
print(double([1,2,3]))

# from math import pi
#
# def areaCircle(radius):
#     area=pi *radius**2
#     return area
#
# print(areaCircle(3))
# print(areaCircle(4))
# print(areaCircle(5))

# def surfaceArea(height,width,depth):
#     frontArea=height*width
#     topArea=width*depth
#     sideArea=height*depth
#
#     calculatedSurfaceArea=(frontArea+topArea+sideArea)*2
#     return calculatedSurfaceArea
#
# print(surfaceArea(2,3,5))