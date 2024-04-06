def fahrenheit(celsius):
    """return the temperature in degrees Fahrenheit"""
    return(celsius*9/5)+32

for t in (22.6,25.8,27.3,29.8,-40.0,0.0,100.0):
    print(t,":",fahrenheit(t))