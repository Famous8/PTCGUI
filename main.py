import sys
import math
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import (QApplication, QMainWindow,)
from PyQt5 import QtWidgets
from PyQt5.QtGui import (QIcon)

import PTCGUI


class MainWindow (QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = PTCGUI.Ui_MainWindow()
        self.ui.setupUi(self)
        width = 923
        height = 624
        title = ("Pythagorean Theorem Calculator")
        self.setWindowTitle(title)
        self.setFixedSize(width, height)
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)
        self.setWindowIcon(QIcon("C:\\Users\\Owner\\Documents\\PTCGUI-fbs\\src\\main\\icons\\icon.ico"))

        #home page buttons
        self.ui.pushButton.clicked.connect(self.sqrnum)
        self.ui.pushButton_4.clicked.connect(self.sqrtnum)
        self.ui.pushButton_3.clicked.connect(self.addnum)
        self.ui.pushButton_2.clicked.connect(self.sidea)
        self.ui.pushButton_5.clicked.connect(self.sideb)
        self.ui.pushButton_6.clicked.connect(self.sidec)
        self.ui.pushButton_7.clicked.connect(self.dettri)
        self.ui.pushButton_8.clicked.connect(self.settings)
        #enter buttons
        self.ui.pushButton_10.clicked.connect(self.showsqr)
        self.ui.pushButton_18.clicked.connect(self.showsqrt)
        self.ui.pushButton_20.clicked.connect(self.add)
        self.ui.pushButton_21.clicked.connect(self.funca)
        self.ui.pushButton_23.clicked.connect(self.funcb)
        self.ui.pushButton_26.clicked.connect(self.funcc)
        self.ui.pushButton_27.clicked.connect(self.frtg)
        #clear buttons
        self.ui.pushButton_11.clicked.connect(self.ui.lineEdit.clear)
        self.ui.pushButton_11.clicked.connect(self.ui.lineEdit_2.clear)
        self.ui.pushButton_13.clicked.connect(self.ui.lineEdit_17.clear)
        self.ui.pushButton_13.clicked.connect(self.ui.lineEdit_18.clear)
        self.ui.pushButton_14.clicked.connect(self.ui.lineEdit_19.clear)
        self.ui.pushButton_14.clicked.connect(self.ui.lineEdit_20.clear)
        self.ui.pushButton_14.clicked.connect(self.ui.lineEdit_21.clear)
        self.ui.pushButton_15.clicked.connect(self.ui.lineEdit_22.clear)
        self.ui.pushButton_15.clicked.connect(self.ui.lineEdit_23.clear)
        self.ui.pushButton_15.clicked.connect(self.ui.lineEdit_24.clear)
        self.ui.pushButton_16.clicked.connect(self.ui.lineEdit_25.clear)
        self.ui.pushButton_16.clicked.connect(self.ui.lineEdit_26.clear)
        self.ui.pushButton_16.clicked.connect(self.ui.lineEdit_27.clear)
        self.ui.pushButton_17.clicked.connect(self.ui.lineEdit_28.clear)
        self.ui.pushButton_17.clicked.connect(self.ui.lineEdit_29.clear)
        self.ui.pushButton_17.clicked.connect(self.ui.lineEdit_30.clear)
        self.ui.pushButton_19.clicked.connect(self.ui.lineEdit_31.clear)
        self.ui.pushButton_19.clicked.connect(self.ui.lineEdit_32.clear)
        self.ui.pushButton_19.clicked.connect(self.ui.lineEdit_33.clear)
        self.ui.pushButton_19.clicked.connect(self.ui.lineEdit_34.clear)
        #copy buttons
        self.ui.pushButton_22.clicked.connect(self.copysqr)
        self.ui.pushButton_24.clicked.connect(self.copysqrt)
        self.ui.pushButton_25.clicked.connect(self.copyadd)
        self.ui.pushButton_28.clicked.connect(self.copy_a)
        self.ui.pushButton_29.clicked.connect(self.copy_b)
        self.ui.pushButton_30.clicked.connect(self.copy_c)
        #labels

        #settings
        self.ui.spinBox.setMinimum(11)
        self.ui.spinBox.valueChanged.connect(self.fontChange)
        self.ui.pushButton_32.clicked.connect(self.reset)






    def sqrnum(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Square)

    def sqrtnum(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.sqrt)

    def addnum(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.add)

    def sidea(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.sidea)

    def sideb(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.sideb)

    def sidec(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.sidec)

    def dettri(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.righttriangle)

    def settings(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Settings)




    def showsqr(self):
        s1 = float(self.ui.lineEdit.text())
        squared = s1*s1
        self.s2 = str(squared)
        self.ui.lineEdit_2.setText(self.s2)


    def showsqrt(self):
        sq1 = float(self.ui.lineEdit_18.text())
        squareRoot = (math.sqrt(sq1))
        self.sq2 = str(squareRoot)
        self.ui.lineEdit_17.setText(self.sq2)

    def add(self):
        add1 = float(self.ui.lineEdit_19.text())
        add2 = float(self.ui.lineEdit_20.text())
        sum = add1 + add2
        self.add3 = str(sum)
        self.ui.lineEdit_21.setText(self.add3)

    def funca(self):
        b1 = float(self.ui.lineEdit_22.text())
        c1 = float(self.ui.lineEdit_23.text())
        math_a = math.sqrt(abs(c1**2 - b1**2))
        self.sida = str(math_a)
        self.ui.lineEdit_24.setText(self.sida)

    def funcb(self):
        a1 = float(self.ui.lineEdit_27.text())
        c2 = float(self.ui.lineEdit_26.text())
        math_b = math.sqrt(abs(c2**2 - a1**2))
        self.sidb = str(math_b)
        self.ui.lineEdit_25.setText(self.sidb)

    def funcc(self):
        a2 = float(self.ui.lineEdit_28.text())
        b3 = float(self.ui.lineEdit_29.text())
        math_c = math.sqrt(abs(a2**2 + b3**2))
        self.sidc = str(math_c)
        self.ui.lineEdit_30.setText(self.sidc)

    def frtg(self):
        sa = float(self.ui.lineEdit_31.text())
        sb = float(self.ui.lineEdit_32.text())
        sc = float(self.ui.lineEdit_33.text())

        if sc == math.sqrt(sa * sa + sb * sb):
          self.ui.lineEdit_34.setText("This Triangle is a Right Triangle")
        else:
          self.ui.lineEdit_34.setText("This Triangle is not a Right Triangle")



    def copysqr(self):
        clipboard = QApplication.clipboard()
        clipboard.clear(mode=clipboard.Clipboard)
        clipboard.setText(self.s2,mode=clipboard.Clipboard)

    def copysqrt(self):
        clipboard = QApplication.clipboard()
        clipboard.clear(mode=clipboard.Clipboard)
        clipboard.setText(self.sq2,mode=clipboard.Clipboard)

    def copyadd(self):
        clipboard = QApplication.clipboard()
        clipboard.clear(mode=clipboard.Clipboard)
        clipboard.setText(self.add3,mode=clipboard.Clipboard)

    def copy_a(self):
        clipboard = QApplication.clipboard()
        clipboard.clear(mode=clipboard.Clipboard)
        clipboard.setText(self.sida , mode=clipboard.Clipboard)

    def copy_b(self):
        clipboard = QApplication.clipboard()
        clipboard.clear(mode=clipboard.Clipboard)
        clipboard.setText(self.sidb,mode=clipboard.Clipboard)

    def copy_c(self):
        clipboard = QApplication.clipboard()
        clipboard.clear(mode=clipboard.Clipboard)
        clipboard.setText(self.sidc,mode=clipboard.Clipboard)

    def fontChange(self):
        value = self.ui.spinBox.value()
        self.ui.centralwidget.setStyleSheet(f"font-size: {value}px")

    def reset(self):
        self.ui.centralwidget.setStyleSheet(f"font-size: {11}px")
        self.ui.spinBox.setValue(11)




if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    appctxt = ApplicationContext()
    MyWindow = MainWindow()
    MyWindow.show()
    sys.exit(appctxt.app.exec_())