# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'daphuongtien_gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 131, 22))
        self.label.setAutoFillBackground(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 20, 151, 21))
        self.label_2.setObjectName("label_2")
        self.imageOriginal = QtWidgets.QLabel(self.centralwidget)
        self.imageOriginal.setGeometry(QtCore.QRect(20, 50, 211, 421))
        self.imageOriginal.setAutoFillBackground(True)
        self.imageOriginal.setScaledContents(True)
        self.imageOriginal.setObjectName("imageOriginal")
        self.imageCompression = QtWidgets.QLabel(self.centralwidget)
        self.imageCompression.setGeometry(QtCore.QRect(250, 50, 241, 421))
        self.imageCompression.setObjectName("imageCompression")
        self.chooseImage = QtWidgets.QPushButton(self.centralwidget)
        self.chooseImage.setGeometry(QtCore.QRect(20, 480, 131, 31))
        self.chooseImage.setObjectName("chooseImage")
        self.Compression = QtWidgets.QPushButton(self.centralwidget)
        self.Compression.setGeometry(QtCore.QRect(280, 480, 161, 31))
        self.Compression.setAutoFillBackground(True)
        self.Compression.setObjectName("Compression")
        self.Decompress = QtWidgets.QPushButton(self.centralwidget)
        self.Decompress.setGeometry(QtCore.QRect(540, 480, 161, 31))
        self.Decompress.setAutoFillBackground(True)
        self.Decompress.setObjectName("Decompress")
        self.imageDecodempression = QtWidgets.QLabel(self.centralwidget)
        self.imageDecodempression.setGeometry(QtCore.QRect(510, 50, 261, 421))
        self.imageDecodempression.setAutoFillBackground(True)
        self.imageDecodempression.setObjectName("imageDecodempression")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(540, 20, 151, 21))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GUI app for compression image"))
        self.label.setText(_translate("MainWindow", "Original Image"))
        self.label_2.setText(_translate("MainWindow", "Compression Image"))
        self.imageOriginal.setText(_translate("MainWindow", "TextLabel"))
        self.imageCompression.setText(_translate("MainWindow", "TextLabel"))
        self.chooseImage.setText(_translate("MainWindow", "Browse Image"))
        self.Compression.setText(_translate("MainWindow", "Compress Image"))
        self.Decompress.setText(_translate("MainWindow", "Decompress Image"))
        self.imageDecodempression.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "Decompression Image"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

