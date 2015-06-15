# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created: Mon Jun 15 17:47:02 2015
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(618, 496)
        Dialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.searchBox = QtWidgets.QLineEdit(Dialog)
        self.searchBox.setObjectName("searchBox")
        self.gridLayout.addWidget(self.searchBox, 0, 0, 1, 1)
        self.searchButton = QtWidgets.QPushButton(Dialog)
        self.searchButton.setObjectName("searchButton")
        self.gridLayout.addWidget(self.searchButton, 0, 1, 1, 1)
        self.searchResults = QtWidgets.QListView(Dialog)
        self.searchResults.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.searchResults.setObjectName("searchResults")
        self.gridLayout.addWidget(self.searchResults, 1, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Search for IMSLP Score"))
        self.searchBox.setPlaceholderText(_translate("Dialog", "Search for IMSLP Score"))
        self.searchButton.setText(_translate("Dialog", "Go"))

