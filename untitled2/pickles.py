from pickle import load, dump
from os import path,walk

# localDirectory=path.expanduser('~')
# startingFolderName=path.join(localDirectory,'Doweload')
# # same as=startingFolderName=localDirectory+'\Doweload'
# # print(startingFolderName)


localDirectory = path.expanduser('~')
startingFolderName = path.join(localDirectory, 'Downloads')
# same as=startingFolderName=localDirectory+'\Doweload'
# print(startingFolderName)
directoryList=[ ]
writingList=[ ]
if path.exists(startingFolderName):
    for root, directories, files in walk(startingFolderName):
        directoryList.append(list((root, files)))
    for items in directoryList:
        print(items)

pickleFilename='checkFileLIst.pl'
with open(path.join(localDirectory,pickleFilename), 'wb')as pickleFileHandle:
      dump(directoryList,pickleFileHandle)
with open(path.join(localDirectory,pickleFilename),'rb')as pickleFileHandle:
    newList = load(pickleFileHandle)
pass