from person import *
class Student(Person):
    def __init__(self, firstname, Lastname, Birthday, Gender, identificationNumber, classRank, major):
        Person.__init__(self,firstname,Lastname, Birthday, Gender)
        self.indentificationNumber=identificationNumber
        self.classRank=classRank
        self.gPA=0
        self.major=major
        self.semestersAttended=[]
        self.numberOfCreditsTaken=0
        self.numberOfCreditPassed=0
    def __str__(self):
        return ("Number:%s,classrange:%s,gPA:%s,major:%s,semesterAttended:%s,numberOfCreditsTaken:%s,numberOfCreditPassed:%s"
                % (self.indentificationNumber, self.classRank, self.gPA, self.major, self.semestersAttended, self.numberOfCreditsTaken, self.numberOfCreditPassed))
    def setindentificationNumber(self,newNumber):
        self.indentificationNumber=newNumber
    def getindentificationNumber(self):
        return self.indentificationNumber
    def setclassrange(self,newrange):
        self.classRank=newrange
    def getclassrange(self):
        return self.classRank
    def setgPA(self,newGPA):
        self.gPA=newGPA

    def getgPA(self):
        return self.gPA
    def setmajor(self,newmajor):
        self.major=newmajor
    def getmajor(self):
        return self.major
    def setsemesterAttended(self,newAttended):
        self.semestersAttended=newAttended
    def getsemesterAttended(self):
        return self.semestersAttended
    def setnumberOfCreditsTaken(self,newCreditsTaken):
        self.numberOfCreditsTaken=newCreditsTaken
    def getnumberOfCreditsTaken(self):
        return self.numberOfCreditsTaken
    def setnumberOfCreditsPassed(self,newPassed):
        self.numberOfCreditsPassed=newPassed
    def getnumberOfCreditsPassed(self):
        return self.numberOfCreditsPassed

person1=Person( "Haoran","Yu","12.24.2000","Male")
student1=Student("Haoran","Yu","12.24.2000","Male",25,"freshman","technology")
print(person1,student1)
