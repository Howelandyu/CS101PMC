from card import Card
from deck import Deck

class Hand(object):
    def __init__(self):
        self.cards=[ ]
        self.softValue  = 0
        self.hardValue = 0
        self.busted = False
        self.blackjack = False
        # self.PlayDealer = 0
        # while self.PlayDealer < 17 in addCard():
        #     return self.PlayerDealer
    def clearHand(self):
        self.cards.clear()
        self.softValue = 0
        self.hardValue = 0
        self.busted = False
        self.blackjack = False

    def addCard(self, cardDeck):
        self.cards.append(cardDeck.getCard())
        self.softValue += self.cards[-1].getSoftValue()
        self.hardValue += self.cards[-1].getHardValue()
        if self.hardValue > 21:
            self.busted=True
        if self.softValue == 21 and len(self.cards) == 2 :
            self.blackjack = True
        self.PlayDealer = 0

    def getCard(self, cardNumber):
        if cardNumber <= len(self.cards):
            return self.cards[cardNumber - 1]
        else:
            return None

    def getSoftValue(self):
        pass

    def getHardValue(self):
        pass

    def getValue(self):
        if self.softValue > 21:
            return self.hardValue
        else:
            return self.softValue

    def isBusted(self):
        return self.busted

    def hasBlackjack(self):
        return self.blackjack

