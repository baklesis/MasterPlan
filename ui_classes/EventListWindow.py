from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from ui_classes.OrganizerListWindow import OrganizerListWindow
from ui_classes.EventCreateWindow import EventCreateWindow
from ui_classes.OrganizerCreateWindow import OrganizerCreateWindow
from data_classes.event import *
from data_classes.schedule import *
from global_vars import *
from ui_classes.ConstraintWindow import ConstraintWindow
class Ui_EventListWindow(object):
    def setupUi(self, EventListWindow):
        if not EventListWindow.objectName():
            EventListWindow.setObjectName(u"EventListWindow")
        EventListWindow.resize(900, 520)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(EventListWindow.sizePolicy().hasHeightForWidth())
        EventListWindow.setSizePolicy(sizePolicy)
        EventListWindow.setMinimumSize(QSize(900, 520))
        EventListWindow.setMaximumSize(QSize(900, 520))
        self.centralwidget = QWidget(EventListWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 20, 252, 481))
        self.LayoutEventList = QVBoxLayout(self.verticalLayoutWidget)
        self.LayoutEventList.setObjectName(u"LayoutEventList")
        self.LayoutEventList.setContentsMargins(0, 0, 0, 0)
        self.LabelEventList = QLabel(self.verticalLayoutWidget)
        self.LabelEventList.setObjectName(u"LabelEventList")
        font = QFont()
        font.setPointSize(18)
        self.LabelEventList.setFont(font)
        self.LabelEventList.setFrameShape(QFrame.Box)
        self.LabelEventList.setAlignment(Qt.AlignCenter)

        self.LayoutEventList.addWidget(self.LabelEventList)

        self.ExtraButtons = QStackedWidget(self.verticalLayoutWidget)
        self.ExtraButtons.setObjectName(u"ExtraButtons")
        sizePolicy.setHeightForWidth(self.ExtraButtons.sizePolicy().hasHeightForWidth())
        self.ExtraButtons.setSizePolicy(sizePolicy)
        self.ExtraButtons.setMinimumSize(QSize(250, 34))
        self.AdminView_2 = QWidget()
        self.AdminView_2.setObjectName(u"AdminView_2")
        self.horizontalLayoutWidget = QWidget(self.AdminView_2)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 251, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.ButtonCreateOrganizer = QPushButton(self.horizontalLayoutWidget)
        self.ButtonCreateOrganizer.setObjectName(u"ButtonCreateOrganizer")

        self.horizontalLayout.addWidget(self.ButtonCreateOrganizer)

        self.ButtonCreateEvent = QPushButton(self.horizontalLayoutWidget)
        self.ButtonCreateEvent.setObjectName(u"ButtonCreateEvent")

        self.horizontalLayout.addWidget(self.ButtonCreateEvent)

        self.ExtraButtons.addWidget(self.AdminView_2)
        self.OrganizerView_2 = QWidget()
        self.OrganizerView_2.setObjectName(u"OrganizerView_2")
        self.ExtraButtons.addWidget(self.OrganizerView_2)

        self.LayoutEventList.addWidget(self.ExtraButtons)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.ButtonFilter = QPushButton(self.verticalLayoutWidget)
        self.ButtonFilter.setObjectName(u"ButtonFilter")

        self.horizontalLayout_2.addWidget(self.ButtonFilter)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.ButtonSort = QPushButton(self.verticalLayoutWidget)
        self.ButtonSort.setObjectName(u"ButtonSort")

        self.horizontalLayout_2.addWidget(self.ButtonSort)


        self.LayoutEventList.addLayout(self.horizontalLayout_2)

        self.ListEvents = QListWidget(self.verticalLayoutWidget)
        self.ListEvents.setObjectName(u"ListEvents")

        self.LayoutEventList.addWidget(self.ListEvents)

        self.EventEditFrame = QFrame(self.centralwidget)
        self.EventEditFrame.setObjectName(u"EventEditFrame")
        self.EventEditFrame.setGeometry(QRect(260, 20, 631, 481))
        self.EventEditFrame.setAutoFillBackground(False)
        self.EventEditFrame.setFrameShape(QFrame.StyledPanel)
        self.EventEditFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget_7 = QWidget(self.EventEditFrame)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(0, 0, 631, 481))
        self.LayoutEventDetails = QVBoxLayout(self.verticalLayoutWidget_7)
        self.LayoutEventDetails.setSpacing(0)
        self.LayoutEventDetails.setObjectName(u"LayoutEventDetails")
        self.LayoutEventDetails.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.LayoutEventDetails.setContentsMargins(0, 0, 0, 0)
        self.LabelDetails = QLabel(self.verticalLayoutWidget_7)
        self.LabelDetails.setObjectName(u"LabelDetails")
        self.LabelDetails.setFont(font)
        self.LabelDetails.setAlignment(Qt.AlignCenter)

        self.LayoutEventDetails.addWidget(self.LabelDetails)

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
        self.OrganizerView.setAutoFillBackground(False)
        self.gridLayoutWidget_2 = QWidget(self.OrganizerView)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 0, 621, 453))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_27 = QSpacerItem(150, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_27, 1, 1, 1, 1)

        self.LayoutTimeConstraints = QVBoxLayout()
        self.LayoutTimeConstraints.setSpacing(0)
        self.LayoutTimeConstraints.setObjectName(u"LayoutTimeConstraints")
        self.LayoutTimeConstraints.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_29)

        self.LabelTimeConstraints = QLabel(self.gridLayoutWidget_2)
        self.LabelTimeConstraints.setObjectName(u"LabelTimeConstraints")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.LabelTimeConstraints.sizePolicy().hasHeightForWidth())
        self.LabelTimeConstraints.setSizePolicy(sizePolicy2)
        self.LabelTimeConstraints.setMinimumSize(QSize(0, 34))
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        font1.setWeight(75)
        self.LabelTimeConstraints.setFont(font1)
        self.LabelTimeConstraints.setFrameShape(QFrame.Panel)
        self.LabelTimeConstraints.setFrameShadow(QFrame.Raised)
        self.LabelTimeConstraints.setLineWidth(1)
        self.LabelTimeConstraints.setMidLineWidth(1)
        self.LabelTimeConstraints.setAlignment(Qt.AlignCenter)
        self.LabelTimeConstraints.setMargin(6)

        self.horizontalLayout_15.addWidget(self.LabelTimeConstraints)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_30)


        self.LayoutTimeConstraints.addLayout(self.horizontalLayout_15)

        self.ListTimeConstraints = QListWidget(self.gridLayoutWidget_2)
        self.ListTimeConstraints.setObjectName(u"ListTimeConstraints")

        self.LayoutTimeConstraints.addWidget(self.ListTimeConstraints)


        self.gridLayout_3.addLayout(self.LayoutTimeConstraints, 0, 0, 1, 3)

        self.LayoutTagConstraints = QVBoxLayout()
        self.LayoutTagConstraints.setSpacing(0)
        self.LayoutTagConstraints.setObjectName(u"LayoutTagConstraints")
        self.LayoutTagConstraints.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_25)

        self.LabelTagConstraints = QLabel(self.gridLayoutWidget_2)
        self.LabelTagConstraints.setObjectName(u"LabelTagConstraints")
        sizePolicy2.setHeightForWidth(self.LabelTagConstraints.sizePolicy().hasHeightForWidth())
        self.LabelTagConstraints.setSizePolicy(sizePolicy2)
        self.LabelTagConstraints.setMinimumSize(QSize(0, 34))
        font2 = QFont()
        font2.setPointSize(13)
        font2.setBold(True)
        font2.setWeight(75)
        font2.setStrikeOut(False)
        font2.setKerning(True)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.LabelTagConstraints.setFont(font2)
        self.LabelTagConstraints.setFrameShape(QFrame.Panel)
        self.LabelTagConstraints.setFrameShadow(QFrame.Raised)
        self.LabelTagConstraints.setLineWidth(1)
        self.LabelTagConstraints.setMidLineWidth(1)
        self.LabelTagConstraints.setAlignment(Qt.AlignCenter)
        self.LabelTagConstraints.setMargin(6)

        self.horizontalLayout_13.addWidget(self.LabelTagConstraints)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_26)


        self.LayoutTagConstraints.addLayout(self.horizontalLayout_13)

        self.ListTagConstraints = QListWidget(self.gridLayoutWidget_2)
        self.ListTagConstraints.setObjectName(u"ListTagConstraints")

        self.LayoutTagConstraints.addWidget(self.ListTagConstraints)


        self.gridLayout_3.addLayout(self.LayoutTagConstraints, 2, 0, 1, 2)

        self.LabelRoomGroup = QLabel(self.gridLayoutWidget_2)
        self.LabelRoomGroup.setObjectName(u"LabelRoomGroup")

        self.gridLayout_3.addWidget(self.LabelRoomGroup, 6, 1, 1, 1)

        self.LayoutSpaceConstraint = QVBoxLayout()
        self.LayoutSpaceConstraint.setSpacing(0)
        self.LayoutSpaceConstraint.setObjectName(u"LayoutSpaceConstraint")
        self.LayoutSpaceConstraint.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_21)

        self.LabelSpaceTitle = QLabel(self.gridLayoutWidget_2)
        self.LabelSpaceTitle.setObjectName(u"LabelSpaceTitle")
        sizePolicy2.setHeightForWidth(self.LabelSpaceTitle.sizePolicy().hasHeightForWidth())
        self.LabelSpaceTitle.setSizePolicy(sizePolicy2)
        self.LabelSpaceTitle.setMinimumSize(QSize(0, 34))
        self.LabelSpaceTitle.setMaximumSize(QSize(16777215, 30))
        self.LabelSpaceTitle.setFont(font2)
        self.LabelSpaceTitle.setFrameShape(QFrame.Panel)
        self.LabelSpaceTitle.setFrameShadow(QFrame.Raised)
        self.LabelSpaceTitle.setLineWidth(1)
        self.LabelSpaceTitle.setMidLineWidth(1)
        self.LabelSpaceTitle.setAlignment(Qt.AlignCenter)
        self.LabelSpaceTitle.setMargin(6)

        self.horizontalLayout_11.addWidget(self.LabelSpaceTitle)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_22)


        self.LayoutSpaceConstraint.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_23 = QSpacerItem(60, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_23)

        self.FieldSpaceConstraint = QLineEdit(self.gridLayoutWidget_2)
        self.FieldSpaceConstraint.setObjectName(u"FieldSpaceConstraint")

        self.horizontalLayout_12.addWidget(self.FieldSpaceConstraint)

        self.horizontalSpacer_24 = QSpacerItem(60, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_24)


        self.LayoutSpaceConstraint.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.ButtonUpdateSpaceConstraint = QPushButton(self.gridLayoutWidget_2)
        self.ButtonUpdateSpaceConstraint.setObjectName(u"ButtonUpdateSpaceConstraint")
        sizePolicy.setHeightForWidth(self.ButtonUpdateSpaceConstraint.sizePolicy().hasHeightForWidth())
        self.ButtonUpdateSpaceConstraint.setSizePolicy(sizePolicy)

        self.horizontalLayout_16.addWidget(self.ButtonUpdateSpaceConstraint)


        self.LayoutSpaceConstraint.addLayout(self.horizontalLayout_16)


        self.gridLayout_3.addLayout(self.LayoutSpaceConstraint, 2, 2, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)

        self.ButtonAddTimeConstraint = QPushButton(self.gridLayoutWidget_2)
        self.ButtonAddTimeConstraint.setObjectName(u"ButtonAddTimeConstraint")

        self.horizontalLayout_9.addWidget(self.ButtonAddTimeConstraint)


        self.gridLayout_3.addLayout(self.horizontalLayout_9, 1, 2, 1, 1)

        self.LabelDateTitle = QLabel(self.gridLayoutWidget_2)
        self.LabelDateTitle.setObjectName(u"LabelDateTitle")

        self.gridLayout_3.addWidget(self.LabelDateTitle, 5, 0, 1, 1)

        self.LabelScheduledDatetime = QLabel(self.gridLayoutWidget_2)
        self.LabelScheduledDatetime.setObjectName(u"LabelScheduledDatetime")

        self.gridLayout_3.addWidget(self.LabelScheduledDatetime, 6, 0, 1, 1)

        self.LabelScheduledRoom = QLabel(self.gridLayoutWidget_2)
        self.LabelScheduledRoom.setObjectName(u"LabelScheduledRoom")

        self.gridLayout_3.addWidget(self.LabelScheduledRoom, 6, 2, 1, 1)

        self.LabelRoomTitle = QLabel(self.gridLayoutWidget_2)
        self.LabelRoomTitle.setObjectName(u"LabelRoomTitle")

        self.gridLayout_3.addWidget(self.LabelRoomTitle, 5, 2, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_13)

        self.ButtonAddTagConstraint = QPushButton(self.gridLayoutWidget_2)
        self.ButtonAddTagConstraint.setObjectName(u"ButtonAddTagConstraint")

        self.horizontalLayout_10.addWidget(self.ButtonAddTagConstraint)


        self.gridLayout_3.addLayout(self.horizontalLayout_10, 3, 1, 1, 1)

        self.LabelRoomGroupTitle = QLabel(self.gridLayoutWidget_2)
        self.LabelRoomGroupTitle.setObjectName(u"LabelRoomGroupTitle")

        self.gridLayout_3.addWidget(self.LabelRoomGroupTitle, 5, 1, 1, 1)

        self.DividingLine = QFrame(self.gridLayoutWidget_2)
        self.DividingLine.setObjectName(u"DividingLine")
        self.DividingLine.setFrameShape(QFrame.HLine)
        self.DividingLine.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.DividingLine, 4, 0, 1, 3)

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
        self.LayoutTags = QVBoxLayout()
        self.LayoutTags.setSpacing(0)
        self.LayoutTags.setObjectName(u"LayoutTags")
        self.verticalSpacer_2 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.LayoutTags.addItem(self.verticalSpacer_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.LabelTags = QLabel(self.gridLayoutWidget)
        self.LabelTags.setObjectName(u"LabelTags")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.LabelTags.sizePolicy().hasHeightForWidth())
        self.LabelTags.setSizePolicy(sizePolicy3)
        self.LabelTags.setMinimumSize(QSize(0, 30))
        self.LabelTags.setFont(font2)
        self.LabelTags.setFrameShape(QFrame.Panel)
        self.LabelTags.setFrameShadow(QFrame.Raised)
        self.LabelTags.setLineWidth(1)
        self.LabelTags.setMidLineWidth(0)
        self.LabelTags.setAlignment(Qt.AlignCenter)
        self.LabelTags.setMargin(6)

        self.horizontalLayout_6.addWidget(self.LabelTags)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_11)

        self.ButtonAddTag = QPushButton(self.gridLayoutWidget)
        self.ButtonAddTag.setObjectName(u"ButtonAddTag")

        self.horizontalLayout_6.addWidget(self.ButtonAddTag)


        self.LayoutTags.addLayout(self.horizontalLayout_6)

        self.listWidget_3 = QListWidget(self.gridLayoutWidget)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        self.listWidget_3.setObjectName(u"listWidget_3")
        self.listWidget_3.setEnabled(True)
        self.listWidget_3.setFlow(QListView.LeftToRight)

        self.LayoutTags.addWidget(self.listWidget_3)


        self.gridLayout.addLayout(self.LayoutTags, 5, 0, 1, 1)

        self.LabelDateTitle_2 = QLabel(self.gridLayoutWidget)
        self.LabelDateTitle_2.setObjectName(u"LabelDateTitle_2")

        self.gridLayout.addWidget(self.LabelDateTitle_2, 3, 0, 1, 1)

        self.DividingLine_2 = QFrame(self.gridLayoutWidget)
        self.DividingLine_2.setObjectName(u"DividingLine_2")
        self.DividingLine_2.setFrameShape(QFrame.HLine)
        self.DividingLine_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.DividingLine_2, 2, 0, 1, 3)

        self.LayoutSpaceConstraint_2 = QVBoxLayout()
        self.LayoutSpaceConstraint_2.setSpacing(0)
        self.LayoutSpaceConstraint_2.setObjectName(u"LayoutSpaceConstraint_2")
        self.LayoutSpaceConstraint_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_9)

        self.LabelSpaceTitle_2 = QLabel(self.gridLayoutWidget)
        self.LabelSpaceTitle_2.setObjectName(u"LabelSpaceTitle_2")
        sizePolicy2.setHeightForWidth(self.LabelSpaceTitle_2.sizePolicy().hasHeightForWidth())
        self.LabelSpaceTitle_2.setSizePolicy(sizePolicy2)
        self.LabelSpaceTitle_2.setMinimumSize(QSize(0, 30))
        self.LabelSpaceTitle_2.setFont(font2)
        self.LabelSpaceTitle_2.setFrameShape(QFrame.Panel)
        self.LabelSpaceTitle_2.setFrameShadow(QFrame.Raised)
        self.LabelSpaceTitle_2.setLineWidth(1)
        self.LabelSpaceTitle_2.setMidLineWidth(1)
        self.LabelSpaceTitle_2.setAlignment(Qt.AlignCenter)
        self.LabelSpaceTitle_2.setMargin(6)

        self.horizontalLayout_4.addWidget(self.LabelSpaceTitle_2)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_10)


        self.LayoutSpaceConstraint_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_7 = QSpacerItem(60, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)

        self.LabelSpaceConstraint = QLabel(self.gridLayoutWidget)
        self.LabelSpaceConstraint.setObjectName(u"LabelSpaceConstraint")
        self.LabelSpaceConstraint.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.LabelSpaceConstraint)

        self.horizontalSpacer_8 = QSpacerItem(60, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)


        self.LayoutSpaceConstraint_2.addLayout(self.horizontalLayout_5)


        self.gridLayout.addLayout(self.LayoutSpaceConstraint_2, 1, 0, 1, 1)

        self.LayoutTimeConstraints_2 = QVBoxLayout()
        self.LayoutTimeConstraints_2.setSpacing(0)
        self.LayoutTimeConstraints_2.setObjectName(u"LayoutTimeConstraints_2")
        self.LayoutTimeConstraints_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

        self.LabelTimeConstraints_2 = QLabel(self.gridLayoutWidget)
        self.LabelTimeConstraints_2.setObjectName(u"LabelTimeConstraints_2")
        sizePolicy2.setHeightForWidth(self.LabelTimeConstraints_2.sizePolicy().hasHeightForWidth())
        self.LabelTimeConstraints_2.setSizePolicy(sizePolicy2)
        self.LabelTimeConstraints_2.setMinimumSize(QSize(0, 30))
        self.LabelTimeConstraints_2.setFont(font2)
        self.LabelTimeConstraints_2.setFrameShape(QFrame.Panel)
        self.LabelTimeConstraints_2.setFrameShadow(QFrame.Raised)
        self.LabelTimeConstraints_2.setLineWidth(1)
        self.LabelTimeConstraints_2.setMidLineWidth(1)
        self.LabelTimeConstraints_2.setAlignment(Qt.AlignCenter)
        self.LabelTimeConstraints_2.setMargin(6)

        self.horizontalLayout_7.addWidget(self.LabelTimeConstraints_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)


        self.LayoutTimeConstraints_2.addLayout(self.horizontalLayout_7)

        self.listWidget = QListWidget(self.gridLayoutWidget)
        self.listWidget.setObjectName(u"listWidget")

        self.LayoutTimeConstraints_2.addWidget(self.listWidget)


        self.gridLayout.addLayout(self.LayoutTimeConstraints_2, 0, 0, 1, 1)

        self.LayoutTagConstraints_2 = QVBoxLayout()
        self.LayoutTagConstraints_2.setSpacing(0)
        self.LayoutTagConstraints_2.setObjectName(u"LayoutTagConstraints_2")
        self.LayoutTagConstraints_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.LabelTagConstraints_2 = QLabel(self.gridLayoutWidget)
        self.LabelTagConstraints_2.setObjectName(u"LabelTagConstraints_2")
        sizePolicy2.setHeightForWidth(self.LabelTagConstraints_2.sizePolicy().hasHeightForWidth())
        self.LabelTagConstraints_2.setSizePolicy(sizePolicy2)
        self.LabelTagConstraints_2.setMinimumSize(QSize(0, 30))
        self.LabelTagConstraints_2.setFont(font2)
        self.LabelTagConstraints_2.setFrameShape(QFrame.Panel)
        self.LabelTagConstraints_2.setFrameShadow(QFrame.Raised)
        self.LabelTagConstraints_2.setLineWidth(1)
        self.LabelTagConstraints_2.setMidLineWidth(1)
        self.LabelTagConstraints_2.setAlignment(Qt.AlignCenter)
        self.LabelTagConstraints_2.setMargin(6)

        self.horizontalLayout_3.addWidget(self.LabelTagConstraints_2)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.LayoutTagConstraints_2.addLayout(self.horizontalLayout_3)

        self.ListTagConstraints_2 = QListWidget(self.gridLayoutWidget)
        self.ListTagConstraints_2.setObjectName(u"ListTagConstraints_2")

        self.LayoutTagConstraints_2.addWidget(self.ListTagConstraints_2)


        self.gridLayout.addLayout(self.LayoutTagConstraints_2, 0, 2, 1, 1)

        self.LabelScheduledRoom_2 = QLabel(self.gridLayoutWidget)
        self.LabelScheduledRoom_2.setObjectName(u"LabelScheduledRoom_2")
        self.LabelScheduledRoom_2.setIndent(6)

        self.gridLayout.addWidget(self.LabelScheduledRoom_2, 4, 2, 1, 1)

        self.LabelScheduledDatetime_2 = QLabel(self.gridLayoutWidget)
        self.LabelScheduledDatetime_2.setObjectName(u"LabelScheduledDatetime_2")

        self.gridLayout.addWidget(self.LabelScheduledDatetime_2, 4, 0, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_12, 0, 1, 1, 1)

        self.LabelRoomTitle_2 = QLabel(self.gridLayoutWidget)
        self.LabelRoomTitle_2.setObjectName(u"LabelRoomTitle_2")
        self.LabelRoomTitle_2.setMargin(0)
        self.LabelRoomTitle_2.setIndent(6)

        self.gridLayout.addWidget(self.LabelRoomTitle_2, 3, 2, 1, 1)

        self.LayoutExecuteScheduling = QVBoxLayout()
        self.LayoutExecuteScheduling.setSpacing(6)
        self.LayoutExecuteScheduling.setObjectName(u"LayoutExecuteScheduling")
        self.LabelRoomGroupTitle_2 = QLabel(self.gridLayoutWidget)
        self.LabelRoomGroupTitle_2.setObjectName(u"LabelRoomGroupTitle_2")
        self.LabelRoomGroupTitle_2.setMargin(2)
        self.LabelRoomGroupTitle_2.setIndent(4)

        self.LayoutExecuteScheduling.addWidget(self.LabelRoomGroupTitle_2)

        self.LabelRoomGroup_2 = QLabel(self.gridLayoutWidget)
        self.LabelRoomGroup_2.setObjectName(u"LabelRoomGroup_2")
        self.LabelRoomGroup_2.setMargin(2)
        self.LabelRoomGroup_2.setIndent(4)

        self.LayoutExecuteScheduling.addWidget(self.LabelRoomGroup_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.LayoutExecuteScheduling.addItem(self.verticalSpacer)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.ButtonExecute = QPushButton(self.gridLayoutWidget)
        self.ButtonExecute.setObjectName(u"ButtonExecute")
        sizePolicy.setHeightForWidth(self.ButtonExecute.sizePolicy().hasHeightForWidth())
        self.ButtonExecute.setSizePolicy(sizePolicy)
        self.ButtonExecute.setMinimumSize(QSize(170, 32))
        font3 = QFont()
        font3.setBold(True)
        font3.setItalic(False)
        font3.setWeight(75)
        self.ButtonExecute.setFont(font3)
        self.ButtonExecute.setLayoutDirection(Qt.LeftToRight)
        self.ButtonExecute.setFlat(False)

        self.horizontalLayout_14.addWidget(self.ButtonExecute)


        self.LayoutExecuteScheduling.addLayout(self.horizontalLayout_14)


        self.gridLayout.addLayout(self.LayoutExecuteScheduling, 5, 2, 1, 1)

        self.LayoutAssignOrganizer = QVBoxLayout()
        self.LayoutAssignOrganizer.setSpacing(0)
        self.LayoutAssignOrganizer.setObjectName(u"LayoutAssignOrganizer")
        self.LayoutAssignOrganizer.setContentsMargins(8, 8, 8, 8)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.LabelAssignedOrganizer = QLabel(self.gridLayoutWidget)
        self.LabelAssignedOrganizer.setObjectName(u"LabelAssignedOrganizer")
        self.LabelAssignedOrganizer.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.LabelAssignedOrganizer)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_14)

        self.ButtonAssignOrganizer = QPushButton(self.gridLayoutWidget)
        self.ButtonAssignOrganizer.setObjectName(u"ButtonAssignOrganizer")

        self.horizontalLayout_8.addWidget(self.ButtonAssignOrganizer)


        self.LayoutAssignOrganizer.addLayout(self.horizontalLayout_8)


        self.gridLayout.addLayout(self.LayoutAssignOrganizer, 1, 2, 1, 1)

        self.stackedWidget_2.addWidget(self.AdminView)

        self.LayoutEventDetails.addWidget(self.stackedWidget_2)

        self.LabelHint = QLabel(self.centralwidget)
        self.LabelHint.setObjectName(u"LabelHint")
        self.LabelHint.setGeometry(QRect(440, 260, 281, 20))
        EventListWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(EventListWindow)

        self.ExtraButtons.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.ButtonExecute.setDefault(False)


        QMetaObject.connectSlotsByName(EventListWindow)
    # setupUi

    def retranslateUi(self, EventListWindow):
        EventListWindow.setWindowTitle(QCoreApplication.translate("EventListWindow", u"Edit Mode", None))
        self.LabelEventList.setText(QCoreApplication.translate("EventListWindow", u"Event List", None))
        self.ButtonCreateOrganizer.setText(QCoreApplication.translate("EventListWindow", u"Create Organizer", None))
        self.ButtonCreateEvent.setText(QCoreApplication.translate("EventListWindow", u"Create Event", None))
        self.ButtonFilter.setText(QCoreApplication.translate("EventListWindow", u"Filter", None))
        self.ButtonSort.setText(QCoreApplication.translate("EventListWindow", u"Sort", None))
        self.LabelDetails.setText(QCoreApplication.translate("EventListWindow", u"Event Details", None))
        self.LabelTimeConstraints.setText(QCoreApplication.translate("EventListWindow", u"Time Constraints", None))
        self.LabelTagConstraints.setText(QCoreApplication.translate("EventListWindow", u"Tag Constraints", None))
        self.LabelRoomGroup.setText(QCoreApplication.translate("EventListWindow", u"<Room Group>", None))
        self.LabelSpaceTitle.setText(QCoreApplication.translate("EventListWindow", u"Space Constraint", None))
        self.ButtonUpdateSpaceConstraint.setText(QCoreApplication.translate("EventListWindow", u"Update", None))
        self.ButtonAddTimeConstraint.setText(QCoreApplication.translate("EventListWindow", u"Add", None))
        self.LabelDateTitle.setText(QCoreApplication.translate("EventListWindow", u"Current Scheduled Date and Time:", None))
        self.LabelScheduledDatetime.setText(QCoreApplication.translate("EventListWindow", u"<Datetime>", None))
        self.LabelScheduledRoom.setText(QCoreApplication.translate("EventListWindow", u"<Room>", None))
        self.LabelRoomTitle.setText(QCoreApplication.translate("EventListWindow", u"Current Scheduled Room:", None))
        self.ButtonAddTagConstraint.setText(QCoreApplication.translate("EventListWindow", u"Add", None))
        self.LabelRoomGroupTitle.setText(QCoreApplication.translate("EventListWindow", u"Event Room Group:", None))
        self.LabelTags.setText(QCoreApplication.translate("EventListWindow", u"Tags", None))
        self.ButtonAddTag.setText(QCoreApplication.translate("EventListWindow", u"Add", None))

        __sortingEnabled = self.listWidget_3.isSortingEnabled()
        self.listWidget_3.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget_3.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("EventListWindow", u"New Item", None));
        ___qlistwidgetitem1 = self.listWidget_3.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("EventListWindow", u"New Item", None));
        ___qlistwidgetitem2 = self.listWidget_3.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("EventListWindow", u"New Item", None));
        ___qlistwidgetitem3 = self.listWidget_3.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("EventListWindow", u"New Item", None));
        ___qlistwidgetitem4 = self.listWidget_3.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("EventListWindow", u"New Item", None));
        ___qlistwidgetitem5 = self.listWidget_3.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("EventListWindow", u"New Item", None));
        ___qlistwidgetitem6 = self.listWidget_3.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("EventListWindow", u"New Item", None));
        ___qlistwidgetitem7 = self.listWidget_3.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("EventListWindow", u"New Item", None));
        self.listWidget_3.setSortingEnabled(__sortingEnabled)

        self.LabelDateTitle_2.setText(QCoreApplication.translate("EventListWindow", u"Current Scheduled Date and Time:", None))
        self.LabelSpaceTitle_2.setText(QCoreApplication.translate("EventListWindow", u"Space Constraint", None))
        self.LabelSpaceConstraint.setText(QCoreApplication.translate("EventListWindow", u"<SpaceConstraint>", None))
        self.LabelTimeConstraints_2.setText(QCoreApplication.translate("EventListWindow", u"Time Constraints", None))
        self.LabelTagConstraints_2.setText(QCoreApplication.translate("EventListWindow", u"Tag Constraints", None))
        self.LabelScheduledRoom_2.setText(QCoreApplication.translate("EventListWindow", u"<Room>", None))
        self.LabelScheduledDatetime_2.setText(QCoreApplication.translate("EventListWindow", u"<Datetime>", None))
        self.LabelRoomTitle_2.setText(QCoreApplication.translate("EventListWindow", u"Current Scheduled Room:", None))
        self.LabelRoomGroupTitle_2.setText(QCoreApplication.translate("EventListWindow", u"Event Room Group:", None))
        self.LabelRoomGroup_2.setText(QCoreApplication.translate("EventListWindow", u"<RoomGroup>", None))
        self.ButtonExecute.setText(QCoreApplication.translate("EventListWindow", u"Execute scheduling", None))
        self.LabelAssignedOrganizer.setText(QCoreApplication.translate("EventListWindow", u"Assigned Organizer:", None))
        self.ButtonAssignOrganizer.setText(QCoreApplication.translate("EventListWindow", u"Assign", None))
        self.LabelHint.setText(QCoreApplication.translate("EventListWindow", u"Please select an event from the list on the left", None))
    # retranslateUi

class EventListWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_EventListWindow()
        self.ui.setupUi(self)
        self.connectSignals()

    def connectSignals(self):
        self.ui.ButtonCreateEvent.clicked.connect(self.createEvent)
        self.ui.ButtonCreateOrganizer.clicked.connect(self.createOrganizer)
        self.ui.ListEvents.itemDoubleClicked.connect(self.selectEvent)
        self.ui.ButtonAddTimeConstraint.clicked.connect(self.addTimeConstraint)
        self.ui.ButtonAddTagConstraint.clicked.connect(self.addTagConstraint)
        self.ui.ButtonAssignOrganizer.clicked.connect(self.assignOrganizer)
        self.ui.ButtonAddTag.clicked.connect(self.addTag)
        self.ui.ButtonExecute.clicked.connect(self.executeScheduling)
        self.ui.listWidget_3.itemChanged.connect(self.renameTag)
        self.ui.ButtonUpdateSpaceConstraint.clicked.connect(self.setSpaceConstraint)

    def selectEvent(self):
        self.ui.LabelAssignedOrganizer.setText("Assigned Organizer:")
        self.ui.ButtonAssignOrganizer.show()
        self.ui.LabelHint.hide()
        selected_event = schedule.getEvent(self.ui.ListEvents.currentItem().text())
        # set event's labels
        self.ui.LabelDetails.setText(selected_event["object"].name)
        if selected_event["datetime"] == None:
            self.ui.LabelScheduledDatetime.setText("<font color=red>Not Scheduled Yet!</font>")
            self.ui.LabelScheduledDatetime_2.setText("<font color=red>Not Scheduled Yet!</font>")
        else:
            self.ui.LabelScheduledDatetime.setText(selected_event["datetime"].strftime("%d/%m/%Y, %H:%M"))
            self.ui.LabelScheduledDatetime_2.setText(selected_event["datetime"].strftime("%d/%m/%Y, %H:%M"))
            self.ui.LabelScheduledRoom.setText(selected_event["room"].name)
            self.ui.LabelScheduledRoom_2.setText(selected_event["room"].name)
        eventRoomGroup = selected_event["object"].room_group
        if eventRoomGroup == None:
            self.ui.LabelRoomGroup.setText("None")
            self.ui.LabelRoomGroup_2.setText("None")
        else:
            self.ui.LabelRoomGroup.setText(selected_event["object"].room_group.name)
            self.ui.LabelRoomGroup_2.setText(selected_event["object"].room_group.name)
            # update lists
        for tag in reversed(range(self.ui.listWidget_3.count())):
            self.ui.listWidget_3.takeItem(tag)
        for tag in selected_event["object"].tag_list:
            self.ui.listWidget_3.addItem(tag.name)
        for constraint in reversed(range(self.ui.ListTagConstraints.count())):
            self.ui.ListTagConstraints.takeItem(constraint)
        for constraint in reversed(range(self.ui.ListTagConstraints_2.count())):
            self.ui.ListTagConstraints_2.takeItem(constraint)
        for constraint in reversed(range(self.ui.ListTimeConstraints.count())):
            self.ui.ListTimeConstraints.takeItem(constraint)
        for constraint in reversed(range(self.ui.listWidget.count())):
            self.ui.listWidget.takeItem(constraint)
        self.ui.FieldSpaceConstraint.setText("Enter preffered capacity")
        self.ui.LabelSpaceConstraint.setText("None")
        for constraint in selected_event["object"].constraint_list:
            if type(constraint).__name__ == "TagConstraint":
                self.ui.ListTagConstraints.addItem(constraint.tag.name + " (" + constraint.weight + ")")
                self.ui.ListTagConstraints_2.addItem(constraint.tag.name + " (" + constraint.weight + ")")
            if type(constraint).__name__ == "TimeConstraint":
                start_time = constraint.start_datetime.strftime("%d/%m/%Y, %H:%M")
                end_time = constraint.end_datetime.strftime("%d/%m/%Y, %H:%M")
                self.ui.ListTimeConstraints.addItem(start_time + " - " + end_time  + " (" + constraint.weight + ")")
                self.ui.listWidget.addItem(start_time + " - " + end_time  + " (" + constraint.weight + ")")
            if type(constraint).__name__ == "SpaceConstraint":
                self.ui.LabelSpaceConstraint.setText(constraint.space)
                self.ui.FieldSpaceConstraint.setText(constraint.space)
        if selected_event["object"].organizer is not None:
            self.ui.ButtonAssignOrganizer.hide()
            self.ui.LabelAssignedOrganizer.setText("Assigned Organizer: " + selected_event["object"].organizer.fullname)
        self.ui.EventEditFrame.show()

    def addTimeConstraint(self):
        selectedEvent = schedule.getEvent(self.ui.LabelDetails.text())
        self.timeconstraintWindow=ConstraintWindow(selectedEvent)
        self.timeconstraintWindow.ui.stackedWidget.setCurrentIndex(0)
        response = self.timeconstraintWindow.showWindow()
        if response == 1:
            self.timeconstraintWindow.saveConstraint()
            self.selectEvent()

    def addTagConstraint(self):
        selectedEvent = schedule.getEvent(self.ui.LabelDetails.text())
        self.tagConstraintWindow=ConstraintWindow(selectedEvent)
        self.tagConstraintWindow.ui.stackedWidget.setCurrentIndex(1)
        response = self.tagConstraintWindow.showWindow()
        if response == 1:
            self.tagConstraintWindow.saveConstraint()
            self.selectEvent()

    def createEvent(self):
        self.eventCreateWindow = EventCreateWindow()
        response = self.eventCreateWindow.showWindow()
        if response == 1:
            self.eventCreateWindow.saveEvent()
        self.fillEvents()

    def createOrganizer(self):
        self.organizerCreateWindow = OrganizerCreateWindow()
        response = self.organizerCreateWindow.showWindow()
        if response == 1:
            self.organizerCreateWindow. createOrganizer()

    def fillEvents(self):
        if session.getUserType() == "Admin":
            for event in reversed(range(self.ui.ListEvents.count())):
                self.ui.ListEvents.takeItem(event)
            for event in schedule.event_list:
                self.ui.ListEvents.addItem(event["object"].name)
        else:
            for event in reversed(range(self.ui.ListEvents.count())):
                self.ui.ListEvents.takeItem(event)
            for event in schedule.event_list:
                if event["object"].organizer == session.current_user:
                    self.ui.ListEvents.addItem(event["object"].name)

    def showWindow(self):
        self.show()
        self.ui.EventEditFrame.hide()
        self.fillEvents()

    def addTag(self):
        current_event = schedule.getEvent(self.ui.LabelDetails.text())
        current_event["object"].addTag("New Tag", tag_list)
        for tag in reversed(range(self.ui.listWidget_3.count())):
            self.ui.listWidget_3.takeItem(tag)
        for tag in current_event["object"].tag_list:
            self.ui.listWidget_3.addItem(tag.name)
            if tag.name == "New Tag":
                new_tag = self.ui.listWidget_3.item(self.ui.listWidget_3.count()-1)
                new_tag.setForeground(Qt.gray)
        last_item = self.ui.listWidget_3.item(self.ui.listWidget_3.count() - 1)
        last_item.setFlags(last_item.flags() | Qt.ItemIsEditable)

    def renameTag(self):
        current_event = schedule.getEvent(self.ui.LabelDetails.text())
        current_tag_name = self.ui.listWidget_3.item(self.ui.listWidget_3.count()-1).text()
        if current_tag_name == "New Tag":
            current_event["object"].removeTag(current_tag_name, tag_list, schedule)
            return None
        current_event["object"].removeTag(current_tag_name, tag_list, schedule)
        current_event["object"].addTag(current_tag_name, tag_list)
        for tag in reversed(range(self.ui.listWidget_3.count())):
            self.ui.listWidget_3.takeItem(tag)
        for tag in current_event["object"].tag_list:
            self.ui.listWidget_3.addItem(tag.name)

    def setSpaceConstraint(self):
        current_event = schedule.getEvent(self.ui.LabelDetails.text())
        size = self.ui.FieldSpaceConstraint.text()
        try:
            if int(size) < 2000 and int(size) > 0:
                constraint = SpaceConstraint(session.current_user, size)
                current_event["object"].addConstraint(constraint)
                self.selectEvent()
            else:
                self.ui.FieldSpaceConstraint.setText("Invalid number")
        except:
            self.ui.FieldSpaceConstraint.setText("Not a number")
    def assignOrganizer(self):
        selected_event = self.ui.LabelDetails.text()
        self.organizerListWindow = OrganizerListWindow(selected_event)
        response = self.organizerListWindow.showWindow()
        if response == 1:
            self.organizerListWindow.assignOrganizer()
        self.selectEvent()

    def executeScheduling(self):
        global schedule
        schedule = schedule.executeScheduling(room_list)