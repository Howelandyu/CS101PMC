class Bicycle(object):
 def __init__(self, cadence = 0,speed = 0, gear = 1):
    self.cadence = cadence
    self.speed = speed
    self.gear = gear
 def changeCadence(self, cadenceValue):
    self.cadence = cadenceValue
 def getCadence(self):
    return self.cadence
 def changeGear(self, gearValue):
    self.gear = gearValue

 def getGear(self):

    return self.gear
 def speedUp(self, increment):
    self.speed += increment
 def getSpeed(self):
    return self.speed
 def applyBrakes(self, decrement):
    self.speed -= decrement
 def printState(self):
    print("cadence:",
        self.getCadence(),",speed:",
        self.getSpeed(),",gear:",
        self.getGear())

class ThreeSpeedBike(Bicycle):
    NUMGEARS = 3
    def changeGear(self, gearValue):

        if 0 < gearValue < self.NUMGEARS + 1:
         self.gear = gearValue
        else:
            print("This bike has only % i gears.You cannot set the  gear to % i"  % (self.NUMGEARS, gearValue))



# BicycleDemo!
# Create two different Bicycle
bike1 = Bicycle()
bike2 = Bicycle()

# Invoke methods on those objects!
print("Bike1")
bike1.changeCadence(50)
bike1.speedUp(10)
bike1.changeGear(2)
bike1.printState()

print("Bike2")
bike2.changeCadence(50)
bike2.speedUp(10)
bike2.changeGear(2)
bike2.changeCadence(40)
bike2.speedUp(10)
bike2.changeGear(3)
bike2.printState()
bike3 = ThreeSpeedBike()
print("Bike3")
bike3.changeCadence(50)
bike3.changeGear(4)
bike3.speedUp(10)
bike3.changeGear(3)
bike3.changeGear(0)
bike3.printState()

