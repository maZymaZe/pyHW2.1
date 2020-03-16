# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newgui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(289, 309)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 20, 171, 51))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 90, 171, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 160, 171, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 289, 18))
        self.menubar.setObjectName("menubar")
        self.menuabout = QtWidgets.QMenu(self.menubar)
        self.menuabout.setObjectName("menuabout")
        self.menuabout_the_author = QtWidgets.QMenu(self.menuabout)
        self.menuabout_the_author.setObjectName("menuabout_the_author")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionmaZymaZe = QtWidgets.QAction(MainWindow)
        self.actionmaZymaZe.setObjectName("actionmaZymaZe")
        self.menuabout_the_author.addAction(self.actionmaZymaZe)
        self.menuabout.addAction(self.menuabout_the_author.menuAction())
        self.menubar.addAction(self.menuabout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "get data"))
        self.label.setText(_translate("MainWindow", "    Hello! In this programme, you can learn something about new patients of 2019-nCoV in China in each day of Febrary."))
        self.pushButton.setText(_translate("MainWindow", "get data from Internet(recommended)"))
        self.pushButton_2.setText(_translate("MainWindow", "manual input"))
        self.menuabout.setTitle(_translate("MainWindow", "about"))
        self.menuabout_the_author.setTitle(_translate("MainWindow", "about the author"))
        self.actionmaZymaZe.setText(_translate("MainWindow", "maZymaZe"))
