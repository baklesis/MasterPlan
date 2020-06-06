# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'OrganizerCreateWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from global_vars import *

class Ui_OrganizerCreateWindow(object):
    def setupUi(self, OrganizerCreateWindow):
        if not OrganizerCreateWindow.objectName():
            OrganizerCreateWindow.setObjectName(u"OrganizerCreateWindow")
        OrganizerCreateWindow.resize(278, 284)
        self.buttonBox = QDialogButtonBox(OrganizerCreateWindow)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(-120, 240, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.FieldName = QLineEdit(OrganizerCreateWindow)
        self.FieldName.setObjectName(u"FieldName")
        self.FieldName.setGeometry(QRect(20, 90, 211, 27))
        self.FieldEmail = QLineEdit(OrganizerCreateWindow)
        self.FieldEmail.setObjectName(u"FieldEmail")
        self.FieldEmail.setGeometry(QRect(20, 140, 211, 27))
        self.LabelName = QLabel(OrganizerCreateWindow)
        self.LabelName.setObjectName(u"LabelName")
        self.LabelName.setGeometry(QRect(20, 70, 71, 19))
        self.LabelEmail = QLabel(OrganizerCreateWindow)
        self.LabelEmail.setObjectName(u"LabelEmail")
        self.LabelEmail.setGeometry(QRect(20, 120, 41, 19))
        self.LabelPrompt = QLabel(OrganizerCreateWindow)
        self.LabelPrompt.setObjectName(u"LabelPrompt")
        self.LabelPrompt.setGeometry(QRect(20, 20, 251, 31))
        self.LabelPrompt.setWordWrap(True)
        self.LabeInfo = QLabel(OrganizerCreateWindow)
        self.LabeInfo.setObjectName(u"LabeInfo")
        self.LabeInfo.setGeometry(QRect(20, 180, 241, 51))
        font = QFont()
        font.setItalic(True)
        self.LabeInfo.setFont(font)
        self.LabeInfo.setWordWrap(True)

        self.retranslateUi(OrganizerCreateWindow)
        self.buttonBox.accepted.connect(OrganizerCreateWindow.accept)
        self.buttonBox.rejected.connect(OrganizerCreateWindow.reject)

        QMetaObject.connectSlotsByName(OrganizerCreateWindow)
    # setupUi

    def retranslateUi(self, OrganizerCreateWindow):
        OrganizerCreateWindow.setWindowTitle(QCoreApplication.translate("OrganizerCreateWindow", u"Create a new organizer", None))
        self.LabelName.setText(QCoreApplication.translate("OrganizerCreateWindow", u"Full Name", None))
        self.LabelEmail.setText(QCoreApplication.translate("OrganizerCreateWindow", u"Email", None))
        self.LabelPrompt.setText(QCoreApplication.translate("OrganizerCreateWindow", u"Please enter the organizer's information", None))
        self.LabeInfo.setText(QCoreApplication.translate("OrganizerCreateWindow", u"Clicking \"OK\" will send an automated invitation to the email specified above.", None))
    # retranslateUi
class OrganizerCreateWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_OrganizerCreateWindow()
        self.ui.setupUi(self)
        self.connectSignals()

    def connectSignals(self):
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)

    def showWindow(self):
        return self.exec()

    def createOrganizer(self):
        name = self.ui.FieldName.text()
        email = self.ui.FieldEmail.text()
        organizer_list.addOrganizer(account_list, "upatras", name, email)
