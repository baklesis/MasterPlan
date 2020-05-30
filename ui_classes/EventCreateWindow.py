from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from data_classes import *
from global_vars import *

class Ui_EventCreateWindow(object):
    def setupUi(self, EventCreateWindow):
        if not EventCreateWindow.objectName():
            EventCreateWindow.setObjectName(u"EventCreateWindow")
        EventCreateWindow.setWindowModality(Qt.ApplicationModal)
        EventCreateWindow.resize(360, 480)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(EventCreateWindow.sizePolicy().hasHeightForWidth())
        EventCreateWindow.setSizePolicy(sizePolicy)
        EventCreateWindow.setMinimumSize(QSize(360, 480))
        EventCreateWindow.setMaximumSize(QSize(360, 480))
        self.centralwidget = QWidget(EventCreateWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 20, 321, 441))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 10)
        self.TitleWindow = QLabel(self.verticalLayoutWidget)
        self.TitleWindow.setObjectName(u"TitleWindow")
        font = QFont()
        font.setPointSize(18)
        self.TitleWindow.setFont(font)
        self.TitleWindow.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.TitleWindow)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.FieldHours = QSpinBox(self.verticalLayoutWidget)
        self.FieldHours.setObjectName(u"FieldHours")

        self.gridLayout.addWidget(self.FieldHours, 1, 1, 1, 1)

        self.FieldMinutes = QSpinBox(self.verticalLayoutWidget)
        self.FieldMinutes.setObjectName(u"FieldMinutes")

        self.gridLayout.addWidget(self.FieldMinutes, 2, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(70, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 2, 1, 1)

        self.LabelRoomGroup = QLabel(self.verticalLayoutWidget)
        self.LabelRoomGroup.setObjectName(u"LabelRoomGroup")
        self.LabelRoomGroup.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.LabelRoomGroup, 3, 0, 1, 1)

        self.LabelName = QLabel(self.verticalLayoutWidget)
        self.LabelName.setObjectName(u"LabelName")
        self.LabelName.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.LabelName, 0, 0, 1, 1)

        self.FieldName = QLineEdit(self.verticalLayoutWidget)
        self.FieldName.setObjectName(u"FieldName")

        self.gridLayout.addWidget(self.FieldName, 0, 1, 1, 1)

        self.LabelHours = QLabel(self.verticalLayoutWidget)
        self.LabelHours.setObjectName(u"LabelHours")

        self.gridLayout.addWidget(self.LabelHours, 1, 2, 1, 1)

        self.LabelDuration = QLabel(self.verticalLayoutWidget)
        self.LabelDuration.setObjectName(u"LabelDuration")
        self.LabelDuration.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.LabelDuration, 1, 0, 1, 1)

        self.MenuRoomGroup = QComboBox(self.verticalLayoutWidget)
        self.MenuRoomGroup.addItem("")
        self.MenuRoomGroup.setObjectName(u"MenuRoomGroup")

        self.gridLayout.addWidget(self.MenuRoomGroup, 3, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(70, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 3, 3, 1, 1)

        self.LabelMinutes = QLabel(self.verticalLayoutWidget)
        self.LabelMinutes.setObjectName(u"LabelMinutes")

        self.gridLayout.addWidget(self.LabelMinutes, 2, 2, 1, 1)

        self.LabelTags = QLabel(self.verticalLayoutWidget)
        self.LabelTags.setObjectName(u"LabelTags")
        self.LabelTags.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.LabelTags, 4, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer_3, 6, 0, 1, 1)

        self.scrollArea = QScrollArea(self.verticalLayoutWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 159, 114))
        self.ListTags = QListWidget(self.scrollAreaWidgetContents)
        self.ListTags.setObjectName(u"ListTags")
        self.ListTags.setGeometry(QRect(0, 0, 181, 121))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 4, 1, 3, 2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer_4, 5, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(30, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.ButtonSave = QPushButton(self.verticalLayoutWidget)
        self.ButtonSave.setObjectName(u"ButtonSave")

        self.horizontalLayout_2.addWidget(self.ButtonSave)

        self.horizontalSpacer_3 = QSpacerItem(30, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.ButtonCancel = QPushButton(self.verticalLayoutWidget)
        self.ButtonCancel.setObjectName(u"ButtonCancel")

        self.horizontalLayout_2.addWidget(self.ButtonCancel)

        self.horizontalSpacer_5 = QSpacerItem(30, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        EventCreateWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(EventCreateWindow)

        QMetaObject.connectSlotsByName(EventCreateWindow)
    # setupUi

    def retranslateUi(self, EventCreateWindow):
        EventCreateWindow.setWindowTitle(QCoreApplication.translate("EventCreateWindow", u"MainView", None))
        self.TitleWindow.setText(QCoreApplication.translate("EventCreateWindow", u"Create New Event", None))
        self.LabelRoomGroup.setText(QCoreApplication.translate("EventCreateWindow", u"Room Group:", None))
        self.LabelName.setText(QCoreApplication.translate("EventCreateWindow", u"Name:", None))
        self.LabelHours.setText(QCoreApplication.translate("EventCreateWindow", u"hours", None))
        self.LabelDuration.setText(QCoreApplication.translate("EventCreateWindow", u"Duration:", None))
        self.MenuRoomGroup.setItemText(0, QCoreApplication.translate("EventCreateWindow", u"None", None))

        self.LabelMinutes.setText(QCoreApplication.translate("EventCreateWindow", u"minutes", None))
        self.LabelTags.setText(QCoreApplication.translate("EventCreateWindow", u"Tags:", None))
        self.ButtonSave.setText(QCoreApplication.translate("EventCreateWindow", u"Save", None))
        self.ButtonCancel.setText(QCoreApplication.translate("EventCreateWindow", u"Cancel", None))
    # retranslateUi

    def connectSignals(self):
        self.ButtonSave.clicked.connect(self.saveEvent())


    # domain functions

    def saveEvent(self):
        # checks if all complete and valid
        # gets Name and Duration and creates base Event in Schedule's event list
        newEvent = schedule.addEvent(self.FieldName.text(),int(self.FieldHours.text())*60+int(self.FieldMinutes.text()))
        # adds selected Room Group
        newEvent.room_group=self.MenuRoomGroup.currentText()
        # adds Tag list
        tag_list=[]
        for i in range(self.ListTags.count()):
            # it imports every tag to the organization's global TagList
            tag_list[i] = TagList.addTag(self.ListTags.item(i).text())
        # adds tags to event's tag list
        newEvent.tag_list = tag_list
        # if not complete shows message

        return self