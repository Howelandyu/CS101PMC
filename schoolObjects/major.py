class Major(object):
    def __init__(self,Name,numberOfCredit):
        self.name=Name
        self.numberOfCredits=numberOfCredit
    def __str__(self):
        return ("name:%s,Credits:%s" %(self.name,self.numberOfCredits))
    def setName(self,newname):
        self.Name=newname
    def getname(self):
        return self.name
    def setnumberOfCredits(self,newCredits):
        self.numberOfCredits=newCredits
    def getnumberOfCredits(self):
        return self.numberOfCredits

major1=Major("Computer","4.0")
print(major1)