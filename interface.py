# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(297, 409)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.message_box = QPlainTextEdit(self.centralwidget)
        self.message_box.setObjectName(u"message_box")
        self.message_box.setReadOnly(True)

        self.gridLayout.addWidget(self.message_box, 0, 0, 1, 2)

        self.reconnect_button = QPushButton(self.centralwidget)
        self.reconnect_button.setObjectName(u"reconnect_button")

        self.gridLayout.addWidget(self.reconnect_button, 2, 1, 1, 1)

        self.message_button = QPushButton(self.centralwidget)
        self.message_button.setObjectName(u"message_button")

        self.gridLayout.addWidget(self.message_button, 1, 1, 1, 1)

        self.message_input = QLineEdit(self.centralwidget)
        self.message_input.setObjectName(u"message_input")

        self.gridLayout.addWidget(self.message_input, 1, 0, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Chat v0.1", None))
        self.message_box.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Connecting...", None))
        self.reconnect_button.setText(QCoreApplication.translate("MainWindow", u"Reconnect", None))
        self.message_button.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.message_input.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Type your message here...", None))
    # retranslateUi
