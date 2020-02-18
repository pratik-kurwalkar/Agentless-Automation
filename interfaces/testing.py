from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        xpos = 200
        ypos = 200
        width = 300
        height = 300
        self.setGeometry(xpos, ypos, width, height)
        self.setWindowTitle("Agentless Automation")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Test Label")
        self.label.move(50, 50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("I am a button")
        self.b1.clicked.connect(self.afterclick)

    def afterclick(self):
        self.label.setText("The Butt is Clicked!")
        self.updateSize()

    def updateSize(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())


window()
