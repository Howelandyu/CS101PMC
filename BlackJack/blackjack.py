from pickle import load,dump

from os.path import exists

import sys
import blackjackResources_rc
from time import sleep
from PyQt5.QtCore import pyqtSlot,QTimer,QCoreApplication,QSettings,QObject
from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import  QMainWindow, QApplication,QDialog
from random import randint
from card import Card
from deck import Deck
from  hand import Hand

class BlackjackGame(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi("blackjack.ui", self)
        self.unCover=False
        self.playercard=Card
        self.dealercard=Card
        self.playerHand=Hand()
        self.dealerHand=Hand()
        self.deck=Deck()
        self.deck.shuffle()
        self.playerbet.setRange(10, 100)
        self.playerbet.setSingleStep(5)
        # self.yourCardValue=0
        self.hit = False
        self.stay = False
        self.playerwinsCounter=0
        self.dealerwinsCounter=0
        self.playerbankvalue = randint(10, 999)
        self.dealerbankvalue=randint(10,999)
        # self.playerbet = 0
        self.hitButton.clicked.connect(self.hitButtonClickedHandler)
        # self.hitButton.clicked.connect(self.hitButtonClickedHandler2)
        self.stayButton.clicked.connect(self.stayButtonClickedHandler)
        self.newButton.clicked.connect(self.newButtonClickhandler)
        # self.playerbet.valueChanged.connect(self.spinBoxChangedHandler)
        # self.hitButton.setEnabled(False)
        # self.stayButton.setEnabled(False)
        self.newButtonClickhandler()  #Start the game
        self.updateUI()


    def updateUI ( self ):
        # if self.unCover == True:
        #     print("dealercard1: %i" % (self.dealercard1.getValue()))
        #     self.dealercard1.setPixmap(QtGui.QPixmap(":/" + str(self.dealercard1.getValue())))
        # else:
        #     self.dealercard1.setPixmap(QtGui.QPixmap(":/" + "?"))

        self.dealerwins.setText(str(self.dealerwinsCounter))
        self.playerwins.setText(str(self.playerwinsCounter))
        self.playerBank.setText(str(self.playerbankvalue))
        self.dealerBank.setText(str(self.dealerbankvalue))
        # self.DealerValue.setText(str(self.dealerHand.getValue()))
        self.yourValue.setText(str(self.playerHand.getValue()))
        self.playercard1.setPixmap(QtGui.QPixmap(":/" + str(self.playerHand.getCard(1))))
        self.playercard2.setPixmap(QtGui.QPixmap(":/" + str(self.playerHand.getCard(2))))
        self.playercard3.setPixmap(QtGui.QPixmap(":/" + str(self.playerHand.getCard(3))))
        self.playercard4.setPixmap(QtGui.QPixmap(":/" + str(self.playerHand.getCard(4))))
        self.playercard5.setPixmap(QtGui.QPixmap(":/" + str(self.playerHand.getCard(5))))
        self.playercard6.setPixmap(QtGui.QPixmap(":/" + str(self.playerHand.getCard(6))))
        self.playercard7.setPixmap(QtGui.QPixmap(":/" + str(self.playerHand.getCard(7))))
        if self.unCover:
            self.dealercard1.setPixmap(QtGui.QPixmap(":/" + str(self.dealerHand.getCard(1))))

        else:
            self.dealercard1.setPixmap(QtGui.QPixmap(":/back"))

        self.dealercard2.setPixmap(QtGui.QPixmap(":/" + str(self.dealerHand.getCard(2))))
        self.dealercard3.setPixmap(QtGui.QPixmap(":/" + str(self.dealerHand.getCard(3))))
        self.dealercard4.setPixmap(QtGui.QPixmap(":/" + str(self.dealerHand.getCard(4))))
        self.dealercard5.setPixmap(QtGui.QPixmap(":/" + str(self.dealerHand.getCard(5))))
        self.dealercard6.setPixmap(QtGui.QPixmap(":/" + str(self.dealerHand.getCard(6))))
        self.dealercard7.setPixmap(QtGui.QPixmap(":/" + str(self.dealerHand.getCard(7))))


    @pyqtSlot()
    def newButtonClickhandler (self):
        self.playerHand.clearHand()
        self.dealerHand.clearHand()

        self.playerHand.addCard(self.deck)
        self.playerHand.addCard(self.deck)
        self.unCover = False
        self.dealerHand.addCard(self.deck)
        self.dealerHand.addCard(self.deck)

        self.updateUI()

        self.newButton.setEnabled(False)
        self.hitButton.setEnabled(True)
        self.stayButton.setEnabled(True)

        self.updateUI()

    @pyqtSlot()
    def hitButtonClickedHandler(self):
        self.playerHand.addCard(self.deck)
        if self.playerHand.hasBlackjack():
            self.playerwinsCounter += 1
            self.playerbankvalue = self.playerbankvalue + self.playerbet.value()
            self.dealerbankvalue = self.dealerbankvalue - self.playerbet.value()

        if self.playerHand.isBusted():
            self.dealerwinsCounter += 1
            self.playerbankvalue = self.playerbankvalue - self.playerbet.value()
            self.dealerbankvalue = self.dealerbankvalue + self.playerbet.value()
            # if self.playerHand.getValue() > self.dealerHand.getValue():
            #     # self.playDealer()
            #     self.dealerwinsCounter += 1
            #     self.playerbankvalue = self.playerbankvalue - self.playerbet.value()
            #     self.dealerbankvalue = self.dealerbankvalue + self.playerbet.value()
        elif self.playerHand.getValue() > self.dealerHand.getValue():
            self.playerwinsCounter += 1
            self.playerbankvalue = self.playerbankvalue + self.playerbet.value()
            self.dealerbankvalue = self.dealerbankvalue - self.playerbet.value()
        elif self.playerHand.getValue() < self.dealerHand.getValue():
             # self.playDealer()
                self.dealerwinsCounter += 1
                self.playerbankvalue = self.playerbankvalue - self.playerbet.value()
                self.dealerbankvalue = self.dealerbankvalue + self.playerbet.value()
        else:
            pass

        self.unCover=True
        self.newButton.setEnabled(True)
        self.hitButton.setEnabled(False)
        self.stayButton.setEnabled(False)
        # self.updateUI()
        self.updateUI()
    @pyqtSlot()
    def stayButtonClickedHandler(self):
        # self.playDealer()
        if self.playerHand.hasBlackjack():
            self.playerwinsCounter += 1
            self.playerbankvalue = self.playerbankvalue + self.playerbet.value()
            self.dealerbankvalue = self.dealerbankvalue - self.playerbet.value()

        if self.playerHand.isBusted():
            self.dealerwinsCounter += 1
            self.playerbankvalue = self.playerbankvalue - self.playerbet.value()
            self.dealerbankvalue = self.dealerbankvalue + self.playerbet.value()
            # if self.playerHand.getValue() > self.dealerHand.getValue():
            #     # self.playDealer()
            #     self.dealerwinsCounter += 1
            #     self.playerbankvalue = self.playerbankvalue - self.playerbet.value()
            #     self.dealerbankvalue = self.dealerbankvalue + self.playerbet.value()
        elif self.playerHand.getValue() > self.dealerHand.getValue():
            self.playerwinsCounter += 1
            self.playerbankvalue = self.playerbankvalue + self.playerbet.value()
            self.dealerbankvalue = self.dealerbankvalue - self.playerbet.value()
        elif self.playerHand.getValue() < self.dealerHand.getValue():
            # self.playDealer()
            self.dealerwinsCounter += 1
            self.playerbankvalue = self.playerbankvalue - self.playerbet.value()
            self.dealerbankvalue = self.dealerbankvalue + self.playerbet.value()
        else:
            pass

        self.unCover =True
        self.newButton.setEnabled(True)
        self.hitButton.setEnabled(False)
        self.stayButton.setEnabled(False)
        self.updateUI()
        # self.updateUI()
    @pyqtSlot()
    def spinBoxChangedHandler(self):
        self.bidSpinbox=self.bidspinBox.value()
        self.updateUI()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoApp = BlackjackGame()
    demoApp.updateUI()
    demoApp.show()
    sys.exit(app.exec_())



