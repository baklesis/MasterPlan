from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from global_vars import *

class Ui_OrganizerListWindow(object):
    def setupUi(self, OrganizerListWindow):
        if not OrganizerListWindow.objectName():
            OrganizerListWindow.setObjectName(u"OrganizerListWindow")
        OrganizerListWindow.resize(360, 480)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(OrganizerListWindow.sizePolicy().hasHeightForWidth())
        OrganizerListWindow.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget = QWidget(OrganizerListWindow)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 20, 301, 431))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.LabelSelect = QLabel(self.verticalLayoutWidget)
        self.LabelSelect.setObjectName(u"LabelSelect")
        font = QFont()
        font.setPointSize(18)
        self.LabelSelect.setFont(font)
        self.LabelSelect.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.LabelSelect)

        self.LabelPrompt = QLabel(self.verticalLayoutWidget)
        self.LabelPrompt.setObjectName(u"LabelPrompt")
        self.LabelPrompt.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.LabelPrompt)

        self.ListOrganizers = QListWidget(self.verticalLayoutWidget)
        self.ListOrganizers.setObjectName(u"ListOrganizers")
        self.ListOrganizers.setAlternatingRowColors(True)
        self.ListOrganizers.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.ListOrganizers.setLayoutMode(QListView.SinglePass)
        self.ListOrganizers.setModelColumn(0)
        self.ListOrganizers.setUniformItemSizes(False)
        self.ListOrganizers.setSelectionRectVisible(False)
        self.ListOrganizers.setSortingEnabled(True)

        self.verticalLayout.addWidget(self.ListOrganizers)

        self.LayoutButtons = QHBoxLayout()
        self.LayoutButtons.setObjectName(u"LayoutButtons")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.LayoutButtons.addItem(self.horizontalSpacer)

        self.ButtonCancel = QPushButton(self.verticalLayoutWidget)
        self.ButtonCancel.setObjectName(u"ButtonCancel")

        self.LayoutButtons.addWidget(self.ButtonCancel)

        self.ButtonAssign = QPushButton(self.verticalLayoutWidget)
        self.ButtonAssign.setObjectName(u"ButtonAssign")

        self.LayoutButtons.addWidget(self.ButtonAssign)


        self.verticalLayout.addLayout(self.LayoutButtons)


        self.retranslateUi(OrganizerListWindow)

        self.ButtonAssign.setDefault(True)


        QMetaObject.connectSlotsByName(OrganizerListWindow)
    # setupUi

    def retranslateUi(self, OrganizerListWindow):
        OrganizerListWindow.setWindowTitle(QCoreApplication.translate("OrganizerListWindow", u"Dialog", None))
        self.LabelSelect.setText(QCoreApplication.translate("OrganizerListWindow", u"Select Organizer", None))
        self.LabelPrompt.setText(QCoreApplication.translate("OrganizerListWindow", u"Assign an organizer to this event", None))

        __sortingEnabled = self.ListOrganizers.isSortingEnabled()
        self.ListOrganizers.setSortingEnabled(False)
        self.ListOrganizers.setSortingEnabled(__sortingEnabled)

        self.ButtonCancel.setText(QCoreApplication.translate("OrganizerListWindow", u"Cancel", None))
        self.ButtonAssign.setText(QCoreApplication.translate("OrganizerListWindow", u"Assign", None))
    # retranslateUi

class OrganizerListWindow(QDialog):
    def __init__(self, selected_event):
        super().__init__()
        self.ui = Ui_OrganizerListWindow()
        self.ui.setupUi(self)
        self.connectSignals()
        self.selected_event = selected_event

    def connectSignals(self):
        self.ui.ButtonCancel.clicked.connect(self.reject)
        self.ui.ButtonAssign.clicked.connect(self.accept)

    def assignOrganizer(self):
        selected_organizer = self.ui.ListOrganizers.currentItem().text()
        schedule.getEvent(self.selected_event).organizer = organizer_list.getOrganizer(selected_organizer)

    def showWindow(self):
        fullnames = [x.fullname for x in organizer_list.organizer_list]
        sameFullnames = [x for x in fullnames if fullnames.count(x) >= 2]
        sameFullnames = [organizer_list.getOrganizer(x) for x in sameFullnames]
        for organizer in organizer_list.organizer_list:
            if organizer in sameFullnames:
                self.ui.ListOrganizers.addItem(organizer.fullname + " (" +  organizer.username + ")")
            else:
                self.ui.ListOrganizers.addItem(organizer.fullname)
        self.exec()

