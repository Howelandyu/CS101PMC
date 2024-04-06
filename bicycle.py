class Bicycle(object):

    def __init__(self, cadence = 0, speed = 0, gear = 1):
        self.cadence = cadence
        self.speed = speed
        self.gear = gear

    def changeCadence(self, newValue):
        self.cadence = newValue

    def getCadence(self):
        return self.cadence

    def changeGear(self, newValue):
        self.gear = newValue

    def getGear(self):
        return self.gear

    def speedUp(self, increment):
        self.speed += increment

    def getSpeed(self):
        return self.speed

    def applyBrake(self, decrement):
        self.speed -= decrement

    def getSpeed(self):
        return self.speed


    def printState(self):
        print("Cadence: ",self.getCadence(), "Speed:",self.getSpeed(), "Gear: ",self.getGear())
class threeSpeedBike(Bicycle):
    NUMGEARS = 10
    def changeGear(self, newValue):
        if 0 < newValue < self.NUMGEARS + 1:
            self.gear = newValue
        else:
            print("This bike has only %i gears. You cannot set the gear to %i." %(self.NUMGEARS, newValue))


bike1 = Bicycle()
bike2 = Bicycle()
bike3 = threeSpeedBike()

print("bike1")
bike1.changeCadence(20)
bike1.changeGear(6)
bike1.speedUp(50)
bike1.printState()

print("Bike3")
bike3.changeCadence(300)
bike3.changeGear(8)
bike3.speedUp(900)
bike3.printState()