from card import Card, Face, Ace
import random

class Deck(object):
    def __init__(self):
        self.listOfCards  = []
        for suit in ('C', 'D', 'H', 'S'):
            for rank in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]:
                if 2 <= rank <= 10:
                    self.listOfCards.append(Card(rank, suit))
                elif 11 <= rank <= 13:
                    self.listOfCards.append(Face(rank, suit))
                else:
                    self.listOfCards.append(Ace(rank, suit))
    def shuffle(self):
        random.shuffle(self.listOfCards)



    def getCard(self):
        return self.listOfCards.pop( )
