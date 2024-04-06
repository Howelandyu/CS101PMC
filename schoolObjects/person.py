class Person(object):
    def __init__(self,firstname,Lastname, Birthday, Gender):
        self.firstname=firstname
        self.Lastname=Lastname
        self.Birthday=Birthday
        self.Gender=Gender
    def __str__(self):
        return ("firstname:%s, Lastname:%s, Birthday:%s, Gender:%s" %(self.firstname,self.Lastname,self.Birthday,self.Gender))

    def setfirstname(self,newfirstname):
        self.firstname=newfirstname
    def getfirstname(self):
        return self.firstname
    def setLastname(self,newLastname):
        self.Lastname=newLastname
    def getLastname(self):
        return self.Lastname
    def setBirthday(self,newBirthday):
        self.Birthday=newBirthday
    def getBirthday(self):
        return self.Birthday
    def setGender(self,newGender):
        self.Gender=newGender
    def getGender(self):
        return self.Gender


person1=Person("Haoran","Yu","12.24.2000","Male" )
print(person1)





