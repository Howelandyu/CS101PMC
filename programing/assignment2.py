# Number1=float(input("Type the first number" ))
# Number2=float(input("Type the second number"))
# Number3=float(input("Type the third number"))
# average=Number1+Number2+Number3
# print(average/3)

# TemperatureC=float(input("What temperature today?"))
# TemperatureF=9/5*TemperatureC+32
# if TemperatureC>212:
#     print("It is steaming hot!")
# else:
#     print(TemperatureF,"F")

# divisor=1
# while divisor<= 10:
#     print("%a times 7 = %a" % (divisor,divisor*7))
#     divisor+=1

# babyswan=int(input("How many chicks did they have?"))
# for number in range(0,babyswan+1):
#         print("The family comprises %i kgs.of swans with %i babies"% (13+number*1.5,number))

# number=1
# while number in range(1,10):
#     print("i=",number)
#     number+=1

# animals=["tiger","elephent","monkey"]
# for zoo in animals:
#     print(zoo)

# question=(input("Do you like Python?"))
# if question==("yes"):
#     print("That is great!")
# else:
#     print("That is disapointing.")

# question=(input("Do you like Python?"))
# if question==("yes"):
#     print("That is great!")
# elif question==("no"):
#     print("That is disapointing.")
# else:
#     print("That is disapointing.")


import random
counter=1
Numberanswer=random.randint(1,11)
while counter<=5:
    Numberguess=int(input("Please guess a number"))
    counter+= 1
    if Numberguess ==Numberanswer:
        print("Hooray!")
        break
if counter>5:
        print("Better luck next time")





