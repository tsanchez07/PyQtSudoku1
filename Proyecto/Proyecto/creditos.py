# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'creditos.ui'
#
# Created: Fri Jul 19 10:48:43 2013
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

class Ui_Creditos(object):
    def setupUi(self, Creditos):
        Creditos.setObjectName(_fromUtf8("Creditos"))
        Creditos.resize(411, 241)
        self.label = QtGui.QLabel(Creditos)
        self.label.setGeometry(QtCore.QRect(140, 20, 141, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gabriola"))
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("font: 75 20pt \"Gabriola\";\n"
"color: rgb(255, 255, 255);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Creditos)
        self.label_2.setGeometry(QtCore.QRect(160, 70, 110, 15))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Creditos)
        self.label_3.setGeometry(QtCore.QRect(160, 100, 110, 15))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Creditos)
        self.label_4.setGeometry(QtCore.QRect(160, 130, 110, 15))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton = QtGui.QPushButton(Creditos)
        self.pushButton.setGeometry(QtCore.QRect(230, 190, 100, 37))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(_fromUtf8("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(1, 147, 176, 255), stop:1 rgba(19, 117, 135, 255));\n"
"color: rgb(255, 255, 255);\n"
""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.btn_VolverMenu = QtGui.QPushButton(Creditos)
        self.btn_VolverMenu.setGeometry(QtCore.QRect(100, 190, 100, 37))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_VolverMenu.setFont(font)
        self.btn_VolverMenu.setStyleSheet(_fromUtf8("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(1, 147, 176, 255), stop:1 rgba(19, 117, 135, 255));\n"
"color: rgb(255, 255, 255);\n"
""))
        self.btn_VolverMenu.setObjectName(_fromUtf8("btn_VolverMenu"))
        self.label_5 = QtGui.QLabel(Creditos)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 411, 241))
        self.label_5.setStyleSheet(_fromUtf8("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 175, 205, 255), stop:1 rgba(26, 163, 184, 255));"))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.retranslateUi(Creditos)
        QtCore.QMetaObject.connectSlotsByName(Creditos)

    def retranslateUi(self, Creditos):
        Creditos.setWindowTitle(_translate("Creditos", "Dialog", None))
        self.label.setText(_translate("Creditos", "Desarrolladores", None))
        self.label_2.setText(_translate("Creditos", "- Romero Juan", None))
        self.label_3.setText(_translate("Creditos", "- Sánchez Tania", None))
        self.label_4.setText(_translate("Creditos", "- Sanga Joao", None))
        self.pushButton.setText(_translate("Creditos", "Salir", None))
        self.btn_VolverMenu.setText(_translate("Creditos", "Volver al Menú", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Creditos = QtGui.QDialog()
    ui = Ui_Creditos()
    ui.setupUi(Creditos)
    Creditos.show()
    sys.exit(app.exec_())

