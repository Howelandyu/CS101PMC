class Card(object):
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit  = suit
        self.hardValue=rank
        self.softValue=rank
    def __str__(self):
        if self.rank <= 10:
            return str(self.rank) + self.suit
        elif self.rank == 11:
            return 'J' + self.suit
        elif self.rank == 12:
            return 'Q' + self.suit
        elif self.rank == 13:
            return 'K' + self.suit
        elif self.rank == 14:
            return 'A' + self.suit

    def getHardValue(self):
        return self.hardValue
    def getSoftValue(self):
        return self.softValue


class Face(Card):
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit  = suit
        self.hardValue=10
        self.softValue=10
class Ace(Card):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit  = suit
        self.hardValue=1
        self.softValue=11


