from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QLocale)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from ui_classes.MessageWindow import MessageWindow


class Ui_RangeWindow(object):
    def setupUi(self, RangeWindow):
        if not RangeWindow.objectName():
            RangeWindow.setObjectName(u"RangeWindow")
        RangeWindow.resize(300, 200)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RangeWindow.sizePolicy().hasHeightForWidth())
        RangeWindow.setSizePolicy(sizePolicy)
        RangeWindow.setMinimumSize(QSize(300, 200))
        RangeWindow.setMaximumSize(QSize(300, 200))
        RangeWindow.setContextMenuPolicy(Qt.DefaultContextMenu)
        RangeWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.verticalLayout = QVBoxLayout(RangeWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.LayoutLabelCalendar = QHBoxLayout()
        self.LayoutLabelCalendar.setObjectName(u"LayoutLabelCalendar")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.LayoutLabelCalendar.addItem(self.horizontalSpacer_3)
        self.LabelCalendar = QLabel(RangeWindow)
        self.LabelCalendar.setObjectName(u"LabelCalendar")
        sizePolicy.setHeightForWidth(self.LabelCalendar.sizePolicy().hasHeightForWidth())
        self.LabelCalendar.setSizePolicy(sizePolicy)
        self.LabelCalendar.setMinimumSize(QSize(30, 30))
        self.LabelCalendar.setMaximumSize(QSize(30, 30))
        self.LabelCalendar.setPixmap(QPixmap(u"icons/calendar.png"))
        self.LabelCalendar.setScaledContents(True)
        self.LayoutLabelCalendar.addWidget(self.LabelCalendar)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.LayoutLabelCalendar.addItem(self.horizontalSpacer_4)
        self.verticalLayout.addLayout(self.LayoutLabelCalendar)
        self.LabelMessage = QLabel(RangeWindow)
        self.LabelMessage.setObjectName(u"LabelMessage")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.LabelMessage.sizePolicy().hasHeightForWidth())
        self.LabelMessage.setSizePolicy(sizePolicy1)
        self.LabelMessage.setMinimumSize(QSize(30, 0))
        self.LabelMessage.setMaximumSize(QSize(400, 16777215))
        self.LabelMessage.setAlignment(Qt.AlignCenter)
        self.LabelMessage.setWordWrap(True)
        self.verticalLayout.addWidget(self.LabelMessage)
        self.LayoutFrom = QHBoxLayout()
        self.LayoutFrom.setObjectName(u"LayoutFrom")
        self.LabelFrom = QLabel(RangeWindow)
        self.LabelFrom.setObjectName(u"LabelFrom")
        self.LabelFrom.setMinimumSize(QSize(20, 0))
        self.LabelFrom.setMaximumSize(QSize(20, 16777215))
        self.LayoutFrom.addWidget(self.LabelFrom)
        self.DateTimeFrom = QDateTimeEdit(RangeWindow)
        self.DateTimeFrom.setObjectName(u"DateTimeFrom")
        self.DateTimeFrom.setDate(QDate(2020, 1, 1))
        self.DateTimeFrom.setCurrentSection(QDateTimeEdit.DaySection)
        self.DateTimeFrom.setCalendarPopup(False)
        self.LayoutFrom.addWidget(self.DateTimeFrom)
        self.verticalLayout.addLayout(self.LayoutFrom)
        self.LayoutTo = QHBoxLayout()
        self.LayoutTo.setObjectName(u"LayoutTo")
        self.LabelTo_2 = QLabel(RangeWindow)
        self.LabelTo_2.setObjectName(u"LabelTo_2")
        self.LabelTo_2.setMinimumSize(QSize(20, 0))
        self.LabelTo_2.setMaximumSize(QSize(20, 16777215))
        self.LayoutTo.addWidget(self.LabelTo_2)
        self.DateTimeTo = QDateTimeEdit(RangeWindow)
        self.DateTimeTo.setObjectName(u"DateTimeTo")
        self.DateTimeTo.setDate(QDate(2021, 1, 1))
        self.LayoutTo.addWidget(self.DateTimeTo)
        self.verticalLayout.addLayout(self.LayoutTo)
        self.LayoutButtons = QHBoxLayout()
        self.LayoutButtons.setObjectName(u"LayoutButtons")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.LayoutButtons.addItem(self.horizontalSpacer)
        self.ButtonTrue = QPushButton(RangeWindow)
        self.ButtonTrue.setObjectName(u"ButtonTrue")
        self.LayoutButtons.addWidget(self.ButtonTrue)
        self.ButtonFalse = QPushButton(RangeWindow)
        self.ButtonFalse.setObjectName(u"ButtonFalse")
        self.LayoutButtons.addWidget(self.ButtonFalse)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.LayoutButtons.addItem(self.horizontalSpacer_2)
        self.verticalLayout.addLayout(self.LayoutButtons)
        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.verticalLayout.addItem(self.verticalSpacer)
        self.retranslateUi(RangeWindow)
        QMetaObject.connectSlotsByName(RangeWindow)

    def retranslateUi(self, RangeWindow):
        RangeWindow.setWindowTitle(QCoreApplication.translate("RangeWindow", u"Download", None))
        self.LabelCalendar.setText("")
        self.LabelMessage.setText(QCoreApplication.translate("RangeWindow", u"Select calendar range to download:", None))
        self.LabelFrom.setText(QCoreApplication.translate("RangeWindow", u"From:", None))
        self.DateTimeFrom.setDisplayFormat(QCoreApplication.translate("RangeWindow", u"d/M/yyyy", None))
        self.LabelTo_2.setText(QCoreApplication.translate("RangeWindow", u"To: ", None))
        self.DateTimeTo.setDisplayFormat(QCoreApplication.translate("RangeWindow", u"d/M/yyyy", None))
        self.ButtonTrue.setText(QCoreApplication.translate("RangeWindow", u"OK", None))
        self.ButtonFalse.setText(QCoreApplication.translate("RangeWindow", u"Cancel", None))

# window class #########################################################################################################
class RangeWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_RangeWindow()
        self.ui.setupUi(self)
        self.connectSignals()

    def connectSignals(self):
        self.ui.ButtonTrue.clicked.connect(self.showMessageWindow)
        self.ui.ButtonFalse.clicked.connect(self.reject)

    def showWindow(self):
        self.exec()

    def showMessageWindow(self):
        self.messageWindow = MessageWindow()
        self.messageWindow.showFileMessage()
        response = messageWindow.exec()
        if response == 1:
            messageWindow.createFile()
            self.accept()









