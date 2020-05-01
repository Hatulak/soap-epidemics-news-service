# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'news_details_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

from NewsRequester import NewsRequester


class Ui_NewsDetailsWindow(object):
    def setupUi(self, NewsDetailsWindow, id):
        self.id = id
        self.news_details_window = NewsDetailsWindow
        NewsDetailsWindow.setObjectName("NewsDetailsWindow")
        NewsDetailsWindow.resize(800, 600)
        NewsDetailsWindow.setMinimumSize(QtCore.QSize(800, 600))
        NewsDetailsWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(NewsDetailsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(280, 0, 521, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.titleLabel.setFont(font)
        self.titleLabel.setText("")
        self.titleLabel.setObjectName("titleLabel")
        self.dateLabel = QtWidgets.QLabel(self.centralwidget)
        self.dateLabel.setGeometry(QtCore.QRect(0, 0, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dateLabel.setFont(font)
        self.dateLabel.setText("")
        self.dateLabel.setObjectName("dateLabel")
        self.imageLabel = QtWidgets.QLabel(self.centralwidget)
        self.imageLabel.setGeometry(QtCore.QRect(0, 40, 321, 491))
        self.imageLabel.setText("")
        self.imageLabel.setObjectName("imageLabel")
        self.textLabel = QtWidgets.QLabel(self.centralwidget)
        self.textLabel.setGeometry(QtCore.QRect(340, 40, 481, 561))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textLabel.setFont(font)
        self.textLabel.setText("")
        self.textLabel.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.textLabel.setObjectName("textLabel")
        self.categoryLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.categoryLabel.setFont(font)
        self.categoryLabel.setGeometry(QtCore.QRect(140, 0, 141, 31))
        self.categoryLabel.setText("")
        self.categoryLabel.setObjectName("categoryLabel")
        self.pdfButton = QtWidgets.QPushButton(self.centralwidget)
        self.pdfButton.setGeometry(QtCore.QRect(20, 560, 75, 23))
        self.pdfButton.setObjectName("pdfButton")
        NewsDetailsWindow.setCentralWidget(self.centralwidget)

        self.pdfButton.clicked.connect(self.save_pdf)

        self.news = NewsRequester().get_news_by_id(self.id)
        self.dateLabel.setText(self.news.date)
        self.titleLabel.setText(self.news.name)
        self.textLabel.setText(self.news.desc)
        self.categoryLabel.setText(self.news.categoryName)
        image = NewsRequester().load_file(self.news.imagePath)
        self.imageLabel.setPixmap(QtGui.QPixmap(image))

        self.retranslateUi(NewsDetailsWindow)
        QtCore.QMetaObject.connectSlotsByName(NewsDetailsWindow)

    def retranslateUi(self, NewsDetailsWindow):
        _translate = QtCore.QCoreApplication.translate
        NewsDetailsWindow.setWindowTitle(_translate("NewsDetailsWindow", "MainWindow"))
        self.pdfButton.setText(_translate("NewsDetailsWindow", "Generuj pdf"))

    def save_pdf(self):
        fileName = QFileDialog.getSaveFileName(self.news_details_window, 'Zapisz', directory='news.pdf')
        NewsRequester().generate_pdf(self.id, fileName[0])


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    NewsDetailsWindow = QtWidgets.QMainWindow()
    ui = Ui_NewsDetailsWindow()
    ui.setupUi(NewsDetailsWindow)
    NewsDetailsWindow.show()
    sys.exit(app.exec_())
