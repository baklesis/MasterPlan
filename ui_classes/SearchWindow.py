from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import schedule


class Ui_SearchWindow(object):
    def setupUi(self, searchbtn):
        if not searchbtn.objectName():
            searchbtn.setObjectName(u"searchbtn")
        searchbtn.resize(320, 320)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(searchbtn.sizePolicy().hasHeightForWidth())
        searchbtn.setSizePolicy(sizePolicy)
        searchbtn.setMinimumSize(QSize(320, 320))
        searchbtn.setMaximumSize(QSize(320, 320))
        self.lineEdit = QLineEdit(searchbtn)
        self.lineEdit.setObjectName(u"Search")
        self.lineEdit.setGeometry(QRect(30, 30, 171, 21))
        self.lineEdit.setMaximumSize(QSize(16777215, 100))
        self.searchButton = QPushButton(searchbtn)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setGeometry(QRect(200, 30, 31, 21))
        icon = QIcon()
        icon.addFile(u"icons/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchButton.setIcon(icon)
        self.horizontalLayoutWidget = QWidget(searchbtn)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(30, 30, 201, 21))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.listView = QListView(searchbtn)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(30, 50, 201, 191))
        self.verticalLayoutWidget = QWidget(searchbtn)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 30, 201, 211))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.retranslateUi(searchbtn)

        QMetaObject.connectSlotsByName(searchbtn)

    def retranslateUi(self, searchbtn):
        SearchWindow.setWindowTitle(QCoreApplication.translate("SearchWindow", u"Download", None))
        searchbtn.setWindowTitle(QCoreApplication.translate("Search Events", u"Form", None))
        self.searchButton.setText("")

class SearchWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SearchWindow()
        self.ui.setupUi(self)
        self.completer = QCompleter(schedule.event_list)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.searchbar.setCompleter(self.completer)

    def showWindow(self):
        self.show()

    def update_display(self, text):

        for event in schedule.event_list:
            if text.lower() in event.name.lower():
                event.show()
            else:
                event.hide()



