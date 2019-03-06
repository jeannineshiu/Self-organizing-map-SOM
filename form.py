# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(889, 643)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(290, 30, 341, 21))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(680, 40, 141, 16))
        self.label_2.setObjectName("label_2")
        self.btopenfile = QtWidgets.QPushButton(Form)
        self.btopenfile.setGeometry(QtCore.QRect(390, 60, 114, 32))
        self.btopenfile.setObjectName("btopenfile")
        self.filenamelabel = QtWidgets.QLabel(Form)
        self.filenamelabel.setGeometry(QtCore.QRect(400, 100, 101, 16))
        self.filenamelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.filenamelabel.setObjectName("filenamelabel")
        self.mplwidget1 = MplWidget(Form)
        self.mplwidget1.setGeometry(QtCore.QRect(20, 150, 411, 411))
        self.mplwidget1.setObjectName("mplwidget1")
        self.mplwidget2 = MplWidget(Form)
        self.mplwidget2.setGeometry(QtCore.QRect(460, 150, 411, 411))
        self.mplwidget2.setObjectName("mplwidget2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(200, 120, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(560, 120, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.btrun = QtWidgets.QPushButton(Form)
        self.btrun.setGeometry(QtCore.QRect(390, 580, 111, 41))
        self.btrun.setObjectName("btrun")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Neural Networks HW3 - SOM"))
        self.label_2.setText(_translate("Form", "104103025許嘉茵"))
        self.btopenfile.setText(_translate("Form", "Open file"))
        self.filenamelabel.setText(_translate("Form", "filename"))
        self.label_3.setText(_translate("Form", "Result"))
        self.label_4.setText(_translate("Form", "Result- Normalized"))
        self.btrun.setText(_translate("Form", "Run"))

from mplwidget import MplWidget
