from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from global_vars import schedule


class Ui_SearchWindow(object):
    def setupUi(self, SearchWindow):
        if not SearchWindow.objectName():
            SearchWindow.setObjectName(u"SearchWindow")
        SearchWindow.resize(320, 320)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SearchWindow.sizePolicy().hasHeightForWidth())
        SearchWindow.setSizePolicy(sizePolicy)
        SearchWindow.setMinimumSize(QSize(320, 320))
        SearchWindow.setMaximumSize(QSize(320, 320))
        self.searchBar = QLineEdit(SearchWindow)
        self.searchBar.setObjectName(u"searchBar")
        self.searchBar.setGeometry(QRect(30, 30, 171, 21))
        self.searchBar.setMaximumSize(QSize(16777215, 100))
        self.searchButton = QPushButton(SearchWindow)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setGeometry(QRect(200, 30, 31, 21))
        icon = QIcon()
        icon.addFile(u"../icons/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchButton.setIcon(icon)
        self.horizontalLayoutWidget = QWidget(SearchWindow)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(30, 30, 201, 21))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.searchResults = QListView(SearchWindow)
        self.searchResults.setObjectName(u"searchResults")
        self.searchResults.setGeometry(QRect(30, 50, 201, 191))
        self.verticalLayoutWidget = QWidget(SearchWindow)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 30, 201, 211))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.retranslateUi(SearchWindow)

        QMetaObject.connectSlotsByName(SearchWindow)
    # setupUi

    def retranslateUi(self, SearchWindow):
        SearchWindow.setWindowTitle(QCoreApplication.translate("SearchWindow", u"Form", None))
        self.searchButton.setText("")
    # retranslateUi

class SearchWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SearchWindow()
        self.ui.setupUi(self)
        self.event_name_list = [x.name for x in schedule.event_list]
        self.completer = QCompleter(schedule.event_name_list)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.ui.searchBar.setCompleter(self.completer)

    def connectSignals(self):
        self.ui.searchButton.clicked.connect(update_display)

    def showWindow(self):
        self.show()

    def update_display(self, text):

        for event in schedule.event_name_list:
            if text.lower() in event.name.lower():
                event.show()
            else:
                event.hide()



