# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from CategoryRequester import CategoryRequester
from NewsRequester import NewsRequester


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 190, 47, 13))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Test"))


if __name__ == "__main__":
    # import sys
    # app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_())
    requester_cat = CategoryRequester()
    requester_news = NewsRequester()
    # print(requester_cat.get_category_by_id(1))
    # print("--------------------------------------")
    # print(requester_cat.create_category("ebola xd"))
    # print("--------------------------------------")
    # print(requester_cat.delete_category(1))
    # print("--------------------------------------")
    # print(requester_cat.get_all_category())
    # print("--------------------------------------")
    # print(requester_news.create_news("test nazwa", "opis", "31/12/1998 12:12:12", 4))
    # print("--------------------------------------")
    # print(requester_news.create_news("test nazwa", "opis", "31/12/1998 12:12:12", 3))
    # print("--------------------------------------")
    # print(requester_news.get_all_news())
    # print("--------------------------------------")
    # print(requester_news.get_news_by_id(7))
    # print("--------------------------------------")
    # print(requester_news.delete_news(9))
    # print("--------------------------------------")
    # print(requester_news.get_all_news())
    # print("--------------------------------------")
    # print(requester_news.get_all_news())
    # print("--------------------------------------")
    # print(requester_cat.get_all_category())
    # print("--------------------------------------")
    # print(requester_cat.delete_category(3))
    # print("--------------------------------------")
    # print(requester_cat.get_all_category())
    # print("--------------------------------------")
    # print(requester_news.store_file("C:/Users/exomat/Desktop/zordon.png",3))
    # print("--------------------------------------")
    print(requester_news.get_all_news())
    print(requester_news.load_file("files\\3_uwagaklątwafaraona\\zordon.png"))

