# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'secenekler.ui'
#
# Created: Sun Nov 20 02:08:31 2016
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(216, 152)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.chkStopword = QtWidgets.QCheckBox(Dialog)
        self.chkStopword.setObjectName("chkStopword")
        self.verticalLayout.addWidget(self.chkStopword)
        self.chkEnuzunkok = QtWidgets.QCheckBox(Dialog)
        self.chkEnuzunkok.setObjectName("chkEnuzunkok")
        self.verticalLayout.addWidget(self.chkEnuzunkok)
        self.chkTumKokleriListele = QtWidgets.QCheckBox(Dialog)
        self.chkTumKokleriListele.setObjectName("chkTumKokleriListele")
        self.verticalLayout.addWidget(self.chkTumKokleriListele)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.close)
        self.pushButton_2.clicked.connect(Dialog.secenekKaydet)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Secenekler"))
        self.chkStopword.setText(_translate("Dialog", "Stopword temizligi"))
        self.chkEnuzunkok.setText(_translate("Dialog", "En uzun kok"))
        self.chkTumKokleriListele.setText(_translate("Dialog", "Tum kokleri listele"))
        self.pushButton.setText(_translate("Dialog", "Kapat"))
        self.pushButton_2.setText(_translate("Dialog", "Kaydet"))

