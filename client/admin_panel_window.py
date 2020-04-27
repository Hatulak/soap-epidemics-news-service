# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_panel_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog

from CategoryRequester import CategoryRequester
from NewsRequester import NewsRequester


class Ui_AdminPanelWindow(object):
    def setupUi(self, AdminPanelWindow):
        self.choosen_file_name_to_new_news = ""
        self.choosen_file_name_to_edit_news = ""
        self.category_requester = CategoryRequester()
        self.news_requester = NewsRequester()
        AdminPanelWindow.setObjectName("AdminPanelWindow")
        AdminPanelWindow.resize(750, 600)
        AdminPanelWindow.setMinimumSize(QtCore.QSize(600, 600))
        AdminPanelWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(AdminPanelWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.addCategoryLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.addCategoryLineEdit.setGeometry(QtCore.QRect(52, 40, 201, 20))
        self.addCategoryLineEdit.setObjectName("addCategoryLineEdit")
        self.addCategoryButton = QtWidgets.QPushButton(self.centralwidget)
        self.addCategoryButton.setGeometry(QtCore.QRect(10, 70, 241, 23))
        self.addCategoryButton.setObjectName("addCategoryButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 115, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 47, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 140, 47, 16))
        self.label_4.setObjectName("label_4")
        self.addCategoryComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.addCategoryComboBox.setGeometry(QtCore.QRect(10, 160, 241, 22))
        self.addCategoryComboBox.setObjectName("addCategoryComboBox")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 190, 47, 21))
        self.label_5.setObjectName("label_5")
        self.addTitleLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.addTitleLineEdit.setGeometry(QtCore.QRect(50, 190, 201, 20))
        self.addTitleLineEdit.setObjectName("addTitleLineEdit")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 220, 47, 13))
        self.label_6.setObjectName("label_6")
        self.addDescriptionTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.addDescriptionTextEdit.setGeometry(QtCore.QRect(10, 240, 241, 241))
        self.addDescriptionTextEdit.setObjectName("addDescriptionTextEdit")
        self.addAddonButton = QtWidgets.QPushButton(self.centralwidget)
        self.addAddonButton.setGeometry(QtCore.QRect(10, 510, 91, 23))
        self.addAddonButton.setObjectName("addAddonButton")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 490, 47, 13))
        self.label_7.setObjectName("label_7")
        self.addAddonLabel = QtWidgets.QLabel(self.centralwidget)
        self.addAddonLabel.setGeometry(QtCore.QRect(110, 510, 141, 21))
        self.addAddonLabel.setText("")
        self.addAddonLabel.setObjectName("addAddonLabel")
        self.addNewsButton = QtWidgets.QPushButton(self.centralwidget)
        self.addNewsButton.setGeometry(QtCore.QRect(10, 550, 241, 23))
        self.addNewsButton.setObjectName("addNewsButton")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(320, 10, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.chooseCategoryComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.chooseCategoryComboBox.setGeometry(QtCore.QRect(540, 10, 201, 22))
        self.chooseCategoryComboBox.setObjectName("chooseCategoryComboBox")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(440, 10, 101, 20))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(320, 40, 47, 21))
        self.label_10.setObjectName("label_10")
        self.editCategoryLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.editCategoryLineEdit.setGeometry(QtCore.QRect(370, 40, 201, 20))
        self.editCategoryLineEdit.setObjectName("editCategoryLineEdit")
        self.editCategoryButton = QtWidgets.QPushButton(self.centralwidget)
        self.editCategoryButton.setGeometry(QtCore.QRect(330, 70, 241, 23))
        self.editCategoryButton.setObjectName("editCategoryButton")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(320, 110, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(440, 110, 101, 20))
        self.label_12.setObjectName("label_12")
        self.chooseNewsComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.chooseNewsComboBox.setGeometry(QtCore.QRect(540, 110, 201, 22))
        self.chooseNewsComboBox.setObjectName("chooseNewsComboBox")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(320, 140, 47, 16))
        self.label_13.setObjectName("label_13")
        self.editCategoryComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.editCategoryComboBox.setGeometry(QtCore.QRect(320, 160, 241, 22))
        self.editCategoryComboBox.setObjectName("editCategoryComboBox")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(320, 190, 47, 21))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(320, 490, 47, 13))
        self.label_15.setObjectName("label_15")
        self.editAddonButton = QtWidgets.QPushButton(self.centralwidget)
        self.editAddonButton.setGeometry(QtCore.QRect(320, 510, 91, 23))
        self.editAddonButton.setObjectName("editAddonButton")
        self.editTitleLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.editTitleLineEdit.setGeometry(QtCore.QRect(360, 190, 201, 20))
        self.editTitleLineEdit.setObjectName("editTitleLineEdit")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(320, 220, 47, 13))
        self.label_16.setObjectName("label_16")
        self.editNewsButton = QtWidgets.QPushButton(self.centralwidget)
        self.editNewsButton.setGeometry(QtCore.QRect(320, 550, 241, 23))
        self.editNewsButton.setObjectName("editNewsButton")
        self.editDescriptionTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.editDescriptionTextEdit.setGeometry(QtCore.QRect(320, 240, 241, 241))
        self.editDescriptionTextEdit.setObjectName("editDescriptionTextEdit")
        self.editAddonLabel = QtWidgets.QLabel(self.centralwidget)
        self.editAddonLabel.setGeometry(QtCore.QRect(420, 510, 141, 21))
        self.editAddonLabel.setText("")
        self.editAddonLabel.setObjectName("editAddonLabel")
        self.deleteCategoryButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteCategoryButton.setGeometry(QtCore.QRect(640, 50, 101, 23))
        self.deleteCategoryButton.setObjectName("deleteCategoryButton")
        self.deleteNewsButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteNewsButton.setGeometry(QtCore.QRect(640, 150, 101, 23))
        self.deleteNewsButton.setObjectName("deleteNewsButton")

        self.addCategoryButton.clicked.connect(self.add_category)
        self.addAddonButton.clicked.connect(self.choose_file_to_new_news)
        self.addNewsButton.clicked.connect(self.add_news)
        self.editCategoryButton.clicked.connect(self.edit_category)
        self.editNewsButton.clicked.connect(self.edit_news)
        self.deleteCategoryButton.clicked.connect(self.delete_category)
        self.deleteNewsButton.clicked.connect(self.delete_news)
        self._refresh_combo_boxes()
        self.chooseCategoryComboBox.currentTextChanged.connect(self.load_category)
        self.chooseNewsComboBox.currentTextChanged.connect(self.load_news)
        AdminPanelWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AdminPanelWindow)
        QtCore.QMetaObject.connectSlotsByName(AdminPanelWindow)

    def load_category(self):
        pass  # todo - jak bedzie mozliwosc to zmienic
        # category = self.category_requester.get_category_by_id(self.chooseCategoryComboBox.currentData())
        # self.editCategoryLineEdit.setText(category.name)

    def load_news(self):
        if self.chooseNewsComboBox.currentData():
            news = self.news_requester.get_news_by_id(int(self.chooseNewsComboBox.currentData()))
            print(news)
            self.editTitleLineEdit.setText(news.name)
            self.editDescriptionTextEdit.setText(news.desc)
            self.editCategoryComboBox.setCurrentText(news.categoryName)

    def add_category(self):
        if self.addCategoryLineEdit.text():
            self.category_requester.create_category(self.addCategoryLineEdit.text())
            self.addCategoryLineEdit.setText("")
            self._show_messge_dialog("Sukces", "Dodano kategorię", QMessageBox.Information)
            self._refresh_combo_boxes()
        else:
            self._show_messge_dialog("Błąd", "Nazwa nie może być pusta", QMessageBox.Warning)

    def edit_category(self):
        pass  # todo - jak bedzie mozliwosc edycji to zmienic

    # if self.editCategoryLineEdit.text():
    #     self.category_requester.(self.addCategoryLineEdit.text())
    #     self.addCategoryLineEdit.setText("")
    #     self._show_messge_dialog("Sukces", "Dodano kategorię", QMessageBox.Information)
    #     self._refresh_combo_boxes()
    # else:
    #     self._show_messge_dialog("Błąd", "Nazwa nie może być pusta", QMessageBox.Warning)

    def choose_file_to_new_news(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setNameFilters(["Images (*.png *.jpg *.bmp *.jpeg)"])
        dlg.selectNameFilter("Images (*.png *.jpg *.bmp *.jpeg)")
        if dlg.exec_():
            filenames = dlg.selectedFiles()

            self.choosen_file_name_to_new_news = filenames[0]
            self.addAddonLabel.setText("Plik wybrany")
        else:
            self.choosen_file_name_to_new_news = ""
            self.addAddonLabel.setText("Plik niewybrany")

    def choose_file_to_edit_news(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setNameFilters(["Images (*.png *.jpg *.bmp *.jpeg)"])
        dlg.selectNameFilter("Images (*.png *.jpg *.bmp *.jpeg)")
        if dlg.exec_():
            filenames = dlg.selectedFiles()

            self.choosen_file_name_to_edit_news = filenames[0]
            self.addAddonLabel.setText("Plik wybrany")
        else:
            self.choosen_file_name_to_edit_news = ""
            self.addAddonLabel.setText("Plik niewybrany")

    def add_news(self):
        if self.addTitleLineEdit.text():
            if self.addDescriptionTextEdit.toPlainText():
                if self.choosen_file_name_to_new_news:
                    news = self.news_requester.create_news(self.addTitleLineEdit.text(),
                                                           self.addDescriptionTextEdit.toPlainText(),
                                                           str(datetime.now().strftime('%d/%m/%Y')),
                                                           int(self.addCategoryComboBox.currentData()))
                    self.news_requester.store_file(self.choosen_file_name_to_new_news, news.id)
                    self._refresh_combo_boxes()
                    self.addTitleLineEdit.setText("")
                    self.addDescriptionTextEdit.setText("")
                    self.addAddonLabel.setText("")
                    self._show_messge_dialog("Sukces", "Dodano newsa", QMessageBox.Information)
                else:
                    self._show_messge_dialog("Błąd", "Należy wybrać załącznik", QMessageBox.Warning)
            else:
                self._show_messge_dialog("Błąd", "Opis nie może być pusty", QMessageBox.Warning)
        else:
            self._show_messge_dialog("Błąd", "Tytuł nie może być pusty", QMessageBox.Warning)

    def edit_news(self):
        pass  # todo - jak bedzie mozliwosc edycji to zmienic
        # if self.editTitleLineEdit.text():
        #     if self.editDescriptionTextEdit.toPlainText():
        #         if self.choosen_file_name_to_new_news:
        #             self.news_requester.edit_news(self.editTitleLineEdit.text(),
        #                                             self.editDescriptionTextEdit.toPlainText(),
        #                                             str(datetime.now().strftime('%d/%m/%Y')),
        #                                             int(self.editCategoryComboBox.currentData()))
        #             self._show_messge_dialog("Sukces", "Dodano newsa", QMessageBox.Information)
        #         else:
        #             self._show_messge_dialog("Błąd", "Należy wybrać załącznik", QMessageBox.Warning)
        #     else:
        #         self._show_messge_dialog("Błąd", "Opis nie może być pusty", QMessageBox.Warning)
        # else:
        #     self._show_messge_dialog("Błąd", "Tytuł nie może być pusty", QMessageBox.Warning)

    def delete_category(self):
        self.category_requester.delete_category(int(self.chooseCategoryComboBox.currentData()))
        self._refresh_combo_boxes()
        self._show_messge_dialog("Sukces", "Usunięto", QMessageBox.Information)

    def delete_news(self):
        self.news_requester.delete_news(int(self.chooseNewsComboBox.currentData()))
        self._refresh_combo_boxes()
        self._show_messge_dialog("Sukces", "Usunięto", QMessageBox.Information)

    # type - QMessageBox.Warning, QMessageBox.Information ...
    def _show_messge_dialog(self, header, message, message_type):
        msg = QMessageBox()
        msg.setIcon(message_type)
        msg.setText(header)
        msg.setInformativeText(message)
        msg.setWindowTitle(header)
        msg.exec_()

    def _refresh_combo_boxes(self):
        self.addCategoryComboBox.clear()
        categories = self.category_requester.get_all_category()
        for c in categories:
            self.addCategoryComboBox.addItem(c.name, str(c.id))

        self.editCategoryComboBox.clear()
        categories = self.category_requester.get_all_category()
        for c in categories:
            self.editCategoryComboBox.addItem(c.name, str(c.id))

        self.chooseCategoryComboBox.clear()
        categories = self.category_requester.get_all_category()
        for c in categories:
            self.chooseCategoryComboBox.addItem(c.name, str(c.id))

        self.chooseNewsComboBox.clear()
        newses = self.news_requester.get_all_news()
        print(newses)
        for n in newses:
            self.chooseNewsComboBox.addItem(n.name, str(n.id))

    def retranslateUi(self, AdminPanelWindow):
        _translate = QtCore.QCoreApplication.translate
        AdminPanelWindow.setWindowTitle(_translate("AdminPanelWindow", "MainWindow"))
        self.label.setText(_translate("AdminPanelWindow", "Dodawanie kategorii"))
        self.addCategoryButton.setText(_translate("AdminPanelWindow", "Dodaj kategorię"))
        self.label_2.setText(_translate("AdminPanelWindow", "Dodawanie newsa"))
        self.label_3.setText(_translate("AdminPanelWindow", "Nazwa"))
        self.label_4.setText(_translate("AdminPanelWindow", "Kategoria"))
        self.label_5.setText(_translate("AdminPanelWindow", "Tytuł"))
        self.label_6.setText(_translate("AdminPanelWindow", "Opis"))
        self.addAddonButton.setText(_translate("AdminPanelWindow", "Dodaj załącznik"))
        self.label_7.setText(_translate("AdminPanelWindow", "Załącznik"))
        self.addNewsButton.setText(_translate("AdminPanelWindow", "Dodaj news"))
        self.label_8.setText(_translate("AdminPanelWindow", "Edycja kategorii"))
        self.label_9.setText(_translate("AdminPanelWindow", "Wybierz kategorię"))
        self.label_10.setText(_translate("AdminPanelWindow", "Nazwa"))
        self.editCategoryButton.setText(_translate("AdminPanelWindow", "Zmień kategorię"))
        self.label_11.setText(_translate("AdminPanelWindow", "Edycja newsa"))
        self.label_12.setText(_translate("AdminPanelWindow", "Wybierz newsa"))
        self.label_13.setText(_translate("AdminPanelWindow", "Kategoria"))
        self.label_14.setText(_translate("AdminPanelWindow", "Tytuł"))
        self.label_15.setText(_translate("AdminPanelWindow", "Załącznik"))
        self.editAddonButton.setText(_translate("AdminPanelWindow", "Dodaj załącznik"))
        self.label_16.setText(_translate("AdminPanelWindow", "Opis"))
        self.editNewsButton.setText(_translate("AdminPanelWindow", "Zmień newsa"))
        self.deleteCategoryButton.setText(_translate("AdminPanelWindow", "Usuń kategorię"))
        self.deleteNewsButton.setText(_translate("AdminPanelWindow", "Usuń newsa"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    AdminPanelWindow = QtWidgets.QMainWindow()
    ui = Ui_AdminPanelWindow()
    ui.setupUi(AdminPanelWindow)
    AdminPanelWindow.show()
    sys.exit(app.exec_())
