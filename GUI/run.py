import sys


from PyQt5 import QtCore, QtGui, QtWidgets, uic
 
ui_file_path =  "Materialtheorie.ui"

class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):

        # Parent class init
        QtGui.QMainWindow.__init__(self) 
        # You may also write
        # super(MyApp, self).__init__()

        # Load UI
        uic.loadUi(ui_file_path, self)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())