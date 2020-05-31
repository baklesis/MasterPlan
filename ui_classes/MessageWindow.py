from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QLocale)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# window ui class ######################################################################################################
class Ui_MessageWindow(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(300, 200)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(300, 200))
        Dialog.setMaximumSize(QSize(300, 200))
        Dialog.setContextMenuPolicy(Qt.DefaultContextMenu)
        Dialog.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.LayoutInfo = QHBoxLayout()
        self.LayoutInfo.setObjectName(u"LayoutInfo")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.LayoutInfo.addItem(self.horizontalSpacer_3)
        self.LabelInfo = QLabel(Dialog)
        self.LabelInfo.setObjectName(u"LabelInfo")
        sizePolicy.setHeightForWidth(self.LabelInfo.sizePolicy().hasHeightForWidth())
        self.LabelInfo.setSizePolicy(sizePolicy)
        self.LabelInfo.setMinimumSize(QSize(30, 30))
        self.LabelInfo.setMaximumSize(QSize(30, 30))
        self.LabelInfo.setPixmap(QPixmap(u"icons/info.png"))
        self.LabelInfo.setScaledContents(True)
        self.LayoutInfo.addWidget(self.LabelInfo)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.LayoutInfo.addItem(self.horizontalSpacer_4)
        self.verticalLayout.addLayout(self.LayoutInfo)
        self.LabelMessage = QLabel(Dialog)
        self.LabelMessage.setObjectName(u"LabelMessage")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.LabelMessage.sizePolicy().hasHeightForWidth())
        self.LabelMessage.setSizePolicy(sizePolicy1)
        self.LabelMessage.setMinimumSize(QSize(30, 0))
        self.LabelMessage.setMaximumSize(QSize(300, 16777215))
        self.LabelMessage.setAlignment(Qt.AlignCenter)
        self.LabelMessage.setWordWrap(True)
        self.verticalLayout.addWidget(self.LabelMessage)
        self.LayoutButtons = QHBoxLayout()
        self.LayoutButtons.setObjectName(u"LayoutButtons")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.LayoutButtons.addItem(self.horizontalSpacer)
        self.ButtonTrue = QPushButton(Dialog)
        self.ButtonTrue.setObjectName(u"ButtonTrue")
        self.LayoutButtons.addWidget(self.ButtonTrue)
        self.ButtonFalse = QPushButton(Dialog)
        self.ButtonFalse.setObjectName(u"ButtonFalse")
        self.LayoutButtons.addWidget(self.ButtonFalse)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.LayoutButtons.addItem(self.horizontalSpacer_2)
        self.verticalLayout.addLayout(self.LayoutButtons)
        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.verticalLayout.addItem(self.verticalSpacer)
        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Message", None))
        self.LabelInfo.setText("")
        self.LabelMessage.setText(QCoreApplication.translate("Dialog", u"<insert text>", None))
        self.ButtonTrue.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.ButtonFalse.setText(QCoreApplication.translate("Dialog", u"Cancel", None))

# window class #########################################################################################################
class MessageWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MessageWindow()
        self.ui.setupUi(self)
        self.connectSignals()

    def connectSignals(self):
        self.ui.ButtonTrue.clicked.connect(self.accept)
        self.ui.ButtonFalse.clicked.connect(self.reject)

    # domain functions

    def showLogInError(self):
        self.ui.LabelMessage.setText("Account not found.")
        self.ui.ButtonFalse.hide()
        self.ui.ButtonTrue.setText("OK")

    def showCreateEventError(self):
        self.LabelMessage.setText("Some fields are invalid or incomplete.")
        self.ButtonFalse.hide()
        self.ButtonTrue.setText("OK")



