# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EventListWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_EventListWindow(object):
    def setupUi(self, EventListWindow):
        if not EventListWindow.objectName():
            EventListWindow.setObjectName(u"EventListWindow")
        EventListWindow.resize(900, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(EventListWindow.sizePolicy().hasHeightForWidth())
        EventListWindow.setSizePolicy(sizePolicy)
        EventListWindow.setMinimumSize(QSize(900, 600))
        EventListWindow.setMaximumSize(QSize(900, 600))
        self.centralwidget = QWidget(EventListWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, -10, 21, 41))
        self.label.setPixmap(QPixmap(u"../Downloads/Microsoft.SkypeApp_kzf8qxf38zg5c!App/All/baseline_list_black_18dp.png"))
        self.verticalLayoutWidget_7 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(260, 20, 631, 481))
        self.verticalLayout_8 = QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_details = QLabel(self.verticalLayoutWidget_7)
        self.label_details.setObjectName(u"label_details")
        font = QFont()
        font.setPointSize(18)
        self.label_details.setFont(font)
        self.label_details.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_details)

        self.stackedWidget_2 = QStackedWidget(self.verticalLayoutWidget_7)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stackedWidget_2.sizePolicy().hasHeightForWidth())
        self.stackedWidget_2.setSizePolicy(sizePolicy1)
        self.OrganizerView = QWidget()
        self.OrganizerView.setObjectName(u"OrganizerView")
        sizePolicy1.setHeightForWidth(self.OrganizerView.sizePolicy().hasHeightForWidth())
        self.OrganizerView.setSizePolicy(sizePolicy1)
        self.gridLayoutWidget_2 = QWidget(self.OrganizerView)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 0, 621, 453))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_25)

        self.label_25 = QLabel(self.gridLayoutWidget_2)
        self.label_25.setObjectName(u"label_25")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy2)
        self.label_25.setMinimumSize(QSize(0, 34))
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        font1.setWeight(75)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.label_25.setFont(font1)
        self.label_25.setFrameShape(QFrame.Panel)
        self.label_25.setFrameShadow(QFrame.Raised)
        self.label_25.setLineWidth(1)
        self.label_25.setMidLineWidth(1)
        self.label_25.setAlignment(Qt.AlignCenter)
        self.label_25.setMargin(6)

        self.horizontalLayout_13.addWidget(self.label_25)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_26)


        self.verticalLayout_16.addLayout(self.horizontalLayout_13)

        self.listView_6 = QListView(self.gridLayoutWidget_2)
        self.listView_6.setObjectName(u"listView_6")

        self.verticalLayout_16.addWidget(self.listView_6)


        self.gridLayout_3.addLayout(self.verticalLayout_16, 2, 0, 1, 2)

        self.label_30 = QLabel(self.gridLayoutWidget_2)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_3.addWidget(self.label_30, 4, 2, 1, 1)

        self.label_26 = QLabel(self.gridLayoutWidget_2)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_3.addWidget(self.label_26, 5, 2, 1, 1)

        self.label_31 = QLabel(self.gridLayoutWidget_2)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_3.addWidget(self.label_31, 4, 0, 1, 1)

        self.label_33 = QLabel(self.gridLayoutWidget_2)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_3.addWidget(self.label_33, 5, 0, 1, 1)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_21)

        self.label_24 = QLabel(self.gridLayoutWidget_2)
        self.label_24.setObjectName(u"label_24")
        sizePolicy2.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy2)
        self.label_24.setMinimumSize(QSize(0, 34))
        self.label_24.setMaximumSize(QSize(16777215, 30))
        self.label_24.setFont(font1)
        self.label_24.setFrameShape(QFrame.Panel)
        self.label_24.setFrameShadow(QFrame.Raised)
        self.label_24.setLineWidth(1)
        self.label_24.setMidLineWidth(1)
        self.label_24.setAlignment(Qt.AlignCenter)
        self.label_24.setMargin(6)

        self.horizontalLayout_11.addWidget(self.label_24)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_22)


        self.verticalLayout_15.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_23 = QSpacerItem(60, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_23)

        self.lineEdit_3 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_12.addWidget(self.lineEdit_3)

        self.horizontalSpacer_24 = QSpacerItem(60, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_24)


        self.verticalLayout_15.addLayout(self.horizontalLayout_12)

        self.update_space_const_btn = QPushButton(self.gridLayoutWidget_2)
        self.update_space_const_btn.setObjectName(u"update_space_const_btn")

        self.verticalLayout_15.addWidget(self.update_space_const_btn)


        self.gridLayout_3.addLayout(self.verticalLayout_15, 2, 2, 1, 1)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_29)

        self.label_32 = QLabel(self.gridLayoutWidget_2)
        self.label_32.setObjectName(u"label_32")
        sizePolicy2.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy2)
        self.label_32.setMinimumSize(QSize(0, 34))
        font2 = QFont()
        font2.setPointSize(13)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_32.setFont(font2)
        self.label_32.setFrameShape(QFrame.Panel)
        self.label_32.setFrameShadow(QFrame.Raised)
        self.label_32.setLineWidth(1)
        self.label_32.setMidLineWidth(1)
        self.label_32.setAlignment(Qt.AlignCenter)
        self.label_32.setMargin(6)

        self.horizontalLayout_15.addWidget(self.label_32)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_30)


        self.verticalLayout_19.addLayout(self.horizontalLayout_15)

        self.listView_7 = QListView(self.gridLayoutWidget_2)
        self.listView_7.setObjectName(u"listView_7")

        self.verticalLayout_19.addWidget(self.listView_7)


        self.gridLayout_3.addLayout(self.verticalLayout_19, 0, 0, 1, 3)

        self.horizontalSpacer_27 = QSpacerItem(150, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_27, 1, 1, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)

        self.add_time_const_btn = QPushButton(self.gridLayoutWidget_2)
        self.add_time_const_btn.setObjectName(u"add_time_const_btn")

        self.horizontalLayout_9.addWidget(self.add_time_const_btn)


        self.gridLayout_3.addLayout(self.horizontalLayout_9, 1, 2, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_13)

        self.add_tag_const_btn = QPushButton(self.gridLayoutWidget_2)
        self.add_tag_const_btn.setObjectName(u"add_tag_const_btn")

        self.horizontalLayout_10.addWidget(self.add_tag_const_btn)


        self.gridLayout_3.addLayout(self.horizontalLayout_10, 3, 1, 1, 1)

        self.stackedWidget_2.addWidget(self.OrganizerView)
        self.AdminView = QWidget()
        self.AdminView.setObjectName(u"AdminView")
        sizePolicy1.setHeightForWidth(self.AdminView.sizePolicy().hasHeightForWidth())
        self.AdminView.setSizePolicy(sizePolicy1)
        self.gridLayoutWidget = QWidget(self.AdminView)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 0, 621, 451))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(8, 8, 8, 8)
        self.label_10 = QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_10)

        self.pushButton_6 = QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout_6.addWidget(self.pushButton_6)


        self.gridLayout.addLayout(self.verticalLayout_6, 1, 2, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_9)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setMinimumSize(QSize(0, 30))
        self.label_5.setFont(font1)
        self.label_5.setFrameShape(QFrame.Panel)
        self.label_5.setFrameShadow(QFrame.Raised)
        self.label_5.setLineWidth(1)
        self.label_5.setMidLineWidth(1)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setMargin(6)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_10)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_7 = QSpacerItem(60, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)

        self.lineEdit = QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_5.addWidget(self.lineEdit)

        self.horizontalSpacer_8 = QSpacerItem(60, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)


        self.gridLayout.addLayout(self.verticalLayout_4, 1, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setMinimumSize(QSize(0, 30))
        self.label_3.setFont(font1)
        self.label_3.setFrameShape(QFrame.Panel)
        self.label_3.setFrameShadow(QFrame.Raised)
        self.label_3.setLineWidth(1)
        self.label_3.setMidLineWidth(1)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setMargin(6)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.listView_4 = QListView(self.gridLayoutWidget)
        self.listView_4.setObjectName(u"listView_4")

        self.verticalLayout_3.addWidget(self.listView_4)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 2, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 3, 2, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer_2 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy3)
        self.label_8.setMinimumSize(QSize(0, 30))
        self.label_8.setFont(font1)
        self.label_8.setFrameShape(QFrame.Panel)
        self.label_8.setFrameShadow(QFrame.Raised)
        self.label_8.setLineWidth(1)
        self.label_8.setMidLineWidth(0)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_8.setMargin(6)

        self.horizontalLayout_6.addWidget(self.label_8)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_11)

        self.pushButton_10 = QPushButton(self.gridLayoutWidget)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.horizontalLayout_6.addWidget(self.pushButton_10)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.scrollArea = QScrollArea(self.gridLayoutWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 800, 28))
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy4)
        self.scrollAreaWidgetContents.setMinimumSize(QSize(800, 0))
        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(-20, 30, 58, 16))
        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(250, 30, 58, 16))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_5.addWidget(self.scrollArea)


        self.gridLayout.addLayout(self.verticalLayout_5, 4, 0, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 2, 2, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.pushButton_11 = QPushButton(self.gridLayoutWidget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(0, 40))
        font3 = QFont()
        font3.setBold(True)
        font3.setItalic(False)
        font3.setWeight(75)
        self.pushButton_11.setFont(font3)
        self.pushButton_11.setFlat(False)

        self.verticalLayout_7.addWidget(self.pushButton_11)


        self.gridLayout.addLayout(self.verticalLayout_7, 4, 2, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_12, 0, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

        self.label_11 = QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        sizePolicy2.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy2)
        self.label_11.setMinimumSize(QSize(0, 30))
        self.label_11.setFont(font1)
        self.label_11.setFrameShape(QFrame.Panel)
        self.label_11.setFrameShadow(QFrame.Raised)
        self.label_11.setLineWidth(1)
        self.label_11.setMidLineWidth(1)
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_11.setMargin(6)

        self.horizontalLayout_7.addWidget(self.label_11)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.listView_2 = QListView(self.gridLayoutWidget)
        self.listView_2.setObjectName(u"listView_2")

        self.verticalLayout.addWidget(self.listView_2)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.label_13 = QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 3, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.AdminView)

        self.verticalLayout_8.addWidget(self.stackedWidget_2)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 20, 262, 521))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.event_list_label = QLabel(self.verticalLayoutWidget)
        self.event_list_label.setObjectName(u"event_list_label")
        self.event_list_label.setFrameShape(QFrame.Box)
        self.event_list_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.event_list_label)

        self.stackedWidget = QStackedWidget(self.verticalLayoutWidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QSize(250, 34))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayoutWidget = QWidget(self.page)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 251, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.create_organizer_btn = QPushButton(self.horizontalLayoutWidget)
        self.create_organizer_btn.setObjectName(u"create_organizer_btn")

        self.horizontalLayout.addWidget(self.create_organizer_btn)

        self.create_event_btn = QPushButton(self.horizontalLayoutWidget)
        self.create_event_btn.setObjectName(u"create_event_btn")

        self.horizontalLayout.addWidget(self.create_event_btn)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_2.addWidget(self.stackedWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.filter_btn = QPushButton(self.verticalLayoutWidget)
        self.filter_btn.setObjectName(u"filter_btn")

        self.horizontalLayout_2.addWidget(self.filter_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.sort_btn = QPushButton(self.verticalLayoutWidget)
        self.sort_btn.setObjectName(u"sort_btn")

        self.horizontalLayout_2.addWidget(self.sort_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.Event_listView = QListView(self.verticalLayoutWidget)
        self.Event_listView.setObjectName(u"Event_listView")

        self.verticalLayout_2.addWidget(self.Event_listView)

        self.exit_btn = QPushButton(self.verticalLayoutWidget)
        self.exit_btn.setObjectName(u"exit_btn")

        self.verticalLayout_2.addWidget(self.exit_btn)

        EventListWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(EventListWindow)

        self.stackedWidget_2.setCurrentIndex(0)
        self.pushButton_11.setDefault(False)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(EventListWindow)
    # setupUi

    def retranslateUi(self, EventListWindow):
        EventListWindow.setWindowTitle(QCoreApplication.translate("EventListWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_details.setText(QCoreApplication.translate("EventListWindow", u"Event Details", None))
        self.label_25.setText(QCoreApplication.translate("EventListWindow", u"Tag Constraints", None))
        self.label_30.setText(QCoreApplication.translate("EventListWindow", u"Current Scheduled Room:", None))
        self.label_26.setText(QCoreApplication.translate("EventListWindow", u"<Room>", None))
        self.label_31.setText(QCoreApplication.translate("EventListWindow", u"Current Scheduled Date and Time:", None))
        self.label_33.setText(QCoreApplication.translate("EventListWindow", u"<Datetime>", None))
        self.label_24.setText(QCoreApplication.translate("EventListWindow", u"Space Constraint", None))
        self.update_space_const_btn.setText(QCoreApplication.translate("EventListWindow", u"Update", None))
        self.label_32.setText(QCoreApplication.translate("EventListWindow", u"Time Constraints", None))
        self.add_time_const_btn.setText(QCoreApplication.translate("EventListWindow", u"Add", None))
        self.add_tag_const_btn.setText(QCoreApplication.translate("EventListWindow", u"Add", None))
        self.label_10.setText(QCoreApplication.translate("EventListWindow", u"Assigned Organizer:", None))
        self.pushButton_6.setText(QCoreApplication.translate("EventListWindow", u"Assign Organizer", None))
        self.label_5.setText(QCoreApplication.translate("EventListWindow", u"Space Constraint", None))
        self.label_3.setText(QCoreApplication.translate("EventListWindow", u"Tag Constraints", None))
        self.label_12.setText(QCoreApplication.translate("EventListWindow", u"<Room>", None))
        self.label_8.setText(QCoreApplication.translate("EventListWindow", u"Tags", None))
        self.pushButton_10.setText(QCoreApplication.translate("EventListWindow", u"Add", None))
        self.label_7.setText(QCoreApplication.translate("EventListWindow", u"TextLabel", None))
        self.label_9.setText(QCoreApplication.translate("EventListWindow", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("EventListWindow", u"Current Scheduled Room:", None))
        self.label_4.setText(QCoreApplication.translate("EventListWindow", u"Current Scheduled Date and Time:", None))
        self.pushButton_11.setText(QCoreApplication.translate("EventListWindow", u"Execute scheduling", None))
        self.label_11.setText(QCoreApplication.translate("EventListWindow", u"Time Constraints", None))
        self.label_13.setText(QCoreApplication.translate("EventListWindow", u"<Datetime>", None))
        self.event_list_label.setText(QCoreApplication.translate("EventListWindow", u"Event List", None))
        self.create_organizer_btn.setText(QCoreApplication.translate("EventListWindow", u"Create Organizer", None))
        self.create_event_btn.setText(QCoreApplication.translate("EventListWindow", u"Create Event", None))
        self.filter_btn.setText(QCoreApplication.translate("EventListWindow", u"Filter", None))
        self.sort_btn.setText(QCoreApplication.translate("EventListWindow", u"Sort", None))
        self.exit_btn.setText(QCoreApplication.translate("EventListWindow", u"Exit", None))
    # retranslateUi

