# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'instrucciones.ui'
#
# Created: Fri Jul 19 10:49:19 2013
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

class Ui_Instrucciones(object):
    def setupUi(self, Instrucciones):
        Instrucciones.setObjectName(_fromUtf8("Instrucciones"))
        Instrucciones.resize(535, 415)
        self.label = QtGui.QLabel(Instrucciones)
        self.label.setGeometry(QtCore.QRect(0, 0, 535, 415))
        self.label.setStyleSheet(_fromUtf8("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 175, 205, 255), stop:1 rgba(26, 163, 184, 255));"))
        self.label.setText(_fromUtf8(""))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Instrucciones)
        self.label_2.setGeometry(QtCore.QRect(0, 20, 535, 415))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gabriola"))
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(Instrucciones)
        QtCore.QMetaObject.connectSlotsByName(Instrucciones)

    def retranslateUi(self, Instrucciones):
        Instrucciones.setWindowTitle(_translate("Instrucciones", "Form", None))
        self.label_2.setText(_translate("Instrucciones", "SUDOKU\n"
"Este juego consiste en rellenar con números del  1 al 9 todas las casillas\n"
"existentes de la parrilla, la cual se compone de 9 filas y 9 columnas ( 9 X 9 ) y a\n"
"su vez estas 81 casillas, que se dividen en otras 9 cuadrillas de 3X3. Hay que\n"
"tener en cuenta que no pueden coincidir 2 números iguales en la misma fila, en\n"
"la misma columna, ni en la misma cuadrilla.\n"
"\n"
"Un Sudoku tiene una única solución, en caso de que se repita un numero en la\n"
"misma fila, en la misma columna o en la misma cuadrilla dicho numero será\n"
"marcado con rojo.\n"
"\n"
"Para poder realizar el juego se facilitan, correctamente rellenadas, unas\n"
"casillas  con el cual te podrás guiar para empezar tu juego.\n"
"", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Instrucciones = QtGui.QWidget()
    ui = Ui_Instrucciones()
    ui.setupUi(Instrucciones)
    Instrucciones.show()
    sys.exit(app.exec_())

