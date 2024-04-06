# try:
#     variable="hello"/12
# except TypeError:
#     print("That doesn't make any sense!")


# with open("sqCubeTable.txt","w") as outputFile:
#     for x in range(1,11):
#         outputFile.write(repr(x),rjust(2),repr(x*x),rjust(3))
#         print(repr(x),rjust(2),repr(x*x),rjust(3),end='')
#         outputFile.write(repr(x*x*x),rjust(5)+'\n')
#           print(repr(x*x*x).rjust(4))


# fruitDictionary= {}
# with open("fruitColors.txt","r")as outputFile:
#     for line in outputFile:
#         fruitName, fruitColor = line[:-1].split(' ')
#         fruitDictionary[fruitName]=fruitColor
# print(fruitDictionary)

print('banana'.split("a"))