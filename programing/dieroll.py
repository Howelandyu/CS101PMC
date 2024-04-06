from random import randint

class Die(object):
    def __init__(self,sides=6):
        self.value=0
        self.numberOfSide=sides
    def getValue(self):
        return self.value
    def setValue(self,newValue=0):
        self.value=newValue
    def roll(self):
        self.value=self.sides.random()