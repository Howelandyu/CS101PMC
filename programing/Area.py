class Quadrilateral(object):
    def __init__(self,height=5,width=8,deepth=4):
        self.height=height
        self.width=width
        self.deepth=deepth

    def getheight(self):
        return self.height
    def setheight(self,changeheight):
        self.height=changeheight
    def getwidth(self):
        return self.width
    def setwidth(self,changewidth):
        self.width=changewidth
    def getdeepth(self):
        return self.deepth
    def setdeepth(self,changedeepth):
        self.deepth=changedeepth
    def volume(self):
        return self.height*self.width*self.deepth
    def Area(self):
        return



class Cube(Quadrilateral):
    def __init__(self):


