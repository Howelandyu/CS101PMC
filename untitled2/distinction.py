# highestTemp=0
# highYear=0
# lowestTemp=200
# lowYear=0
# try:
#     with open('testfile.txt','r') as testFileHandle:
#         headings=testFileHandle.readline( ).split('\t')
#         for inputLine in testFileHandle.readlines():
#             month, AverageLow,  AverageHigh, LowRecordYear, HighRecordYear,AveragePrecipitation, AverageSnow=inputLine.strip().split('\t')
#             lowTemp,lowTempYear=LowRecordYear.split( )
#             lowTemp=int(lowTemp[:-1])
#             lowTempYear=int(lowTempYear[1:-1])
#             highTemp,highTempYear=HighRecordYear.split( )
#             highTemp=int(highTemp[:-1])
#             highTempYear = int(highTempYear[1:-1])
#
#
#
#             print("%s\t\t High-Average: %i\t\t Low-Average: %i" % (month,int(AverageHigh[:-1])-highTemp,int(AverageLow[:-1])-lowTemp))
#         print("High %f in %i Low: %f in %i" % (highestTemp,highYear,lowestTemp,lowYear))
# except FileNotFoundError:
#     print("File not found")

# highestTemp = 0
# highYear = 0
# lowestTemp = 200
# lowYear = 0
# try:
#         with open('testfile.txt', 'r') as testFileHandle:
#             with open('deltafile.txt', 'w')as deltafileHandle:
#                 headings = testFileHandle.readline().split('\t')
#                 for inputLine in testFileHandle.readlines():
#                     month, AverageLow, AverageHigh, LowRecordYear, HighRecordYear, AveragePrecipitation, AverageSnow = inputLine.strip().split(
#                     '\t')
#                     lowTemp, lowTempYear = LowRecordYear.split()
#                     lowTemp = int(lowTemp[:-1])
#                     lowTempYear = int(lowTempYear[1:-1])
#                     highTemp, highTempYear = HighRecordYear.split()
#                     highTemp = int(highTemp[:-1])
#                     highTempYear = int(highTempYear[1:-1])
#
#
#                     deltafileHandle.write("%s\t\t High-Average: %i\t\t Low-Average: %i" % (month, int(AverageHigh[:-1]) - highTemp, int(AverageLow[:-1]) - lowTemp))
#
#             # print("High %f in %i Low: %f in %i" % (highestTemp, highYear, lowestTemp, lowYear))
# except FileNotFoundError:
#         print("File not found")





# from os import path
# inputFile='testfile.txt'
# outFile='testfile.txt'
# highestTemp=0
# highYear=0
# lowestTemp=200
# lowYear=0
# try:
#     if path.exists('testfile.txt')and not path.isdir('testfile.txt'):
#         with open('testfile.txt','r') as testFileHandle:
#             with open('deltafile.txt', 'w')as deltafileHandle:
#                 headings=testFileHandle.readline( ).split('\t')
#                 for inputLine in testFileHandle.readlines():
#                     month, AverageLow,  AverageHigh, LowRecordYear, HighRecordYear,AveragePrecipitation, AverageSnow=inputLine.strip().split('\t')
#                     lowTemp,lowTempYear=LowRecordYear.split( )
#                     lowTemp=int(lowTemp[:-1])
#                     lowTempYear=int(lowTempYear[1:-1])
#                     highTemp,highTempYear=HighRecordYear.split( )
#                     highTemp=int(highTemp[:-1])
#                     highTempYear = int(highTempYear[1:-1])
#                 print("%s\t\t High-Average: %i\t\t Low-Average: %i" % (month,int(AverageHigh[:-1])-highTemp,int(AverageLow[:-1])-lowTemp))
# except FileNotFoundError:
#     print("File not found")