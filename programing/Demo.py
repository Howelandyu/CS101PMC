import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import  QMainWindow, QApplication

class Dice(QMainWindow):

    def __init__(self,parent=None):
        super( ).__init__(parent)
        uic.loadUi("demo.ui",self)
        self.outputMessage=" "

        self.pushMeButton.connect(self.pushMeButtonClickedHandler)

    def updateUI(self):
        self.outputText.setTest(self.outputMessage)

    @pyqtSlot(str)
    def pushMeButtonClickedHandler(self):
        print(" buttom Pressed")
        self.outputMessage="Hello Here"
        self.updateUI( )
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoApp = Dice()
    demoApp.updateUI()
    demoApp.show()
    sys.exit(app.exec_())

