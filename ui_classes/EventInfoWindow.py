from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_EventInfoWindow(object):
    def setupUi(self, EventInfoWindow):
        if not EventInfoWindow.objectName():
            EventInfoWindow.setObjectName(u"EventInfoWindow")
        EventInfoWindow.resize(273, 374)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(EventInfoWindow.sizePolicy().hasHeightForWidth())
        EventInfoWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(EventInfoWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 271, 371))
        self.LayoutWindow = QVBoxLayout(self.verticalLayoutWidget)
        self.LayoutWindow.setObjectName(u"LayoutWindow")
        self.LayoutWindow.setContentsMargins(0, 0, 0, 0)
        self.LabelEventName = QLabel(self.verticalLayoutWidget)
        self.LabelEventName.setObjectName(u"LabelEventName")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.LabelEventName.sizePolicy().hasHeightForWidth())
        self.LabelEventName.setSizePolicy(sizePolicy1)
        self.LabelEventName.setMinimumSize(QSize(0, 50))
        self.LabelEventName.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamily(u"Cambria")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.LabelEventName.setFont(font)
        self.LabelEventName.setScaledContents(False)
        self.LabelEventName.setAlignment(Qt.AlignCenter)
        self.LabelEventName.setWordWrap(True)
        self.LayoutWindow.addWidget(self.LabelEventName)
        self.LayoutInfo = QGridLayout()
        self.LayoutInfo.setObjectName(u"LayoutInfo")
        self.LabelDurationValue = QLabel(self.verticalLayoutWidget)
        self.LabelDurationValue.setObjectName(u"LabelDurationValue")

        self.LayoutInfo.addWidget(self.LabelDurationValue, 3, 1, 1, 1)

        self.LabelRoomValue = QLabel(self.verticalLayoutWidget)
        self.LabelRoomValue.setObjectName(u"LabelRoomValue")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.LabelRoomValue.sizePolicy().hasHeightForWidth())
        self.LabelRoomValue.setSizePolicy(sizePolicy2)
        self.LabelRoomValue.setMinimumSize(QSize(0, 0))
        self.LabelRoomValue.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setPointSize(12)
        self.LabelRoomValue.setFont(font1)

        self.LayoutInfo.addWidget(self.LabelRoomValue, 0, 1, 1, 1)

        self.LabelDuration = QLabel(self.verticalLayoutWidget)
        self.LabelDuration.setObjectName(u"LabelDuration")
        self.LabelDuration.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.LayoutInfo.addWidget(self.LabelDuration, 3, 0, 1, 1)

        self.LabelTime = QLabel(self.verticalLayoutWidget)
        self.LabelTime.setObjectName(u"LabelTime")
        self.LabelTime.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.LayoutInfo.addWidget(self.LabelTime, 2, 0, 1, 1)

        self.LabelTimeValue = QLabel(self.verticalLayoutWidget)
        self.LabelTimeValue.setObjectName(u"LabelTimeValue")

        self.LayoutInfo.addWidget(self.LabelTimeValue, 2, 1, 1, 1)

        self.LabelRoom = QLabel(self.verticalLayoutWidget)
        self.LabelRoom.setObjectName(u"LabelRoom")
        self.LabelRoom.setFont(font1)
        self.LabelRoom.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.LayoutInfo.addWidget(self.LabelRoom, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.LayoutInfo.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.LayoutInfo.addItem(self.verticalSpacer_2, 4, 1, 1, 1)


        self.LayoutWindow.addLayout(self.LayoutInfo)
        self.LayoutPicture = QHBoxLayout()
        self.LayoutPicture.setObjectName(u"LayoutPicture")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.LayoutPicture.addItem(self.horizontalSpacer_3)

        self.LayoutOrganizer = QVBoxLayout()
        self.LayoutOrganizer.setObjectName(u"LayoutOrganizer")
        self.LabelOrganizer = QLabel(self.verticalLayoutWidget)
        self.LabelOrganizer.setObjectName(u"LabelOrganizer")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.LabelOrganizer.sizePolicy().hasHeightForWidth())
        self.LabelOrganizer.setSizePolicy(sizePolicy3)
        self.LabelOrganizer.setMinimumSize(QSize(100, 0))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.LabelOrganizer.setFont(font2)
        self.LabelOrganizer.setAlignment(Qt.AlignCenter)

        self.LayoutOrganizer.addWidget(self.LabelOrganizer)

        self.LabelOrganizerValue = QLabel(self.verticalLayoutWidget)
        self.LabelOrganizerValue.setObjectName(u"LabelOrganizerValue")
        self.LabelOrganizerValue.setAlignment(Qt.AlignCenter)
        self.LabelOrganizerValue.setWordWrap(True)

        self.LayoutOrganizer.addWidget(self.LabelOrganizerValue)

        self.verticalSpacer_3 = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.LayoutOrganizer.addItem(self.verticalSpacer_3)


        self.LayoutPicture.addLayout(self.LayoutOrganizer)

        self.LabelPicture = QLabel(self.verticalLayoutWidget)
        self.LabelPicture.setObjectName(u"LabelPicture")
        sizePolicy.setHeightForWidth(self.LabelPicture.sizePolicy().hasHeightForWidth())
        self.LabelPicture.setSizePolicy(sizePolicy)
        self.LabelPicture.setFrameShape(QFrame.Box)
        self.LabelPicture.setPixmap(QPixmap(u"icons/user.png"))
        self.LabelPicture.setAlignment(Qt.AlignCenter)
        self.LayoutPicture.addWidget(self.LabelPicture)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.LayoutPicture.addItem(self.horizontalSpacer_2)
        self.LayoutWindow.addLayout(self.LayoutPicture)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.LayoutWindow.addItem(self.verticalSpacer_4)

        EventInfoWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(EventInfoWindow)
        QMetaObject.connectSlotsByName(EventInfoWindow)

    def retranslateUi(self, EventInfoWindow):
        EventInfoWindow.setWindowTitle(QCoreApplication.translate("EventInfoWindow", u"MainWindow", None))
        self.LabelEventName.setText(QCoreApplication.translate("EventInfoWindow", u"<event name>", None))
        self.LabelDurationValue.setText(QCoreApplication.translate("EventInfoWindow", u"<duration>", None))
        self.LabelRoomValue.setText(QCoreApplication.translate("EventInfoWindow", u"<room>", None))
        self.LabelDuration.setText(QCoreApplication.translate("EventInfoWindow", u"Duration:", None))
        self.LabelTime.setText(QCoreApplication.translate("EventInfoWindow", u"Starts:", None))
        self.LabelTimeValue.setText(QCoreApplication.translate("EventInfoWindow", u"<time>", None))
        self.LabelRoom.setText(QCoreApplication.translate("EventInfoWindow", u"Room:", None))
        self.LabelOrganizer.setText(QCoreApplication.translate("EventInfoWindow", u"Organizer", None))
        self.LabelOrganizerValue.setText(QCoreApplication.translate("EventInfoWindow", u"<name>", None))
        self.LabelPicture.setText("")

class EventInfoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_EventInfoWindow()
        self.ui.setupUi(self)
        # self.connectSignals()

    def showWindow(self):
        self.show()


