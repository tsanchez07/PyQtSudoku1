# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MenuInicial.ui'
#
# Created: Fri Jul 19 12:54:03 2013
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MenuInicial(object):
    def setupUi(self, MenuInicial):
        MenuInicial.setObjectName(_fromUtf8("MenuInicial"))
        MenuInicial.setWindowModality(QtCore.Qt.WindowModal)
        MenuInicial.resize(793, 516)
        MenuInicial.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MenuInicial.setStyleSheet(_fromUtf8("font: 75 16pt \"Gabriola\";\n"
"background-image: url(fondo1.png);\n"
""))
        MenuInicial.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtGui.QWidget(MenuInicial)
        self.centralwidget.setStyleSheet(_fromUtf8(""))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 793, 516))
        self.label.setStyleSheet(_fromUtf8("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 175, 205, 255), stop:1 rgba(26, 163, 184, 255));\n"
"image: url(:/image/imagen/fondo.png);\n"
"\n"
"   "))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(580, 440, 100, 37))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gabriola"))
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(_fromUtf8("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(1, 147, 176, 255), stop:1 rgba(19, 117, 135, 255));\n"
"color: rgb(255, 255, 255);\n"
""))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(430, 440, 100, 37))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gabriola"))
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(_fromUtf8("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(1, 147, 176, 255), stop:1 rgba(19, 117, 135, 255));\n"
"color: rgb(255, 255, 255);\n"
""))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 440, 100, 37))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gabriola"))
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(_fromUtf8("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(1, 147, 176, 255), stop:1 rgba(19, 117, 135, 255));\n"
"color: rgb(255, 255, 255);\n"
""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 440, 100, 37))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gabriola"))
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(1, 147, 176, 255), stop:1 rgba(19, 117, 135, 255));\n"
"color: rgb(255, 255, 255);\n"
""))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        MenuInicial.setCentralWidget(self.centralwidget)

        self.retranslateUi(MenuInicial)
        QtCore.QMetaObject.connectSlotsByName(MenuInicial)

    def retranslateUi(self, MenuInicial):
        MenuInicial.setWindowTitle(_translate("MenuInicial", "Menú Principal", None))
        self.pushButton_4.setText(_translate("MenuInicial", "Salir", None))
        self.pushButton_3.setText(_translate("MenuInicial", "Top", None))
        self.pushButton.setText(_translate("MenuInicial", "Jugar", None))
        self.pushButton_2.setText(_translate("MenuInicial", "Instrucciones", None))

import fondo_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MenuInicial = QtGui.QMainWindow()
    ui = Ui_MenuInicial()
    ui.setupUi(MenuInicial)
    MenuInicial.show()
    sys.exit(app.exec_())

