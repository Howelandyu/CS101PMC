print("Multiplication Tables:")
for tableNumber in range(1,11):      # Outer Loop
    print("\n%i's Table:" % tableNumber)
    for multiplier in range(1,11):    #Inner Loop
        print("%i times %i=%i" %(tableNumber,multiplier,tableNumber* multiplier))