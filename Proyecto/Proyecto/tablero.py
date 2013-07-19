# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tablero.ui'
#
# Created: Fri Jul 19 10:50:23 2013
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

class Ui_Tablero(object):
    def setupUi(self, Tablero):
        Tablero.setObjectName(_fromUtf8("Tablero"))
        Tablero.resize(575, 502)
        self.centralwidget = QtGui.QWidget(Tablero)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 391, 451))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 210, 100, 37))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(_fromUtf8("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(1, 147, 176, 255), stop:1 rgba(19, 117, 135, 255));\n"
"color: rgb(255, 255, 255);\n"
""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 270, 100, 37))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(1, 147, 176, 255), stop:1 rgba(19, 117, 135, 255));\n"
"color: rgb(255, 255, 255);\n"
""))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(450, 60, 81, 41))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.cronometroLayout = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.cronometroLayout.setMargin(0)
        self.cronometroLayout.setObjectName(_fromUtf8("cronometroLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 575, 502))
        self.label.setStyleSheet(_fromUtf8("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(33, 208, 238, 255), stop:1 rgba(26, 163, 184, 255));"))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(19, 169, 390, 4))
        self.line.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 127);"))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(19, 321, 390, 4))
        self.line_2.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 127);"))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(149, 20, 4, 449))
        self.line_3.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 127);"))
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(280, 20, 4, 449))
        self.line_4.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 127);"))
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.line_5 = QtGui.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(20, 469, 390, 4))
        self.line_5.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 127);"))
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.line_6 = QtGui.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(20, 20, 390, 4))
        self.line_6.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 127);"))
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.line_7 = QtGui.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(20, 20, 4, 449))
        self.line_7.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 127);"))
        self.line_7.setFrameShape(QtGui.QFrame.VLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.line_8 = QtGui.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(410, 20, 4, 449))
        self.line_8.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 127);"))
        self.line_8.setFrameShape(QtGui.QFrame.VLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        Tablero.setCentralWidget(self.centralwidget)

        self.retranslateUi(Tablero)
        QtCore.QMetaObject.connectSlotsByName(Tablero)

    def retranslateUi(self, Tablero):
        Tablero.setWindowTitle(_translate("Tablero", "MainWindow", None))
        self.pushButton.setText(_translate("Tablero", "Guardar y salir", None))
        self.pushButton_2.setText(_translate("Tablero", "Salir", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Tablero = QtGui.QMainWindow()
    ui = Ui_Tablero()
    ui.setupUi(Tablero)
    Tablero.show()
    sys.exit(app.exec_())

