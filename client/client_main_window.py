# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from CategoryRequester import CategoryRequester
from NewsRequester import NewsRequester
from login_to_admin_panel_window import Ui_LoginAdminPanel
from news_details_window import Ui_NewsDetailsWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.main_window = MainWindow
        self.category_requester = CategoryRequester()
        self.news_requester = NewsRequester()
        self.newsList = None
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1280, 900)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 900))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 900))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 200, 321, 211))
        self.calendarWidget.setDateEditEnabled(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.epidemyComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.epidemyComboBox.setGeometry(QtCore.QRect(10, 130, 321, 22))
        self.epidemyComboBox.setObjectName("epidemyComboBox")
        self.searchByEpidemyLabel = QtWidgets.QLabel(self.centralwidget)
        self.searchByEpidemyLabel.setGeometry(QtCore.QRect(10, 100, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.searchByEpidemyLabel.setFont(font)
        self.searchByEpidemyLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.searchByEpidemyLabel.setObjectName("searchByEpidemyLabel")
        self.headerLabel = QtWidgets.QLabel(self.centralwidget)
        self.headerLabel.setGeometry(QtCore.QRect(0, 0, 1281, 101))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(24)
        self.headerLabel.setFont(font)
        self.headerLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.headerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.headerLabel.setWordWrap(False)
        self.headerLabel.setObjectName("headerLabel")
        self.searchByDateLabel = QtWidgets.QLabel(self.centralwidget)
        self.searchByDateLabel.setGeometry(QtCore.QRect(10, 170, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.searchByDateLabel.setFont(font)
        self.searchByDateLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.searchByDateLabel.setObjectName("searchByDateLabel")
        self.adminPanelButton = QtWidgets.QPushButton(self.centralwidget)
        self.adminPanelButton.setGeometry(QtCore.QRect(10, 870, 141, 23))
        self.adminPanelButton.setObjectName("adminPanelButton")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(360, 100, 911, 791))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.itemDoubleClicked.connect(self.show_news_details)
        MainWindow.setCentralWidget(self.centralwidget)
        self.populateInfoList()
        self.updateInfoList()
        self.adminPanelButton.clicked.connect(self.open_admin_panel)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.searchByEpidemyLabel.setText(_translate("MainWindow", "Wyszukaj po epidemii"))
        self.headerLabel.setText(_translate("MainWindow", "Soap News Epidemic Service"))
        self.searchByDateLabel.setText(_translate("MainWindow", "Wyszukaj po dacie"))
        self.adminPanelButton.setText(_translate("MainWindow", "Zaloguj do panelu admina"))

    def open_admin_panel(self):
        self.LoginAdminPanel = QtWidgets.QMainWindow()
        self.admin_login_panel_ui = Ui_LoginAdminPanel()
        self.admin_login_panel_ui.setupUi(self.LoginAdminPanel)
        self.LoginAdminPanel.show()
        self.main_window.hide()

    def populateInfoList(self):
        self.newsList = self.news_requester.get_all_news()
        print(self.newsList)

    def updateInfoList(self):
        for i in self.newsList:
            item = QtWidgets.QListWidgetItem(
                str("Epidemia: " + i.categoryName + "\nData: " + i.date + "  Tytuł: " + i.name), self.listWidget)
            item.setData(1, i.id)

    def show_news_details(self, item):
        self.NewsDetailsWindow = QtWidgets.QMainWindow()
        self.news_details_window_ui = Ui_NewsDetailsWindow()
        self.news_details_window_ui.setupUi(self.NewsDetailsWindow, item.data(1))
        self.NewsDetailsWindow.show()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
