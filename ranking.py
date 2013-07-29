# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ranking.ui'
#
# Created: Fri Jul 19 10:50:11 2013
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

class Ui_Ranking(object):
    def setupUi(self, Ranking):
        Ranking.setObjectName(_fromUtf8("Ranking"))
        Ranking.resize(525, 322)
        Ranking.setStyleSheet(_fromUtf8("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(33, 208, 238, 255), stop:1 rgba(26, 163, 184, 255));"))
        self.pushButton = QtGui.QPushButton(Ranking)
        self.pushButton.setGeometry(QtCore.QRect(230, 280, 100, 37))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(_fromUtf8("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(1, 147, 176, 255), stop:1 rgba(19, 117, 135, 255));\n"
"color: rgb(255, 255, 255);\n"
""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Ranking)
        QtCore.QMetaObject.connectSlotsByName(Ranking)

    def retranslateUi(self, Ranking):
        Ranking.setWindowTitle(_translate("Ranking", "Dialog", None))
        self.pushButton.setText(_translate("Ranking", "PushButton", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Ranking = QtGui.QDialog()
    ui = Ui_Ranking()
    ui.setupUi(Ranking)
    Ranking.show()
    sys.exit(app.exec_())

