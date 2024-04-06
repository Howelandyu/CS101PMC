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