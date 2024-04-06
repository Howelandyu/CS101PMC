from random import randint
class Die:
    def __init__(self,sides=6):
        self.value=0
        self.numberOfSides=sides
    def getVakue(self):
        return self.value
    def setValue(self,newValue=0):
        self.value=newValue
    def roll(self):
        self.value=randint(1)