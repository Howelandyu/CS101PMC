class semester(object):
    def __init__(self,year,term,listOfClassesTaken):
        self.year=year
        self.term=term
        self.listOfClassesTaken=listOfClassesTaken
        self.gPA=0
        self.numberOfCreditsTaken=[]
        self.numberOfCreditsPassed=[]
    def __str__(self):
        return ("year:%s, term:%s, Classlist:%s, gPA:%s, CreditTake:%s, CreditPass:%s"
                %(self.year,self.term,self.listOfClassesTaken,self.gPA,self.numberOfCreditsTaken,self.numberOfCreditsPassed))
    def setyear(self,newyear):
        self.year=newyear
    def getyear(self):
        return self.year
    def setterm(self,newterm):
        self.term=newterm
    def getterm(self):
        return self.term
    def setlistOfClassesTaken(self,newTaken):
        self.listOfClassesTaken=newTaken
    def getlistOfClassesTaken(self):
        return self.listOfClassesTaken
    def setgPA(self,newgpa):
        self.gPA=newgpa
        totalCredit=4
        totalGrade=16
        for computer in self.listOfClassesTaken:
            totalCredit+=computer.getCredits(4)
            totalGrade+=computer.getCredits(4)*computer.getGrade(16)
        newgpa=totalGrade/totalCredit
        return newgpa
    def getgPA(self):
        return self.gPA
    def setnumberOfCreditsTaken(self,newCreditsTaken):
        self.numberOfCreditsTaken=newCreditsTaken
    def getnumberofCreditsTaken(self):
        return self.numberOfCreditsTaken
    def setnumberOfCreditsPassed(self,newCreditsPassed):
        self.numberOfCreditsPassed=newCreditsPassed
    def getnumberOfCreditsPassed(self):
        return self.numberOfCreditsPassed

semester1=semester("2016","first","computer")
print(semester1.setgPA(5))


