
# fibonaci=[0,1]
# Listength=2
# while len(fibonaci) < 35:
#     fibonaci.append(fibonaci[-1] + fibonaci[-2])
#     Listength+=1
# print(fibonaci)
#
#
# for count in range(0,33):
#     fibonaci.append(fibonaci[-1] + fibonaci[-2])
#     print(fibonaci)

fibonaci = [0, 1]
while len(fibonaci) < 35:
    fibonaci.append(fibonaci[-1] + fibonaci[-2])
    print(fibonaci)

fibonaci = [0, 1]
for count in range(0, 33):
    fibonaci.append(fibonaci[-1] + fibonaci[-2])
    print(fibonaci)

fibonaci = [0, 1]
listlength = 2
while listlength < 35:
    fibonaci.append(fibonaci[-1] + fibonaci[-2])
    listlength +=1
    print(fibonaci)