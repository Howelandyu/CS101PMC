fibonaci={1:0,2:1}
nextFibonaciKey=3
while len(fibonaci) < 15:
    fibonaci[nextFibonaciKey]=(fibonaci[nextFibonaciKey-1] + fibonaci[nextFibonaciKey-2])
    nextFibonaciKey+=1
print(fibonaci)
print(fibonaci[12])