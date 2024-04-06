class Class(object):
    def __init__(self, Name, number, section, numberOfCredits, grade, startDate, length, capacity):
        self.Name=Name
        self.number=number
        self.section=section
        self.numberOfCredits=numberOfCredits
        self.grade=0
        self.startDate=startDate
        self.length=length
        self.capacity=capacity
    def __str__(self):
        return "Class:%s,number:%s,section:%s,numberOfCredits:%s,grade:%s,startdate:%s,length:%s,capacity:%s" %(self.Name, self.number, self.section, self.numberOfCredits, self.grade, self.startDate, self.length, self.capacity)
    def setName(self,newname):
        self.Name=newname
    def getName(self):
        return self.Name
    def setnumber(self,newnumber):
        self.number=newnumber
    def getnumber(self):
        return self.number
    def setsection(self,newsection):
        self.section=newsection
    def getsection(self):
        return self.section
    def setnumberOfCredits(self,newCredits):
        self.numberOfCredits=newCredits
    def getnumberOfCredits(self):
        return self.numberOfCredits
    def setgrade(self,newgrade):
        self.grade=newgrade
    def getgrade(self):
        return self.grade
    def setstartDate(self,newDate):
        self.startDate=newDate
    def getstartDate(self):
        return self.startDate
    def setlength(self,newlength):
        self.length=newlength
    def getlength(self):
        return self.length
    def setcapacity(self,newcapacity):
        self.capacity=newcapacity
    def getcapacity(self):
        return self.capacity

class1=Class("Computer",12,"writing program",4.0,16,"9-1",24,20)
print(class1)
