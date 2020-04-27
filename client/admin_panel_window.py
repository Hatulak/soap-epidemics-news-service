# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_panel_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets


class Ui_AdminPanelWindow(object):
    def setupUi(self, AdminPanelWindow):
        AdminPanelWindow.setObjectName("AdminPanelWindow")
        AdminPanelWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(AdminPanelWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 270, 47, 13))
        self.label.setObjectName("label")
        AdminPanelWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AdminPanelWindow)
        QtCore.QMetaObject.connectSlotsByName(AdminPanelWindow)

    def retranslateUi(self, AdminPanelWindow):
        _translate = QtCore.QCoreApplication.translate
        AdminPanelWindow.setWindowTitle(_translate("AdminPanelWindow", "MainWindow"))
        self.label.setText(_translate("AdminPanelWindow", "AdminPanel"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    AdminPanelWindow = QtWidgets.QMainWindow()
    ui = Ui_AdminPanelWindow()
    ui.setupUi(AdminPanelWindow)
    AdminPanelWindow.show()
    sys.exit(app.exec_())
