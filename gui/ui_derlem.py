# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'derlem.ui'
#
# Created: Sun Nov 20 02:08:31 2016
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dlgDerlem(object):
    def setupUi(self, dlgDerlem):
        dlgDerlem.setObjectName("dlgDerlem")
        dlgDerlem.resize(656, 460)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(dlgDerlem)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.editGirdi = QtWidgets.QPlainTextEdit(dlgDerlem)
        self.editGirdi.setObjectName("editGirdi")
        self.verticalLayout.addWidget(self.editGirdi)
        self.editCikti = QtWidgets.QPlainTextEdit(dlgDerlem)
        self.editCikti.setObjectName("editCikti")
        self.verticalLayout.addWidget(self.editCikti)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnSecenekler = QtWidgets.QPushButton(dlgDerlem)
        self.btnSecenekler.setObjectName("btnSecenekler")
        self.horizontalLayout.addWidget(self.btnSecenekler)
        self.btnGirdiDosyasiSec = QtWidgets.QPushButton(dlgDerlem)
        self.btnGirdiDosyasiSec.setObjectName("btnGirdiDosyasiSec")
        self.horizontalLayout.addWidget(self.btnGirdiDosyasiSec)
        self.btnDonustur = QtWidgets.QPushButton(dlgDerlem)
        self.btnDonustur.setObjectName("btnDonustur")
        self.horizontalLayout.addWidget(self.btnDonustur)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnKaydet = QtWidgets.QPushButton(dlgDerlem)
        self.btnKaydet.setObjectName("btnKaydet")
        self.horizontalLayout.addWidget(self.btnKaydet)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(dlgDerlem)
        self.btnSecenekler.clicked.connect(dlgDerlem.secenekler)
        self.btnGirdiDosyasiSec.clicked.connect(dlgDerlem.dosyasec)
        self.btnDonustur.clicked.connect(dlgDerlem.donustur)
        self.btnKaydet.clicked.connect(dlgDerlem.kaydet)
        QtCore.QMetaObject.connectSlotsByName(dlgDerlem)

    def retranslateUi(self, dlgDerlem):
        _translate = QtCore.QCoreApplication.translate
        dlgDerlem.setWindowTitle(_translate("dlgDerlem", "Derlem Uygulamasi"))
        self.btnSecenekler.setText(_translate("dlgDerlem", "Secenekler..."))
        self.btnGirdiDosyasiSec.setText(_translate("dlgDerlem", "Girdi Dosyasi Sec"))
        self.btnDonustur.setText(_translate("dlgDerlem", "Dönüştür"))
        self.btnKaydet.setText(_translate("dlgDerlem", "Kaydet"))

