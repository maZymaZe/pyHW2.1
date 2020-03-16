#from InputData import input_data
from calculation import cal
#from newgui import newgui
from web import web
from manual_get import manual_get
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import  QtCore
import newgui

if __name__ == '__main__':

    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = newgui.Ui_MainWindow()
    ui.setupUi(MainWindow)
  # MainWindow.resize(760,440)
    MainWindow.show()
    ui.pushButton.clicked(web)
    ui.pushButton_2.clicked(manual_get)
    sys.exit(app.exec_())

#data=input_data()
#maxNum,maxDay,minNum,minDay,ave,mid=cal(data)
#gui(maxNum,maxDay,minNum,minDay,ave,mid,data)