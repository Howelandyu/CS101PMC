# highestTemp=0
# highYear=0
# lowestTemp=200
# lowYear=0
# try:
#     with open('testfile.txt','r') as testFileHandle:
#         headings=testFileHandle.readline( ).split('\t')
#         for inputLine in testFileHandle.readlines():
#             print(inputLine,end='')
            # print(inputLine.strip().split('\t'))
#             Date, AverageLow,  AverageHigh, LowRecordYear, HighRecordYear,AveragePrecipitation, AverageSnow=inputLine.strip().split('\t')
#             lowTemp,lowTempYear=LowRecordYear.split( )
#             lowTemp=int(lowTemp[:-1])
#             lowTempYear=int(lowTempYear[1:-1])
#             highTemp,highTempYear=HighRecordYear.split( )
#             highTemp=int(highTemp[:-1])
#             highTempYear = int(highTempYear[1:-1])
#
#             if lowTemp<lowestTemp:
#                 lowestTemp=lowTemp
#                 lowYear=lowTempYear
#             if highTemp>highestTemp:
#                 highestTemp=highTemp
#                 highYear=highTempYear
#
#         print("High %f in %i Low: %f in %i" % (highestTemp,highYear,lowestTemp,lowYear))
# except FileNotFoundError:
#     print("File not found")




# TempYear=0
# temerture=200


# with open('testfile.txt','r') as testFileHandle:
#     headings=testFileHandle.readline( ).split('\t')
#     for inputLine in testFileHandle.readlines():
#         print(inputLine)
#         # print(inputLine,end='')
#         # print(inputLine.strip().split('\t'))


hightestTemp = 0
lowestTemp = 200
with open('testfile.txt','r')as testFileHandle:
    headings =testFileHandle.readline().split('\t')
    print(headings)
    for inputline in testFileHandle.readlines():
        print( inputline.strip().split('\t'))
    testFileHandle.seek(0)
    headings = testFileHandle.readline()
    print(headings)
    for inputline in testFileHandle.readlines():
        temperatures = inputline.strip().split('\t')
        print(temperatures)
        tempYear = temperatures[4].split(' ')
        print(tempYear)
        lowTempYear = temperatures[3].split()
        lowTemp = int(lowTempYear[0][:-1])
        highTempYear = temperatures[4].split(' ')
        highTemp = int(highTempYear[0][:-1])
        if lowTemp < lowestTemp:
            lowestTemp = lowTemp
        if highTemp > hightestTemp:
            hightestTemp=highTemp
    print("High %i low: %i" % (hightestTemp, lowestTemp) )