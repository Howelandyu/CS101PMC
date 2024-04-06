name="Pine Manor College"
new=[]
newString=""
for position in range(len(name)-1,-1,-1):
    new.append(name[position])
    # newString=newString+name[position]
    newString+=name[position]
print(new)
print(newString)