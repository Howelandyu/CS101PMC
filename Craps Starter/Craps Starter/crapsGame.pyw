#!/usr/bin/env python

from die import * 
import sys
import crapsResources_rc
from time import sleep
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import  QMainWindow, QApplication
from random import randint
class Craps(QMainWindow) :
    """A game of Craps."""
    die1 = die2 = None

    def __init__( self, parent=None ):
        """Build a game with two dice."""

        super().__init__(parent)
        uic.loadUi("Craps.ui", self)

        self.bidSpinBox.setRange ( 10, 100 )
        self.bidSpinBox.setSingleStep ( 5 )

        self.unCover = False

        self.die1 = Die()
        self.die2 = Die()
        self.die3 = Die()
        self.die4 = Die()
        self.die5 = Die()
        self.die6 = Die()
        self.totalValue = 0
        self.buttonText = "Roll"
        self.even = False
        self.odd = False

        self.winsCounter = 0
        self.losesCounter = 0
        self.result = ''
        self.bank = randint(10,100)

        self.payouts = [0, 0, 0,  0,  2.0,  1.5,  1.2,  0,  1.2,  1.5,  2.0,  0,  0]

        self.rollButton.clicked.connect(self.rollButtonClickedHandler)
        self.evenButton.clicked.connect(self.evenButtonClickedHandler)
        self.oddButton.clicked.connect(self.oddButtonClickhandler)
        self.evenButton.setEnabled(False)
        self.oddButton.setEnabled(False)

    def __str__( self ):
        """String representation for Dice.
        """

        return "Die1: %s\nDie2: %s" % ( str(self.die1),  str(self.die2) )

    def updateUI ( self ):
        if self.unCover == True:
            print("Die1: %i, Die2: %i" % (self.die1.getValue(),  self.die2.getValue()))
            self.die1View.setPixmap(QtGui.QPixmap( ":/" + str( self.die1.getValue() ) ) )
            self.die2View.setPixmap(QtGui.QPixmap( ":/" + str( self.die2.getValue() ) ) )
            self.die3View.setPixmap(QtGui.QPixmap( ":/" + str( self.die3.getValue() ) ) )
            self.die4View.setPixmap(QtGui.QPixmap( ":/" + str( self.die4.getValue() ) ) )
            self.die5View.setPixmap(QtGui.QPixmap( ":/" + str( self.die5.getValue() ) ) )
            self.die6View.setPixmap(QtGui.QPixmap( ":/" + str( self.die6.getValue() ) ) )
            self.rollingForLabel.setText(str(self.totalValue))
        else:
            self.die1View.setPixmap(QtGui.QPixmap(":/" + "?"))
            self.die2View.setPixmap(QtGui.QPixmap(":/" + "?"))
            self.die3View.setPixmap(QtGui.QPixmap(":/" + "?"))
            self.die4View.setPixmap(QtGui.QPixmap(":/" + "?"))
            self.die5View.setPixmap(QtGui.QPixmap(":/" + "?"))
            self.die6View.setPixmap(QtGui.QPixmap(":/" + "?"))
        self.winsLabel.setText(str(self.winsCounter))
        self.lossesLabel.setText(str(self.losesCounter))
        self.bankValue.setText(str(self.bank))
        self.resultsLabel.setText(self.result)



            # Add your code here to update the GUI view so it matches the game state.

    @pyqtSlot()				# Player asked for another roll of the dice.
    def rollButtonClickedHandler ( self ):
        self.unCover = False
        self.currentBet = self.bidSpinBox.value()
        self.die1.roll()
        self.die2.roll()
        self.die3.roll()
        self.die4.roll()
        self.die5.roll()
        self.die6.roll()
        self.totalValue = self.die1.getValue() + self.die2.getValue() + self.die3.getValue() + self.die4.getValue() + self.die5.getValue() + self.die6.getValue()

        self.rollButton.setEnabled(False)
        self.evenButton.setEnabled(True)
        self.oddButton.setEnabled(True)


        if self.totalValue % 2 ==0:
            self.even = True
            self.odd =False

        else:
            self.odd = True
            self.even = False

        # Play the first roll
        pass            # Replace this line with your roll event handler
        self.updateUI()

    @pyqtSlot()				# Player asked for another roll of the dice.
    def evenButtonClickedHandler ( self ):
        self.unCover = True

        if self.even == True:
            self.winsCounter += 1
            self.bank = self.bank + self.bidSpinBox.value()
            self.result = 'You win!'
        else:
            self.losesCounter += 1
            self.bank  =self.bank - self.bidSpinBox.value()
            self.result = 'You Lose!'
        self.evenButton.setEnabled(False)
        self.oddButton.setEnabled(False)
        self.rollButton.setEnabled(True)

        self.updateUI()

    @pyqtSlot()
    def oddButtonClickhandler(self):
        self.unCover = True

        if self.odd == True:
            self.winsCounter += 1
            self.bank = self.bank + self.bidSpinBox.value()
            self.result = 'You win!'
        else:
            self.losesCounter += 1
            self.bank  =self.bank - self.bidSpinBox.value()
            self.result = 'You Lose!'

        self.evenButton.setEnabled(False)
        self.oddButton.setEnabled(False)
        self.rollButton.setEnabled(True)

        self.updateUI()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    diceApp = Craps()
    diceApp.updateUI()
    diceApp.show()
    sys.exit(app.exec_())


