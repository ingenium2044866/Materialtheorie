from PyQt5 import QtCore, QtGui, QtWidgets
import sys 
import Materialtheorie

class MainWin(QtWidgets.QMainWindow,Materialtheorie.Ui_xx):
      def __init__(self, parent = None):
            super(Main.UiClass,self).__init__(parent)
            self.setupUi(self)
            
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    xx = QtWidgets.QMainWindow()
    xx.show()
    sys.exit(app.exec_())