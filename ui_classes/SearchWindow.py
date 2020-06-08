from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from global_vars import *
from ui_classes.EventInfoWindow import EventInfoWindow


class Ui_SearchWindow(object):
    def setupUi(self, SearchWindow):
        if not SearchWindow.objectName():
            SearchWindow.setObjectName(u"SearchWindow")
        SearchWindow.resize(320, 320)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(60)
        sizePolicy.setVerticalStretch(60)
        sizePolicy.setHeightForWidth(SearchWindow.sizePolicy().hasHeightForWidth())
        SearchWindow.setSizePolicy(sizePolicy)
        SearchWindow.setMinimumSize(QSize(320, 320))
        SearchWindow.setMaximumSize(QSize(320, 320))
        self.searchBar = QLineEdit(SearchWindow)
        self.searchBar.setObjectName(u"searchBar")
        self.searchBar.setGeometry(QRect(80, 30, 151, 21))
        self.searchBar.setMaximumSize(QSize(16777215, 100))
        self.searchButton = QPushButton(SearchWindow)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setGeometry(QRect(230, 29, 32, 22))
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.searchButton.sizePolicy().hasHeightForWidth())
        self.searchButton.setSizePolicy(sizePolicy1)
        icon = QIcon()
        icon.addFile(u"icons/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchButton.setIcon(icon)
        self.searchButton.setCheckable(False)
        self.searchResults = QListWidget(SearchWindow)
        self.searchResults.setObjectName(u"searchResults")
        self.searchResults.setGeometry(QRect(80, 50, 181, 191))

        self.retranslateUi(SearchWindow)

        self.searchButton.setDefault(True)


        QMetaObject.connectSlotsByName(SearchWindow)
    # setupUi

    def retranslateUi(self, SearchWindow):
        SearchWindow.setWindowTitle(QCoreApplication.translate("SearchWindow", u"Search", None))
        self.searchButton.setText("")
    # retranslateUi

class SearchWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SearchWindow()
        self.ui.setupUi(self)
        self.connectSignals()
        self.event_name_list = []
        for event in schedule.event_list:
            self.event_name_list.append(event["object"].name)
        self.completer = QCompleter(self.event_name_list)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.ui.searchBar.setCompleter(self.completer)

    def connectSignals(self):
        self.ui.searchButton.clicked.connect(self.update_display)
        self.ui.searchResults.itemDoubleClicked.connect(self.display_event)


    def updateDisplay(self):
        text = self.ui.searchBar.text()
        for event in reversed(range(self.ui.searchResults.count())):
            self.ui.searchResults.takeItem(event)
        for event in self.event_name_list:
            if text.lower() in event.lower():
                self.ui.searchResults.addItem(event)
        self.ui.searchButton.clicked.connect(self.update_display)
        self.ui.searchResults.itemDoubleClicked.connect(self.display_event)

    def showWindow(self):
        self.show()

    def update_display(self):
        print("click!")
        text = self.ui.searchBar.text()
        for event in reversed(range(self.ui.searchResults.count())):
            self.ui.searchResults.takeItem(event)
        for event in self.event_name_list:
            if text.lower() in event.lower():
                self.ui.searchResults.addItem(event)

    def display_event(self):
        event = schedule.getEvent(self.ui.searchResults.currentItem().text())
        self.eventInfoWindow = EventInfoWindow()
        self.eventInfoWindow.showWindow(event)