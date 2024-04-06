
from math import pi
class sphere(object):
    def __init__(self,radius):
        self.radius=float(radius)
        self.setradius(radius)
    def __str__(self):
        return ("半径:%5.2f 体积:%1.5f 面积:%2.5f " %(self.radius,self.Volume(),self.Area()))
    def setradius(self,newradius):
       if type(newradius)==int or type(newradius)==float:
            if newradius>0:
                self.radius=float(newradius)
        #     else:
        #         raise ValueError
        # else:
        #     raise ValueError
    def getradius(self):
        return self.radius
    def Volume(self):
         return (4/3)*pi*self.radius**3
    def Area(self):
        return 4*pi*self.radius**2














sphere1=sphere(3)
print(sphere1.Volume())
print(sphere1.Area())
print(sphere1)
sphere1.setradius(4)
print(sphere1)
print(sphere1.getradius())

#     sphere=input("type a number")
#     if sphere>0:
#     ball1=sphere()
#     print(ball1)
#     print(ball1.Volume( ))
#     print(ball1.Area( ))
# else:
#     print("type valid number")
# try:
#     sphere
# except(ValueError):
#         print("type valid number")



