# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\coding\python\MyCloud\qt\UI\transfer.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TransferWindow(object):
    def setupUi(self, TransferWindow):
        TransferWindow.setObjectName("TransferWindow")
        TransferWindow.resize(771, 701)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        TransferWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(TransferWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(100, 80, 571, 521))
        self.stackedWidget.setObjectName("stackedWidget")
        self.download_page = QtWidgets.QWidget()
        self.download_page.setObjectName("download_page")
        self.download_w = QtWidgets.QTableWidget(self.download_page)
        self.download_w.setGeometry(QtCore.QRect(0, 0, 571, 521))
        self.download_w.setObjectName("download_w")
        self.download_w.setColumnCount(1)
        self.download_w.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.download_w.setHorizontalHeaderItem(0, item)
        self.stackedWidget.addWidget(self.download_page)
        self.upload_page = QtWidgets.QWidget()
        self.upload_page.setObjectName("upload_page")
        self.upload_w = QtWidgets.QTableWidget(self.upload_page)
        self.upload_w.setGeometry(QtCore.QRect(0, 0, 571, 521))
        self.upload_w.setObjectName("upload_w")
        self.upload_w.setColumnCount(1)
        self.upload_w.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.upload_w.setHorizontalHeaderItem(0, item)
        self.stackedWidget.addWidget(self.upload_page)
        self.complete_page = QtWidgets.QWidget()
        self.complete_page.setObjectName("complete_page")
        self.complete_w = QtWidgets.QTableWidget(self.complete_page)
        self.complete_w.setGeometry(QtCore.QRect(0, 0, 571, 521))
        self.complete_w.setObjectName("complete_w")
        self.complete_w.setColumnCount(1)
        self.complete_w.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.complete_w.setHorizontalHeaderItem(0, item)
        self.stackedWidget.addWidget(self.complete_page)
        self.no_download_page = QtWidgets.QWidget()
        self.no_download_page.setObjectName("no_download_page")
        self.no_download_w = QtWidgets.QListWidget(self.no_download_page)
        self.no_download_w.setGeometry(QtCore.QRect(0, 0, 571, 521))
        self.no_download_w.setObjectName("no_download_w")
        self.label = QtWidgets.QLabel(self.no_download_page)
        self.label.setGeometry(QtCore.QRect(210, 160, 141, 121))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.no_download_page)
        self.label_2.setGeometry(QtCore.QRect(200, 310, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.no_download_page)
        self.no_upload_page = QtWidgets.QWidget()
        self.no_upload_page.setObjectName("no_upload_page")
        self.no_upload_w = QtWidgets.QListWidget(self.no_upload_page)
        self.no_upload_w.setGeometry(QtCore.QRect(0, 0, 571, 521))
        self.no_upload_w.setObjectName("no_upload_w")
        self.label_4 = QtWidgets.QLabel(self.no_upload_page)
        self.label_4.setGeometry(QtCore.QRect(210, 160, 141, 121))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.no_upload_page)
        self.label_5.setGeometry(QtCore.QRect(200, 310, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.stackedWidget.addWidget(self.no_upload_page)
        self.no_complete_page = QtWidgets.QWidget()
        self.no_complete_page.setObjectName("no_complete_page")
        self.label_3 = QtWidgets.QLabel(self.no_complete_page)
        self.label_3.setGeometry(QtCore.QRect(210, 160, 141, 121))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.no_complete_page)
        self.label_6.setGeometry(QtCore.QRect(200, 310, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.listWidget = QtWidgets.QListWidget(self.no_complete_page)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 571, 521))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.raise_()
        self.label_3.raise_()
        self.label_6.raise_()
        self.stackedWidget.addWidget(self.no_complete_page)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(100, 40, 571, 41))
        self.widget_2.setObjectName("widget_2")
        self.upload_btn = QtWidgets.QPushButton(self.widget_2)
        self.upload_btn.setGeometry(QtCore.QRect(110, 0, 111, 41))
        self.upload_btn.setObjectName("upload_btn")
        self.download_btn = QtWidgets.QPushButton(self.widget_2)
        self.download_btn.setGeometry(QtCore.QRect(0, 0, 111, 41))
        self.download_btn.setObjectName("download_btn")
        self.complete_btn = QtWidgets.QPushButton(self.widget_2)
        self.complete_btn.setGeometry(QtCore.QRect(220, 0, 111, 41))
        self.complete_btn.setObjectName("complete_btn")
        self.closeButton = QtWidgets.QPushButton(self.widget_2)
        self.closeButton.setGeometry(QtCore.QRect(530, 0, 41, 41))
        self.closeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.closeButton.setText("")
        self.closeButton.setObjectName("closeButton")
        self.minButton = QtWidgets.QPushButton(self.widget_2)
        self.minButton.setGeometry(QtCore.QRect(490, 0, 41, 41))
        self.minButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.minButton.setText("")
        self.minButton.setObjectName("minButton")
        TransferWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(TransferWindow)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(TransferWindow)

    def retranslateUi(self, TransferWindow):
        _translate = QtCore.QCoreApplication.translate
        TransferWindow.setWindowTitle(_translate("TransferWindow", "TransferWindow"))
        item = self.download_w.horizontalHeaderItem(0)
        item.setText(_translate("TransferWindow", "正在下载"))
        item = self.upload_w.horizontalHeaderItem(0)
        item.setText(_translate("TransferWindow", "正在上传"))
        item = self.complete_w.horizontalHeaderItem(0)
        item.setText(_translate("TransferWindow", "传输完成"))
        self.label_2.setText(_translate("TransferWindow", "当前没有下载任务哦"))
        self.label_5.setText(_translate("TransferWindow", "当前没有上传任务哦"))
        self.label_6.setText(_translate("TransferWindow", "当前没有传输记录哦"))
        self.upload_btn.setText(_translate("TransferWindow", "正在上传"))
        self.download_btn.setText(_translate("TransferWindow", "正在下载"))
        self.complete_btn.setText(_translate("TransferWindow", "传输完成"))