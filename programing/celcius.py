def tempConvert(temperature, scale='c',result='f'):
    try:
     if scale=='c':
        fahrenheit=(temperature*9/5)+32
        celcius=temperature
        kelvin=celcius-273.16
     elif scale=='f':
        fahrenheit = temperature
        celcius = (temperature-32)*5/9
        kelvin = celcius - 273.16
     elif scale=='k':
        fahrenheit = (temperature * 9 / 5) + 32
        celcius = temperature-273.16
        kelvin = temperature
     else:
        print("no valid")
        return None
    except TypeError:
        print("% not valid, try again.")




    if result==None:
        if scale=='c':
            return fahrenheit
        elif scale=='f':
            return celcius
        elif scale=='k':
            return None
    if result=='f':
         return fahrenheit
    elif result=='c':
         return celcius
    elif result=='k':
        return kelvin
    else:
        print("no Valid result")
        return None


print(tempConvert(27))
print(tempConvert(27,'f','c'))
print(tempConvert(27,'c'))

