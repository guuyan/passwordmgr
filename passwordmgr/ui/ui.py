# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName(_fromUtf8("login"))
        login.setWindowModality(QtCore.Qt.NonModal)
        login.resize(311, 444)
        self.centralwidget = QtGui.QWidget(login)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 220, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 281, 211))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(130, 20, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 80, 113, 20))
        self.lineEdit_2.setEchoMode(QtGui.QLineEdit.PasswordEchoOnEdit)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        login.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(login)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 311, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        login.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(login)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        login.setStatusBar(self.statusbar)

        self.retranslateUi(login)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        login.setWindowTitle(_translate("login", "login", None))
        self.pushButton.setText(_translate("login", "PushButton", None))
        self.groupBox.setTitle(_translate("login", "GroupBox", None))

