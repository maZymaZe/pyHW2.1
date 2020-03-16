import sys
from InputData import input_data
from chart import chart
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
import show_data_gui
from calculation import cal
from PyQt5.QtCore import QDate
def show_data():
    def showDate(date):
        tt=date.day()
        #s=self.cal.selectedDate().toString("yyyy-MM-dd dddd")
        ui.label_7.setText("the number of Feb %d is %d"%(tt,data[tt]))

    data = input_data()
    maxNum, maxDay, minNum, minDay, ave, mid = cal(data)

    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = show_data_gui.Ui_MainWindow()
    ui.setupUi(MainWindow)
  # MainWindow.resize(760,440)
    MainWindow.show()
    ui.label.setText("minNum:"+str(minNum))
    ui.label_2.setText("minDay:"+str(minDay))
    ui.label_3.setText("maxNum:"+str(maxNum))
    ui.label_4.setText("maxDay:"+str(maxDay))
    ui.label_5.setText("average:"+str(ave))
    ui.label_6.setText("median:"+str(mid))
    ui.label_7.setText("")
    ui.pushButton.clicked.connect(chart)
    ui.calendarWidget.clicked.connect(showDate)
    sys.exit(app.exec_())
