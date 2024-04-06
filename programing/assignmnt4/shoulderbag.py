class SHoulderBag(object):
    def __init__(self,beginCapacity,begincolor,beginweight,beginname,beginowner,begincontent):
       self.capacity=beginCapacity
       self.color=begincolor
       self.weight=beginweight
       self.name=beginname
       self.owner=beginowner
       self.content=begincontent
    def __str__(self):
        return ("capacity:%i","color:%i","weight:%i","name:%i","owner:%i","content:%i" %self.capacity( ),self.color( ),self.weight( ),self.weight( ),self.owner( ),self.content( ))
    def setcapacity(self,newcapacity):
        self.capacity=newcapacity
    def getcapacity(self):
        return self.capacity
    def setcolor(self,newcolor):
        self.color=newcolor
    def getcorlor(self):
        return self.color
    def setaddItem(self,newItem):
        addItem=newItem
        self.weight+=addItem
        self.content.append(newItem)
    def getaddItem(self):
        return self.weight
    def setreduceItem(self,oldItem):
        reduceItem=oldItem
        self.weight-=reduceItem
        self.content.append(reduceItem)
    def getreduceItem(self):
        return self.weight
    def setname(self,newname):
        self.name=newname
    def gatname(self):
        return self.name


print(SHoulderBag)

























