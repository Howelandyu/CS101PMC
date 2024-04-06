TemperatureC=float(input("What temperature today?"))
TemperatureF=9/5*TemperatureC+32
if TemperatureC>212:
    print("It is steaming hot!")
else:
    print(TemperatureF,"F")