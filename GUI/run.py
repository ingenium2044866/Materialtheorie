import sys, os
from PyQt5 import QtGui,QtCore,uic,QtWidgets

DIRPATH = os.path.join(os.path.dirname(os.path.abspath(__file__)))

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi(os.path.join(DIRPATH, 'Materialtheorie.ui'), self)
        #self.Knopka.clicked.connect(self.handleButton)

    #def handleButton(self):
        #print('Hello World ! ')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())