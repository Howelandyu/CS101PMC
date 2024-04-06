import sys
from PyQt5.QtCore import pyqtSlot
from Die import *
from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import  QMainWindow, QApplication
import chohanresources_rc

class Chohan(QMainWindow):

    def __init__(self,parent=None):
        super( ).__init__(parent)
        uic.loadUi("chohan.ui",self)
        self.outputMessage="Game start "
        self.ObsureDice=False
        self.die1=Die()
        self.die2=Die()
        self.die3 = Die()
        self.die4 = Die()
        self.die5 = Die()
        self.die6 = Die()
        self.dieTotal=0
        self.wins = 0
        self.lose=0
        self.yourbank=100
        self.rollButton.clicked.connect(self.rollButtonClickedHandler)
        self.oddsButton.clicked.connect(self.oddButtonClickedHandler)
        self.evensButton.clicked.connect(self.evenButtonClickedHandler)
    def updateUI(self):
        if self.ObsureDice == True:
            self.die1View.setPixmap(QtGui.QPixmap(":/?"))
            self.die2View.setPixmap(QtGui.QPixmap(":/?"))
            self.die3View.setPixmap(QtGui.QPixmap(":/?"))
            self.die4View.setPixmap(QtGui.QPixmap(":/?"))
            self.die5View.setPixmap(QtGui.QPixmap(":/?"))
            self.die6View.setPixmap(QtGui.QPixmap(":/?"))
        else:
            self.die1View.setPixmap(QtGui.QPixmap(":/" +str(self.die1.getValue())))
            self.die2View.setPixmap(QtGui.QPixmap(":/" + str(self.die2.getValue())))
            self.die3View.setPixmap(QtGui.QPixmap(":/" + str(self.die3.getValue())))
            self.die4View.setPixmap(QtGui.QPixmap(":/" + str(self.die4.getValue())))
            self.die5View.setPixmap(QtGui.QPixmap(":/" + str(self.die5.getValue())))
            self.die6View.setPixmap(QtGui.QPixmap(":/" + str(self.die6.getValue())))
        self.resultLabel.setText(self.outputMessage)
        self.winsLabel.setText(str(self.wins))
        self.loseLabel.setText(str(self.lose))
        self.bankLabel.setText(str(self.yourbank))

    @pyqtSlot()
    def rollButtonClickedHandler(self):
        print("roll buttom Pressed")
        self.outputMessage="Hello Here"
        self.ObsureDice=True
        self.die1.roll()
        self.die2.roll()
        self.die3.roll()
        self.die4.roll()
        self.die5.roll()
        self.die6.roll()
        self.dieTotal=self.die1.getValue()+ self.die2.getValue()+self.die3.getValue()+self.die4.getValue()+self.die5.getValue()+self.die6.getValue()
        self.updateUI( )

    @pyqtSlot()
    def oddButtonClickedHandler(self):
        print("odds buttom Pressed")
        self.ObsureDice=False
        if self.dieTotal%2==1:
            self.wins = self.wins + 1
            self.outputMessage = "You Won!"
            self.yourbank += self.bidValue.value()
        else:
            self.lose=self.lose+1
            self.outputMessage = "You Lost."
            self.yourbank -= self.bidValue.value()

        self.updateUI()

    @pyqtSlot()
    def evenButtonClickedHandler(self):
        print("odds buttom Pressed")
        self.ObsureDice=False
        if self.dieTotal%2==0:
            self.wins = self.wins + 1
            self.outputMessage = "You Won!"
            self.yourbank += self.bidValue.value()
        else:
            self.lose=self.lose+1
            self.outputMessage = "You Lost."
            self.yourbank -= self.bidValue.value()

        self.updateUI()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoApp = Chohan()
    demoApp.updateUI()
    demoApp.show()
    sys.exit(app.exec_())

