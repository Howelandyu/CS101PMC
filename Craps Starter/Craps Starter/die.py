#!/usr/bin/env python
from random import randint

class Die(object):
    def __init__(self, startingNumberOfSides=6):
        self.numberOfSides = startingNumberOfSides
        self.value = 1

    def setNumberOfSides(self, newNumberOfSides):
        self.numberOfSides = newNumberOfSides


    def getNumberOfSides(self):
        return self.numberOfSides

    def setValue(self, newValue):
        self.value = newValue

    def getValue(self):
        return self.value

    def roll(self):
        self.value = randint(1, self.numberOfSides)
        return self.value


