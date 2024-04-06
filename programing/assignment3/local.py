total=0

def sum(arg1,arg2):
    total=arg1+arg2
    print("inside the funtion local total: ",total)
    return total

sum(10,20);
print("Outside the funtion global total: ",total)
