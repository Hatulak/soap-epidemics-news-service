# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_to_admin_panel_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from CategoryRequester import CategoryRequester
from admin_panel_window import Ui_AdminPanelWindow


class Ui_LoginAdminPanel(object):
    def setupUi(self, LoginAdminPanel):
        self.category_requester = CategoryRequester()
        self.login_admin_panel = LoginAdminPanel
        LoginAdminPanel.setObjectName("LoginAdminPanel")
        LoginAdminPanel.resize(201, 174)
        self.centralwidget = QtWidgets.QWidget(LoginAdminPanel)
        self.centralwidget.setObjectName("centralwidget")
        self.header = QtWidgets.QLabel(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(0, 0, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.header.setFont(font)
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setObjectName("header")
        self.loginLabel = QtWidgets.QLabel(self.centralwidget)
        self.loginLabel.setGeometry(QtCore.QRect(10, 70, 41, 16))
        self.loginLabel.setObjectName("loginLabel")
        self.passwordLabel = QtWidgets.QLabel(self.centralwidget)
        self.passwordLabel.setGeometry(QtCore.QRect(10, 100, 41, 16))
        self.passwordLabel.setObjectName("passwordLabel")
        self.loginLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.loginLineEdit.setGeometry(QtCore.QRect(60, 70, 113, 20))
        self.loginLineEdit.setObjectName("loginLineEdit")
        self.passwordLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordLineEdit.setGeometry(QtCore.QRect(60, 100, 113, 20))
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(100, 140, 75, 23))
        self.loginButton.setObjectName("loginButton")
        self.loginButton.clicked.connect(self.login)
        LoginAdminPanel.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginAdminPanel)
        QtCore.QMetaObject.connectSlotsByName(LoginAdminPanel)

    def retranslateUi(self, LoginAdminPanel):
        _translate = QtCore.QCoreApplication.translate
        LoginAdminPanel.setWindowTitle(_translate("LoginAdminPanel", "MainWindow"))
        self.header.setText(_translate("LoginAdminPanel", "Logowanie do panelu Admina"))
        self.loginLabel.setText(_translate("LoginAdminPanel", "Login"))
        self.passwordLabel.setText(_translate("LoginAdminPanel", "Hasło"))
        self.loginButton.setText(_translate("LoginAdminPanel", "Zaloguj"))

    def login(self):
        authorized = self.category_requester.authorize(self.loginLineEdit.text(), self.passwordLineEdit.text())
        if authorized:
            self.AdminPanel = QtWidgets.QMainWindow()
            self.admin_panel_ui = Ui_AdminPanelWindow()
            self.admin_panel_ui.setupUi(self.AdminPanel)
            self.AdminPanel.show()
            self.login_admin_panel.hide()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Błąd logowania")
            msg.setInformativeText('Nieprawidłowe dane logowania')
            msg.setWindowTitle("Błąd logowania")
            msg.exec_()


# main for quicker manual testing
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    LoginAdminPanel = QtWidgets.QMainWindow()
    ui = Ui_LoginAdminPanel()
    ui.setupUi(LoginAdminPanel)
    LoginAdminPanel.show()
    sys.exit(app.exec_())
