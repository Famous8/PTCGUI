# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/media/pi/My Passport/Personal/PTCGUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(923, 624)
        MainWindow.setMaximumSize(QtCore.QSize(923, 624))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 460, 131, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 460, 131, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(170, 460, 181, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(640, 460, 131, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(780, 460, 131, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(740, 560, 191, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 560, 91, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(30, 510, 181, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(40, 40, 871, 401))
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.sideb = QtWidgets.QWidget()
        self.sideb.setObjectName("sideb")
        self.lineEdit_25 = QtWidgets.QLineEdit(self.sideb)
        self.lineEdit_25.setGeometry(QtCore.QRect(200, 330, 81, 31))
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.lineEdit_26 = QtWidgets.QLineEdit(self.sideb)
        self.lineEdit_26.setGeometry(QtCore.QRect(110, 330, 81, 31))
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.lineEdit_27 = QtWidgets.QLineEdit(self.sideb)
        self.lineEdit_27.setGeometry(QtCore.QRect(20, 330, 81, 31))
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.pushButton_23 = QtWidgets.QPushButton(self.sideb)
        self.pushButton_23.setGeometry(QtCore.QRect(120, 370, 61, 23))
        self.pushButton_23.setObjectName("pushButton_23")
        self.label_9 = QtWidgets.QLabel(self.sideb)
        self.label_9.setGeometry(QtCore.QRect(0, 310, 101, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.sideb)
        self.label_10.setGeometry(QtCore.QRect(110, 310, 101, 16))
        self.label_10.setObjectName("label_10")
        self.pushButton_16 = QtWidgets.QPushButton(self.sideb)
        self.pushButton_16.setGeometry(QtCore.QRect(30, 370, 61, 23))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_29 = QtWidgets.QPushButton(self.sideb)
        self.pushButton_29.setGeometry(QtCore.QRect(210, 370, 61, 23))
        self.pushButton_29.setObjectName("pushButton_29")
        self.stackedWidget.addWidget(self.sideb)
        self.sidec = QtWidgets.QWidget()
        self.sidec.setObjectName("sidec")
        self.lineEdit_28 = QtWidgets.QLineEdit(self.sidec)
        self.lineEdit_28.setGeometry(QtCore.QRect(20, 330, 81, 31))
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.lineEdit_29 = QtWidgets.QLineEdit(self.sidec)
        self.lineEdit_29.setGeometry(QtCore.QRect(110, 330, 81, 31))
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.lineEdit_30 = QtWidgets.QLineEdit(self.sidec)
        self.lineEdit_30.setGeometry(QtCore.QRect(200, 330, 81, 31))
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.pushButton_26 = QtWidgets.QPushButton(self.sidec)
        self.pushButton_26.setGeometry(QtCore.QRect(120, 370, 61, 23))
        self.pushButton_26.setObjectName("pushButton_26")
        self.label_11 = QtWidgets.QLabel(self.sidec)
        self.label_11.setGeometry(QtCore.QRect(110, 310, 101, 16))
        self.label_11.setObjectName("label_11")
        self.label_14 = QtWidgets.QLabel(self.sidec)
        self.label_14.setGeometry(QtCore.QRect(10, 310, 101, 16))
        self.label_14.setObjectName("label_14")
        self.pushButton_17 = QtWidgets.QPushButton(self.sidec)
        self.pushButton_17.setGeometry(QtCore.QRect(30, 370, 61, 23))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_30 = QtWidgets.QPushButton(self.sidec)
        self.pushButton_30.setGeometry(QtCore.QRect(210, 370, 61, 23))
        self.pushButton_30.setObjectName("pushButton_30")
        self.stackedWidget.addWidget(self.sidec)
        self.righttriangle = QtWidgets.QWidget()
        self.righttriangle.setObjectName("righttriangle")
        self.lineEdit_31 = QtWidgets.QLineEdit(self.righttriangle)
        self.lineEdit_31.setGeometry(QtCore.QRect(30, 320, 81, 31))
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.lineEdit_32 = QtWidgets.QLineEdit(self.righttriangle)
        self.lineEdit_32.setGeometry(QtCore.QRect(160, 320, 81, 31))
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.lineEdit_33 = QtWidgets.QLineEdit(self.righttriangle)
        self.lineEdit_33.setGeometry(QtCore.QRect(280, 320, 81, 31))
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.lineEdit_34 = QtWidgets.QLineEdit(self.righttriangle)
        self.lineEdit_34.setGeometry(QtCore.QRect(390, 320, 161, 31))
        self.lineEdit_34.setObjectName("lineEdit_34")
        self.label_15 = QtWidgets.QLabel(self.righttriangle)
        self.label_15.setGeometry(QtCore.QRect(150, 300, 101, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.righttriangle)
        self.label_16.setGeometry(QtCore.QRect(270, 300, 101, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.righttriangle)
        self.label_17.setGeometry(QtCore.QRect(20, 300, 101, 16))
        self.label_17.setObjectName("label_17")
        self.pushButton_27 = QtWidgets.QPushButton(self.righttriangle)
        self.pushButton_27.setGeometry(QtCore.QRect(290, 360, 61, 23))
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_19 = QtWidgets.QPushButton(self.righttriangle)
        self.pushButton_19.setGeometry(QtCore.QRect(40, 360, 61, 23))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_31 = QtWidgets.QPushButton(self.righttriangle)
        self.pushButton_31.setGeometry(QtCore.QRect(430, 360, 61, 23))
        self.pushButton_31.setObjectName("pushButton_31")
        self.stackedWidget.addWidget(self.righttriangle)
        self.Settings = QtWidgets.QWidget()
        self.Settings.setObjectName("Settings")
        self.label_8 = QtWidgets.QLabel(self.Settings)
        self.label_8.setGeometry(QtCore.QRect(390, 340, 47, 14))
        self.label_8.setObjectName("label_8")
        self.spinBox = QtWidgets.QSpinBox(self.Settings)
        self.spinBox.setGeometry(QtCore.QRect(370, 360, 81, 22))
        self.spinBox.setObjectName("spinBox")
        self.pushButton_32 = QtWidgets.QPushButton(self.Settings)
        self.pushButton_32.setGeometry(QtCore.QRect(460, 360, 61, 23))
        self.pushButton_32.setObjectName("pushButton_32")
        self.stackedWidget.addWidget(self.Settings)
        self.Square = QtWidgets.QWidget()
        self.Square.setObjectName("Square")
        self.lineEdit = QtWidgets.QLineEdit(self.Square)
        self.lineEdit.setGeometry(QtCore.QRect(40, 330, 81, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.Square)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 330, 131, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_10 = QtWidgets.QPushButton(self.Square)
        self.pushButton_10.setGeometry(QtCore.QRect(120, 370, 61, 23))
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_4 = QtWidgets.QLabel(self.Square)
        self.label_4.setGeometry(QtCore.QRect(40, 310, 251, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton_11 = QtWidgets.QPushButton(self.Square)
        self.pushButton_11.setGeometry(QtCore.QRect(50, 370, 61, 23))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_22 = QtWidgets.QPushButton(self.Square)
        self.pushButton_22.setGeometry(QtCore.QRect(190, 370, 61, 23))
        self.pushButton_22.setObjectName("pushButton_22")
        self.stackedWidget.addWidget(self.Square)
        self.home = QtWidgets.QWidget()
        self.home.setObjectName("home")
        self.stackedWidget.addWidget(self.home)
        self.sqrt = QtWidgets.QWidget()
        self.sqrt.setObjectName("sqrt")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.sqrt)
        self.stackedWidget_2.setGeometry(QtCore.QRect(860, 10, 871, 401))
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.home_3 = QtWidgets.QWidget()
        self.home_3.setObjectName("home_3")
        self.stackedWidget_2.addWidget(self.home_3)
        self.one_3 = QtWidgets.QWidget()
        self.one_3.setObjectName("one_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.one_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(40, 330, 81, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.one_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(150, 330, 81, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_12 = QtWidgets.QPushButton(self.one_3)
        self.pushButton_12.setGeometry(QtCore.QRect(50, 370, 61, 23))
        self.pushButton_12.setObjectName("pushButton_12")
        self.label_6 = QtWidgets.QLabel(self.one_3)
        self.label_6.setGeometry(QtCore.QRect(40, 310, 251, 16))
        self.label_6.setObjectName("label_6")
        self.stackedWidget_2.addWidget(self.one_3)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.stackedWidget_2.addWidget(self.page_3)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.sqrt)
        self.lineEdit_17.setGeometry(QtCore.QRect(110, 330, 161, 31))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.sqrt)
        self.lineEdit_18.setGeometry(QtCore.QRect(10, 330, 81, 31))
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.label_12 = QtWidgets.QLabel(self.sqrt)
        self.label_12.setGeometry(QtCore.QRect(10, 310, 281, 16))
        self.label_12.setObjectName("label_12")
        self.pushButton_18 = QtWidgets.QPushButton(self.sqrt)
        self.pushButton_18.setGeometry(QtCore.QRect(90, 370, 61, 23))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_13 = QtWidgets.QPushButton(self.sqrt)
        self.pushButton_13.setGeometry(QtCore.QRect(20, 370, 61, 23))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_24 = QtWidgets.QPushButton(self.sqrt)
        self.pushButton_24.setGeometry(QtCore.QRect(160, 370, 61, 23))
        self.pushButton_24.setObjectName("pushButton_24")
        self.stackedWidget.addWidget(self.sqrt)
        self.add = QtWidgets.QWidget()
        self.add.setObjectName("add")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.add)
        self.lineEdit_19.setGeometry(QtCore.QRect(20, 330, 81, 31))
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.add)
        self.lineEdit_20.setGeometry(QtCore.QRect(120, 330, 81, 31))
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.pushButton_20 = QtWidgets.QPushButton(self.add)
        self.pushButton_20.setGeometry(QtCore.QRect(130, 370, 61, 23))
        self.pushButton_20.setObjectName("pushButton_20")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.add)
        self.lineEdit_21.setGeometry(QtCore.QRect(220, 330, 81, 31))
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.label_13 = QtWidgets.QLabel(self.add)
        self.label_13.setGeometry(QtCore.QRect(20, 310, 261, 16))
        self.label_13.setObjectName("label_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.add)
        self.pushButton_14.setGeometry(QtCore.QRect(30, 370, 61, 23))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_25 = QtWidgets.QPushButton(self.add)
        self.pushButton_25.setGeometry(QtCore.QRect(230, 370, 61, 23))
        self.pushButton_25.setObjectName("pushButton_25")
        self.stackedWidget.addWidget(self.add)
        self.sidea = QtWidgets.QWidget()
        self.sidea.setObjectName("sidea")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.sidea)
        self.lineEdit_22.setGeometry(QtCore.QRect(20, 320, 81, 31))
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.sidea)
        self.lineEdit_23.setGeometry(QtCore.QRect(120, 320, 81, 31))
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.lineEdit_24 = QtWidgets.QLineEdit(self.sidea)
        self.lineEdit_24.setGeometry(QtCore.QRect(220, 320, 81, 31))
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.pushButton_21 = QtWidgets.QPushButton(self.sidea)
        self.pushButton_21.setGeometry(QtCore.QRect(130, 360, 61, 23))
        self.pushButton_21.setObjectName("pushButton_21")
        self.label_5 = QtWidgets.QLabel(self.sidea)
        self.label_5.setGeometry(QtCore.QRect(10, 300, 101, 16))
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.sidea)
        self.label_7.setGeometry(QtCore.QRect(110, 300, 101, 16))
        self.label_7.setObjectName("label_7")
        self.pushButton_15 = QtWidgets.QPushButton(self.sidea)
        self.pushButton_15.setGeometry(QtCore.QRect(20, 360, 61, 23))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_28 = QtWidgets.QPushButton(self.sidea)
        self.pushButton_28.setGeometry(QtCore.QRect(230, 360, 61, 23))
        self.pushButton_28.setObjectName("pushButton_28")
        self.stackedWidget.addWidget(self.sidea)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(220, 510, 131, 41))
        self.pushButton_8.setObjectName("pushButton_8")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(370, -10, 501, 61))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(380, 510, 501, 41))
        self.label_20.setObjectName("label_20")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(360, 460, 131, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(3)
        self.stackedWidget_2.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Square a Number"))
        self.pushButton_2.setText(_translate("MainWindow", "Find A"))
        self.pushButton_4.setText(_translate("MainWindow", "Square Root a Number"))
        self.pushButton_5.setText(_translate("MainWindow", "Find B"))
        self.pushButton_6.setText(_translate("MainWindow", "Find C"))
        self.label_2.setText(_translate("MainWindow", "Copyright 2020 Zain Raza"))
        self.label_3.setText(_translate("MainWindow", "Version 2.0"))
        self.pushButton_7.setText(_translate("MainWindow", "Detect Right Triangles"))
        self.pushButton_23.setText(_translate("MainWindow", "Enter"))
        self.label_9.setText(_translate("MainWindow", "Please enter Side A"))
        self.label_10.setText(_translate("MainWindow", "Please enter Side C"))
        self.pushButton_16.setText(_translate("MainWindow", "Clear"))
        self.pushButton_29.setText(_translate("MainWindow", "Copy"))
        self.pushButton_26.setText(_translate("MainWindow", "Enter"))
        self.label_11.setText(_translate("MainWindow", "Please enter Side B"))
        self.label_14.setText(_translate("MainWindow", "Please enter Side A"))
        self.pushButton_17.setText(_translate("MainWindow", "Clear"))
        self.pushButton_30.setText(_translate("MainWindow", "Copy"))
        self.label_15.setText(_translate("MainWindow", "Please enter Side B"))
        self.label_16.setText(_translate("MainWindow", "Please enter Side C"))
        self.label_17.setText(_translate("MainWindow", "Please enter Side A"))
        self.pushButton_27.setText(_translate("MainWindow", "Enter"))
        self.pushButton_19.setText(_translate("MainWindow", "Clear"))
        self.pushButton_31.setText(_translate("MainWindow", "Copy"))
        self.label_8.setText(_translate("MainWindow", "Font Size"))
        self.pushButton_32.setText(_translate("MainWindow", "Reset"))
        self.pushButton_10.setText(_translate("MainWindow", "Enter"))
        self.label_4.setText(_translate("MainWindow", "Please enter the number you would like to square"))
        self.pushButton_11.setText(_translate("MainWindow", "Clear"))
        self.pushButton_22.setText(_translate("MainWindow", "Copy"))
        self.pushButton_12.setText(_translate("MainWindow", "Enter"))
        self.label_6.setText(_translate("MainWindow", "Please enter the number you would like to square"))
        self.label_12.setText(_translate("MainWindow", "Please enter the number you would like to Square Root"))
        self.pushButton_18.setText(_translate("MainWindow", "Enter"))
        self.pushButton_13.setText(_translate("MainWindow", "Clear"))
        self.pushButton_24.setText(_translate("MainWindow", "Copy"))
        self.pushButton_20.setText(_translate("MainWindow", "Enter"))
        self.label_13.setText(_translate("MainWindow", "Please enter the two numbers you would like to add"))
        self.pushButton_14.setText(_translate("MainWindow", "Clear"))
        self.pushButton_25.setText(_translate("MainWindow", "Copy"))
        self.pushButton_21.setText(_translate("MainWindow", "Enter"))
        self.label_5.setText(_translate("MainWindow", "Please enter Side B"))
        self.label_7.setText(_translate("MainWindow", "Please enter Side C"))
        self.pushButton_15.setText(_translate("MainWindow", "Clear"))
        self.pushButton_28.setText(_translate("MainWindow", "Copy"))
        self.pushButton_8.setText(_translate("MainWindow", "Settings"))
        self.label.setText(_translate("MainWindow", "Pythagorean Theorem Calculator"))
        self.label_20.setText(_translate("MainWindow", "Please choose the action you would like to do"))
        self.pushButton_3.setText(_translate("MainWindow", "Add numbers"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

