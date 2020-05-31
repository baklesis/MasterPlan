from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from global_vars import *
from data_classes.roomGroup import *
from ui_classes.MessageWindow import MessageWindow

class Ui_EventCreateWindow(object):
    def setupUi(self, EventCreateWindow):
        if not EventCreateWindow.objectName():
            EventCreateWindow.setObjectName(u"EventCreateWindow")
        EventCreateWindow.setWindowModality(Qt.WindowModal)
        EventCreateWindow.resize(360, 360)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(EventCreateWindow.sizePolicy().hasHeightForWidth())
        EventCreateWindow.setSizePolicy(sizePolicy)
        EventCreateWindow.setMinimumSize(QSize(360, 360))
        EventCreateWindow.setMaximumSize(QSize(360, 360))
        self.verticalLayoutWidget = QWidget(EventCreateWindow)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 20, 321, 311))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 10)
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 154, 119))
        self.ListTags = QListWidget(self.scrollAreaWidgetContents)
        self.ListTags.setObjectName(u"ListTags")
        self.ListTags.setGeometry(QRect(0, 0, 181, 121))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 4, 1, 3, 2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer_4, 5, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.buttonBox = QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(EventCreateWindow)

        QMetaObject.connectSlotsByName(EventCreateWindow)
    # setupUi

    def retranslateUi(self, EventCreateWindow):
        EventCreateWindow.setWindowTitle(QCoreApplication.translate("EventCreateWindow", u"Create New Event", None))
        self.LabelRoomGroup.setText(QCoreApplication.translate("EventCreateWindow", u"Room Group:", None))
        self.LabelName.setText(QCoreApplication.translate("EventCreateWindow", u"Name:", None))
        self.LabelHours.setText(QCoreApplication.translate("EventCreateWindow", u"hours", None))
        self.LabelDuration.setText(QCoreApplication.translate("EventCreateWindow", u"Duration:", None))
        self.MenuRoomGroup.setItemText(0, QCoreApplication.translate("EventCreateWindow", u"None", None))

        self.LabelMinutes.setText(QCoreApplication.translate("EventCreateWindow", u"minutes", None))
        self.LabelTags.setText(QCoreApplication.translate("EventCreateWindow", u"Tags:", None))
    # retranslateUi

class EventCreateWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_EventCreateWindow()
        self.ui.setupUi(self)
        self.connectSignals()

    # domain functions
    def connectSignals(self):
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)

    def saveEvent(self):
        # checks if all complete and valid
        print("Clicked")
        if self.ui.FieldName.text() and (int(self.ui.FieldMinutes.text()) != 0):
            # gets Name and Duration and creates base Event in Schedule's event list
            newEvent = schedule.addEvent(self.ui.FieldName.text(),
                                         (int(self.ui.FieldHours.text()) * 60) + int(self.ui.FieldMinutes.text()), "No")
            # adds selected Room Group
            selected_room_group = self.ui.MenuRoomGroup.currentText()
            if selected_room_group != "None":
                newEvent.room_group = room_group_list.getRoomGroup(selected_room_group)
            # adds Tag list
            tag_list = []
            for i in range(self.ui.ListTags.count()):
                # it imports every tag to the organization's global TagList
                tag_list[i] = tag_list.addTag(self.ui.ListTags.item(i).text())
            # adds tags to event's tag list
            newEvent.tag_list = tag_list
            self.close()
            # if not complete shows message
        else:
            print("ok")
            self.messageWindow = MessageWindow()
            self.messageWindow.showCreateEventError()
            self.messageWindow.exec()
        return self

    def showWindow(self):
        for room_group in room_group_list.room_group_list:
            self.ui.MenuRoomGroup.addItem(room_group.name)
        return self.exec()