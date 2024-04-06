# import string
# with(open('CYpher','r')) as Cypher:
#     heading=string.Cypher.readline( )
#     print(heading)
#     output=' '
#     for char in heading:
#         output+=heading(char)


# #2
# charCount={ }
# with open('challange3','r') as textfile:
#     text=textfile.readlines()
#     for line in text:
#         for character in line.rstrip():
#             if character in charCount:
#                 charCount[character]+=1
#             else:
#                 charCount[character]=1
# charList=[ ]
# for key in charCount.keys( ):
#     if charCount[key]==1:
#         charList.append(key)
# with open('challange3','r') as textfile:
#     text=textfile.readlines( )
#     for line in text:
#         for character in line.rstrip():
#             if character in charList:
#                 print(character)

# from re import search
# fullText=" "
# charCount={ }
# with open('challange3','r') as textfile:
#     text=textfile.readlines()
#     for line in text:
#         fullText+=line.rstrip( )
# parttern=compile(r'[a-z]{1}')
# match=search("[A-Z]{3}",fullText)
# if match:
#     print("got it!")
# pass




