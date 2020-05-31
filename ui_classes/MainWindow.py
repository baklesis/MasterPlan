from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QLocale)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from ui_classes.MessageWindow import MessageWindow
from ui_classes.RangeWindow import RangeWindow
from ui_classes.EventInfoWindow import EventInfoWindow
from ui_classes.EventListWindow import EventListWindow
from ui_classes.SearchWindow import SearchWindow

from global_vars import *

# custom calendar class
class MyCalendarWidget(QCalendarWidget):
    def __init__(self, *args):
        QCalendarWidget.__init__(self, *args)
        self.color = QColor(self.palette().color(QPalette.Highlight))
        self.color.setAlpha(64)
        self.selectionChanged.connect(self.updateCells)
    def paintCell(self, painter, rect, date):
        QCalendarWidget.paintCell(self, painter, rect, date)
        if session.selected_building: # αν υπαρχει selected building
            event_list = MainWindow.filter(MainWindow,schedule.getSchedule(session.selected_building,None,None,None)) #παρε τις εκδηλώσεις του building
        else:
            event_list = MainWindow.filter(MainWindow,schedule.event_list) #παρε όλες τις εκδηλώσεις
        for event in event_list:
            if date == event["datetime"].date(): # αγνοει τις εκδηλώσεις που δεν εχουν διοργανωθεί (δεν εχουν datetime)
                painter.fillRect(rect, self.color)

# window ui class ######################################################################################################
class Ui_MainWindow(object):

# ui functions
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1366, 768)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1366, 768))
        MainWindow.setMaximumSize(QSize(1366, 768))
        icon = QIcon()
        icon.addFile(u"icons/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.CentralWidget = QWidget(MainWindow)
        self.CentralWidget.setObjectName(u"CentralWidget")
        self.StackedWidgetMain = QStackedWidget(self.CentralWidget)
        self.StackedWidgetMain.setObjectName(u"StackedWidgetMain")
        self.StackedWidgetMain.setGeometry(QRect(0, 0, 1366, 768))
        self.StackedWidgetMain.setAcceptDrops(False)
        self.StackedWidgetMain.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.StackedWidgetMain.setFrameShape(QFrame.NoFrame)
        self.HomePage = QWidget()
        self.HomePage.setObjectName(u"HomePage")
        self.horizontalLayoutWidget = QWidget(self.HomePage)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 170, 1371, 333))
        self.LayoutHomeHorizontal = QHBoxLayout(self.horizontalLayoutWidget)
        self.LayoutHomeHorizontal.setObjectName(u"LayoutHomeHorizontal")
        self.LayoutHomeHorizontal.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.LayoutHomeHorizontal.addItem(self.horizontalSpacer_3)
        self.LayoutHomeVertical = QVBoxLayout()
        self.LayoutHomeVertical.setObjectName(u"LayoutHomeVertical")
        self.LayoutLogo = QHBoxLayout()
        self.LayoutLogo.setObjectName(u"LayoutLogo")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.LayoutLogo.addItem(self.horizontalSpacer_7)
        self.LabelLogo = QLabel(self.horizontalLayoutWidget)
        self.LabelLogo.setObjectName(u"LabelLogo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.LabelLogo.sizePolicy().hasHeightForWidth())
        self.LabelLogo.setSizePolicy(sizePolicy1)
        self.LabelLogo.setMaximumSize(QSize(200, 200))
        self.LabelLogo.setPixmap(QPixmap(u"icons/logo.png"))
        self.LabelLogo.setScaledContents(True)
        self.LayoutLogo.addWidget(self.LabelLogo)
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.LayoutLogo.addItem(self.horizontalSpacer_8)
        self.LayoutHomeVertical.addLayout(self.LayoutLogo)
        self.LabelWelcome = QLabel(self.horizontalLayoutWidget)
        self.LabelWelcome.setObjectName(u"LabelWelcome")
        font = QFont()
        font.setFamily(u"Cambria")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.LabelWelcome.setFont(font)
        self.LabelWelcome.setLayoutDirection(Qt.LeftToRight)
        self.LabelWelcome.setFrameShape(QFrame.NoFrame)
        self.LabelWelcome.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.LayoutHomeVertical.addWidget(self.LabelWelcome)
        self.LayoutInput = QHBoxLayout()
        self.LayoutInput.setObjectName(u"LayoutInput")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.LayoutInput.addItem(self.horizontalSpacer_9)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout.addItem(self.verticalSpacer_2)
        self.LineOrg = QLineEdit(self.horizontalLayoutWidget)
        self.LineOrg.setObjectName(u"LineOrg")
        sizePolicy1.setHeightForWidth(self.LineOrg.sizePolicy().hasHeightForWidth())
        self.LineOrg.setSizePolicy(sizePolicy1)
        self.LineOrg.setMinimumSize(QSize(200, 25))
        self.verticalLayout.addWidget(self.LineOrg)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout.addItem(self.verticalSpacer)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(self.horizontalSpacer_16)
        self.ButtonGo = QPushButton(self.horizontalLayoutWidget)
        self.ButtonGo.setObjectName(u"ButtonGo")
        self.ButtonGo.setEnabled(True)
        self.ButtonGo.setCheckable(False)
        self.horizontalLayout.addWidget(self.ButtonGo)
        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(self.horizontalSpacer_18)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.LayoutInput.addLayout(self.verticalLayout)
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.LayoutInput.addItem(self.horizontalSpacer_10)
        self.LayoutHomeVertical.addLayout(self.LayoutInput)
        self.LayoutHomeHorizontal.addLayout(self.LayoutHomeVertical)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.LayoutHomeHorizontal.addItem(self.horizontalSpacer_4)
        self.StackedWidgetMain.addWidget(self.HomePage)
        self.ErrorPage = QWidget()
        self.ErrorPage.setObjectName(u"ErrorPage")
        self.LabelError = QLabel(self.ErrorPage)
        self.LabelError.setObjectName(u"LabelError")
        self.LabelError.setGeometry(QRect(450, 330, 481, 91))
        font1 = QFont()
        font1.setPointSize(20)
        self.LabelError.setFont(font1)
        self.ButtonGoBack = QPushButton(self.ErrorPage)
        self.ButtonGoBack.setObjectName(u"ButtonGoBack")
        self.ButtonGoBack.setGeometry(QRect(630, 410, 75, 23))
        self.ButtonGoBack.setCheckable(False)
        self.StackedWidgetMain.addWidget(self.ErrorPage)
        self.UserPage = QWidget()
        self.UserPage.setObjectName(u"UserPage")
        self.StackedWidgetUserTypes = QStackedWidget(self.UserPage)
        self.StackedWidgetUserTypes.setObjectName(u"StackedWidgetUserTypes")
        self.StackedWidgetUserTypes.setGeometry(QRect(150, 20, 231, 111))
        self.GuestPage = QWidget()
        self.GuestPage.setObjectName(u"GuestPage")
        self.verticalLayoutWidget_2 = QWidget(self.GuestPage)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 20, 201, 91))
        self.LayoutLogIn = QVBoxLayout(self.verticalLayoutWidget_2)
        self.LayoutLogIn.setObjectName(u"LayoutLogIn")
        self.LayoutLogIn.setSizeConstraint(QLayout.SetFixedSize)
        self.LayoutLogIn.setContentsMargins(0, 0, 0, 0)
        self.LineUser = QLineEdit(self.verticalLayoutWidget_2)
        self.LineUser.setObjectName(u"LineUser")
        self.LineUser.setInputMethodHints(Qt.ImhHiddenText)
        self.LayoutLogIn.addWidget(self.LineUser)
        self.LinePass = QLineEdit(self.verticalLayoutWidget_2)
        self.LinePass.setObjectName(u"LinePass")
        self.LinePass.setEchoMode(QLineEdit.Password)
        self.LayoutLogIn.addWidget(self.LinePass)
        self.LayoutButton = QHBoxLayout()
        self.LayoutButton.setObjectName(u"LayoutButton")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.LayoutButton.addItem(self.horizontalSpacer_11)
        self.ButtonLogIn = QPushButton(self.verticalLayoutWidget_2)
        self.ButtonLogIn.setObjectName(u"ButtonLogIn")
        self.ButtonLogIn.setCheckable(False)
        self.LayoutButton.addWidget(self.ButtonLogIn)
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.LayoutButton.addItem(self.horizontalSpacer_12)
        self.LayoutLogIn.addLayout(self.LayoutButton)
        self.StackedWidgetUserTypes.addWidget(self.GuestPage)
        self.LoggedUserPage = QWidget()
        self.LoggedUserPage.setObjectName(u"LoggedUserPage")
        self.verticalLayoutWidget = QWidget(self.LoggedUserPage)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 210, 54))
        self.LayoutLoggedIn = QVBoxLayout(self.verticalLayoutWidget)
        self.LayoutLoggedIn.setObjectName(u"LayoutLoggedIn")
        self.LayoutLoggedIn.setContentsMargins(0, 0, 0, 0)
        self.LayoutWelcomeUser = QHBoxLayout()
        self.LayoutWelcomeUser.setObjectName(u"LayoutWelcomeUser")
        self.LabelWelcomeUser = QLabel(self.verticalLayoutWidget)
        self.LabelWelcomeUser.setObjectName(u"LabelWelcomeUser")
        font2 = QFont()
        font2.setPointSize(12)
        self.LabelWelcomeUser.setFont(font2)
        self.LayoutWelcomeUser.addWidget(self.LabelWelcomeUser)
        self.LabelLoggedUser = QLabel(self.verticalLayoutWidget)
        self.LabelLoggedUser.setObjectName(u"LabelLoggedUser")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.LabelLoggedUser.sizePolicy().hasHeightForWidth())
        self.LabelLoggedUser.setSizePolicy(sizePolicy2)
        self.LabelLoggedUser.setFont(font2)
        self.LabelLoggedUser.setStyleSheet(u"color : rgb(5, 76, 181)")
        self.LayoutWelcomeUser.addWidget(self.LabelLoggedUser)
        self.LayoutLoggedIn.addLayout(self.LayoutWelcomeUser)
        self.LayoutLogOut = QHBoxLayout()
        self.LayoutLogOut.setObjectName(u"LayoutLogOut")
        self.ButtonLogOut = QPushButton(self.verticalLayoutWidget)
        self.ButtonLogOut.setObjectName(u"ButtonLogOut")
        self.ButtonLogOut.setMinimumSize(QSize(90, 0))
        self.ButtonLogOut.setMaximumSize(QSize(90, 16777215))
        self.ButtonLogOut.setCheckable(False)
        self.LayoutLogOut.addWidget(self.ButtonLogOut)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.LayoutLogOut.addItem(self.horizontalSpacer_2)
        self.LayoutLoggedIn.addLayout(self.LayoutLogOut)
        self.ButtonMessages = QToolButton(self.LoggedUserPage)
        self.ButtonMessages.setObjectName(u"ButtonMessages")
        self.ButtonMessages.setGeometry(QRect(0, 60, 41, 41))
        icon1 = QIcon()
        icon1.addFile(u"icons/message.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ButtonMessages.setIcon(icon1)
        self.ButtonMessages.setIconSize(QSize(30, 30))
        self.ButtonMessages.setCheckable(False)
        self.ButtonEdit = QToolButton(self.LoggedUserPage)
        self.ButtonEdit.setObjectName(u"ButtonEdit")
        self.ButtonEdit.setGeometry(QRect(50, 60, 41, 41))
        icon2 = QIcon()
        icon2.addFile(u"icons/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ButtonEdit.setIcon(icon2)
        self.ButtonEdit.setIconSize(QSize(30, 30))
        self.ButtonEdit.setCheckable(False)
        self.StackedWidgetUserTypes.addWidget(self.LoggedUserPage)
        self.LabelLogo_2 = QLabel(self.UserPage)
        self.LabelLogo_2.setObjectName(u"LabelLogo_2")
        self.LabelLogo_2.setGeometry(QRect(30, 20, 111, 111))
        sizePolicy1.setHeightForWidth(self.LabelLogo_2.sizePolicy().hasHeightForWidth())
        self.LabelLogo_2.setSizePolicy(sizePolicy1)
        self.LabelLogo_2.setMaximumSize(QSize(200, 200))
        self.LabelLogo_2.setPixmap(QPixmap(u"icons/logo.png"))
        self.LabelLogo_2.setScaledContents(True)
        self.formLayoutWidget = QWidget(self.UserPage)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(40, 134, 1281, 611))
        self.LayoutMainView = QGridLayout(self.formLayoutWidget)
        self.LayoutMainView.setObjectName(u"LayoutMainView")
        self.LayoutMainView.setContentsMargins(0, 0, 0, 0)
        self.LayoutSelectView = QHBoxLayout()
        self.LayoutSelectView.setObjectName(u"LayoutSelectView")
        self.LayoutSelectView.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.LayoutSelectView.addItem(self.horizontalSpacer_13)
        self.LayoutButtons = QHBoxLayout()
        self.LayoutButtons.setObjectName(u"LayoutButtons")
        self.LayoutButtons.setSizeConstraint(QLayout.SetFixedSize)
        self.ButtonGrid = QPushButton(self.formLayoutWidget)
        self.ButtonGrid.setObjectName(u"ButtonGrid")
        self.ButtonGrid.setCheckable(True)
        self.ButtonGrid.setChecked(False)
        self.ButtonGrid.setAutoExclusive(True)
        self.LayoutButtons.addWidget(self.ButtonGrid)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.LayoutButtons.addItem(self.horizontalSpacer)
        self.ButtonCalendar = QPushButton(self.formLayoutWidget)
        self.ButtonCalendar.setObjectName(u"ButtonCalendar")
        self.ButtonCalendar.setCheckable(True)
        self.ButtonCalendar.setAutoExclusive(True)
        self.LayoutButtons.addWidget(self.ButtonCalendar)
        self.LayoutSelectView.addLayout(self.LayoutButtons)
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.LayoutSelectView.addItem(self.horizontalSpacer_14)
        self.LayoutMainView.addLayout(self.LayoutSelectView, 3, 0, 1, 1)
        self.MainView = QStackedWidget(self.formLayoutWidget)
        self.MainView.setObjectName(u"MainView")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.MainView.sizePolicy().hasHeightForWidth())
        self.MainView.setSizePolicy(sizePolicy3)
        self.MainView.setMinimumSize(QSize(500, 500))
        self.MainView.setMaximumSize(QSize(2000, 500))
        self.MainView.setFrameShape(QFrame.NoFrame)
        self.GridView = QWidget()
        self.GridView.setObjectName(u"GridView")
        self.horizontalLayoutWidget_5 = QWidget(self.GridView)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(0, 456, 1281, 41))
        self.LayoutGridToolbar = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.LayoutGridToolbar.setObjectName(u"LayoutGridToolbar")
        self.LayoutGridToolbar.setContentsMargins(0, 0, 0, 0)
        self.ButtonBackToBuildings = QPushButton(self.horizontalLayoutWidget_5)
        self.ButtonBackToBuildings.setObjectName(u"ButtonBackToBuildings")
        self.ButtonBackToBuildings.setCheckable(False)
        self.ButtonBackToBuildings.setAutoRepeat(False)

        self.LayoutGridToolbar.addWidget(self.ButtonBackToBuildings)

        self.LabelFloor = QLabel(self.horizontalLayoutWidget_5)
        self.LabelFloor.setObjectName(u"LabelFloor")
        self.LabelFloor.setMinimumSize(QSize(0, 25))
        self.LabelFloor.setMaximumSize(QSize(16777215, 25))
        self.LabelFloor.setAlignment(Qt.AlignCenter)
        self.LayoutGridToolbar.addWidget(self.LabelFloor)
        self.SpinBoxFloor = QSpinBox(self.horizontalLayoutWidget_5)
        self.SpinBoxFloor.setObjectName(u"SpinBoxFloor")
        self.SpinBoxFloor.setMinimum(0)
        self.LayoutGridToolbar.addWidget(self.SpinBoxFloor)
        self.horizontalSpacer_15 = QSpacerItem(243, 18, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.LayoutGridToolbar.addItem(self.horizontalSpacer_15)
        self.ButtonGridRevert = QPushButton(self.horizontalLayoutWidget_5)
        self.ButtonGridRevert.setObjectName(u"ButtonGridRevert")
        self.ButtonGridRevert.setCheckable(False)
        self.ButtonGridRevert.setAutoRepeat(False)
        self.LayoutGridToolbar.addWidget(self.ButtonGridRevert)
        self.ButtonGridPublish = QPushButton(self.horizontalLayoutWidget_5)
        self.ButtonGridPublish.setObjectName(u"ButtonGridPublish")
        self.ButtonGridPublish.setCheckable(False)
        self.LayoutGridToolbar.addWidget(self.ButtonGridPublish)
        self.FrameGrid = QFrame(self.GridView)
        self.FrameGrid.setObjectName(u"FrameGrid")
        self.FrameGrid.setGeometry(QRect(0, 0, 1281, 451))
        self.FrameGrid.setFrameShape(QFrame.Box)
        self.FrameGrid.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget = QWidget(self.FrameGrid)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 1281, 451))
        self.Grid = QGridLayout(self.gridLayoutWidget)
        self.Grid.setSpacing(0)
        self.Grid.setObjectName(u"Grid")
        self.Grid.setContentsMargins(0, 0, 0, 0)
        self.MainView.addWidget(self.GridView)
        self.CalendarView = QWidget()
        self.CalendarView.setObjectName(u"CalendarView")
        self.horizontalLayoutWidget_6 = QWidget(self.CalendarView)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(0, 456, 1281, 41))
        self.LayoutCalToolbar = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.LayoutCalToolbar.setObjectName(u"LayoutCalToolbar")
        self.LayoutCalToolbar.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_17 = QSpacerItem(243, 18, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.LayoutCalToolbar.addItem(self.horizontalSpacer_17)
        self.ButtonCalPublish = QPushButton(self.horizontalLayoutWidget_6)
        self.ButtonCalPublish.setObjectName(u"ButtonCalPublish")
        self.ButtonCalPublish.setCheckable(False)
        self.ButtonCalPublish.setChecked(False)
        self.ButtonCalPublish.setAutoRepeat(False)
        self.LayoutCalToolbar.addWidget(self.ButtonCalPublish)
        self.ButtonCalRevert = QPushButton(self.horizontalLayoutWidget_6)
        self.ButtonCalRevert.setObjectName(u"ButtonCalRevert")
        self.ButtonCalRevert.setCheckable(False)
        self.LayoutCalToolbar.addWidget(self.ButtonCalRevert)
        self.ButtonDownload = QToolButton(self.horizontalLayoutWidget_6)
        self.ButtonDownload.setObjectName(u"ButtonDownload")
        sizePolicy1.setHeightForWidth(self.ButtonDownload.sizePolicy().hasHeightForWidth())
        self.ButtonDownload.setSizePolicy(sizePolicy1)
        icon3 = QIcon()
        icon3.addFile(u"icons/download.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ButtonDownload.setIcon(icon3)
        self.ButtonDownload.setIconSize(QSize(30, 30))
        self.ButtonDownload.setCheckable(True)
        self.LayoutCalToolbar.addWidget(self.ButtonDownload)
        self.FrameCalendar = QFrame(self.CalendarView)
        self.FrameCalendar.setObjectName(u"FrameCalendar")
        self.FrameCalendar.setGeometry(QRect(0, 0, 1281, 451))
        self.FrameCalendar.setFrameShape(QFrame.Box)
        self.FrameCalendar.setFrameShadow(QFrame.Raised)
        self.horizontalLayoutWidget_7 = QWidget(self.FrameCalendar)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(10, 10, 1261, 431))
        self.LayoutCalendar = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.LayoutCalendar.setObjectName(u"LayoutCalendar")
        self.LayoutCalendar.setContentsMargins(0, 0, 0, 0)
        self.Calendar = MyCalendarWidget(self.horizontalLayoutWidget_7)
        self.Calendar.setObjectName(u"Calendar")
        self.Calendar.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.Calendar.setMaximumDate(QDate(9999, 12, 30))
        self.Calendar.setGridVisible(False)
        self.Calendar.setSelectedDate(datetime.now())
        self.LayoutCalendar.addWidget(self.Calendar)
        self.LayoutEventList = QVBoxLayout()
        self.LayoutEventList.setObjectName(u"LayoutEventList")
        self.LabelSelectedDate = QLabel(self.horizontalLayoutWidget_7)
        self.LabelSelectedDate.setObjectName(u"LabelSelectedDate")
        font3 = QFont()
        font3.setFamily(u"Cambria")
        font3.setPointSize(26)
        self.LabelSelectedDate.setFont(font3)
        self.LabelSelectedDate.setStyleSheet(u"background : rgb(255, 255, 255)")
        self.LabelSelectedDate.setAlignment(Qt.AlignCenter)
        self.LayoutEventList.addWidget(self.LabelSelectedDate)
        self.ListWidgetEvents = QListWidget(self.horizontalLayoutWidget_7)
        self.ListWidgetEvents.setObjectName(u"ListWidgetEvents")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.ListWidgetEvents.sizePolicy().hasHeightForWidth())
        self.ListWidgetEvents.setSizePolicy(sizePolicy4)
        self.ListWidgetEvents.setMinimumSize(QSize(300, 0))
        self.ListWidgetEvents.setMaximumSize(QSize(300, 16777215))
        font4 = QFont()
        font4.setKerning(True)
        self.ListWidgetEvents.setFont(font4)
        self.ListWidgetEvents.setFrameShape(QFrame.NoFrame)
        self.ListWidgetEvents.setAlternatingRowColors(True)
        self.ListWidgetEvents.setLayoutMode(QListView.SinglePass)
        self.ListWidgetEvents.setSpacing(5)
        self.ListWidgetEvents.setViewMode(QListView.ListMode)
        self.ListWidgetEvents.setSelectionRectVisible(True)
        self.ListWidgetEvents.setSortingEnabled(True)
        self.LayoutEventList.addWidget(self.ListWidgetEvents)
        self.LayoutCalendar.addLayout(self.LayoutEventList)
        self.MainView.addWidget(self.CalendarView)
        self.LayoutMainView.addWidget(self.MainView, 2, 0, 1, 1)
        self.LayoutToolbar = QHBoxLayout()
        self.LayoutToolbar.setObjectName(u"LayoutToolbar")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.LayoutToolbar.addItem(self.horizontalSpacer_5)
        self.LayoutComboBoxVertical = QVBoxLayout()
        self.LayoutComboBoxVertical.setObjectName(u"LayoutComboBoxVertical")
        self.ComboBoxBuildings = QComboBox(self.formLayoutWidget)
        self.ComboBoxBuildings.addItem("")
        self.ComboBoxBuildings.setObjectName(u"ComboBoxBuildings")
        font5 = QFont()
        font5.setPointSize(11)
        font5.setItalic(False)
        font5.setStrikeOut(False)
        self.ComboBoxBuildings.setFont(font5)
        self.ComboBoxBuildings.setFrame(True)
        self.LayoutComboBoxVertical.addWidget(self.ComboBoxBuildings)
        self.ComboBoxFilters = QComboBox(self.formLayoutWidget)
        self.ComboBoxFilters.addItem("")
        self.ComboBoxFilters.setObjectName(u"ComboBoxFilters")
        self.ComboBoxFilters.setFrame(True)
        self.LayoutComboBoxVertical.addWidget(self.ComboBoxFilters)
        self.LayoutToolbar.addLayout(self.LayoutComboBoxVertical)
        self.horizontalSpacer_6 = QSpacerItem(500, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.LayoutToolbar.addItem(self.horizontalSpacer_6)
        self.ButtonSearch = QToolButton(self.formLayoutWidget)
        self.ButtonSearch.setObjectName(u"ButtonSearch")
        icon4 = QIcon()
        icon4.addFile(u"icons/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ButtonSearch.setIcon(icon4)
        self.ButtonSearch.setIconSize(QSize(30, 30))
        self.ButtonSearch.setCheckable(False)
        self.LayoutToolbar.addWidget(self.ButtonSearch)
        self.LayoutMainView.addLayout(self.LayoutToolbar, 1, 0, 1, 1)
        self.StackedWidgetMain.addWidget(self.UserPage)
        MainWindow.setCentralWidget(self.CentralWidget)
        self.retranslateUi(MainWindow)
        self.StackedWidgetMain.setCurrentIndex(0)
        self.StackedWidgetUserTypes.setCurrentIndex(0)
        self.MainView.setCurrentIndex(0)
        self.ButtonGridPublish.hide()
        self.ButtonGridRevert.hide()
        self.ButtonCalPublish.hide()
        self.ButtonCalRevert.hide()
        QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MasterPlan", None))
        self.LabelLogo.setText("")
        self.LabelWelcome.setText(QCoreApplication.translate("MainWindow", u"MasterPlan", None))
        self.LineOrg.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter organization", None))
        self.ButtonGo.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.LabelError.setText(QCoreApplication.translate("MainWindow", u"Sorry, there is no such organization. :(", None))
        self.ButtonGoBack.setText(QCoreApplication.translate("MainWindow", u"Go back", None))
        self.LineUser.setPlaceholderText(QCoreApplication.translate("MainWindow", u"username", None))
        self.LinePass.setPlaceholderText(QCoreApplication.translate("MainWindow", u"password", None))
        self.ButtonLogIn.setText(QCoreApplication.translate("MainWindow", u"Log in", None))
        self.LabelWelcomeUser.setText(QCoreApplication.translate("MainWindow", u"Welcome,", None))
        self.LabelLoggedUser.setText(QCoreApplication.translate("MainWindow", u"<user name>", None))
        self.ButtonLogOut.setText(QCoreApplication.translate("MainWindow", u"Log out", None))
        self.ButtonMessages.setText(QCoreApplication.translate("MainWindow", u"Messages", None))
        self.ButtonEdit.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.LabelLogo_2.setText("")
        self.ButtonGrid.setText(QCoreApplication.translate("MainWindow", u"Grid View", None))
        self.ButtonCalendar.setText(QCoreApplication.translate("MainWindow", u"Calendar View", None))
        self.ButtonBackToBuildings.setText(QCoreApplication.translate("MainWindow", u"Back To Buildings", None))
        self.LabelFloor.setText(QCoreApplication.translate("MainWindow", u"Floor", None))
        self.ButtonGridRevert.setText(QCoreApplication.translate("MainWindow", u"Revert Changes", None))
        self.ButtonGridPublish.setText(QCoreApplication.translate("MainWindow", u"Publish Changes", None))
        self.ButtonCalPublish.setText(QCoreApplication.translate("MainWindow", u"Publish Changes", None))
        self.ButtonCalRevert.setText(QCoreApplication.translate("MainWindow", u"Revert Changes", None))
        self.ButtonDownload.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.LabelSelectedDate.setText(QCoreApplication.translate("MainWindow", datetime.now().strftime("%b %d %Y"), None))
        self.ComboBoxBuildings.setItemText(0, QCoreApplication.translate("MainWindow", u"No Building Selected", None))
        self.ComboBoxFilters.setItemText(0, QCoreApplication.translate("MainWindow", u"No Filter Selected", None))
        self.ButtonSearch.setText(QCoreApplication.translate("MainWindow", u"Search", None))

# window class #########################################################################################################
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connectSignals()

    def connectSignals(self):
        self.ui.ButtonGo.clicked.connect(self.enterOrganization)
        self.ui.ButtonGoBack.clicked.connect(self.showHomePage)
        self.ui.ButtonLogIn.clicked.connect(self.logIn)
        self.ui.ButtonLogOut.clicked.connect(self.logOut)
        self.ui.ButtonEdit.clicked.connect(self.selectEventList)
        self.ui.ButtonSearch.clicked.connect(self.selectSearch)
        self.ui.ButtonGrid.clicked.connect(self.showGrid)
        self.ui.ButtonCalendar.clicked.connect(self.showCalendar)
        self.ui.ComboBoxFilters.currentIndexChanged.connect(self.selectFilter)
        self.ui.ComboBoxBuildings.currentIndexChanged.connect(self.updateSelectedBuilding)
        self.ui.Calendar.clicked.connect(self.fillCalEventList)
        self.ui.ButtonDownload.clicked.connect(self.download)
        self.ui.ListWidgetEvents.itemActivated.connect(self.selectEvent)
        self.ui.ButtonBackToBuildings.clicked.connect(self.showBuildings)
        self.ui.SpinBoxFloor.valueChanged.connect(self.changeFloor)

    # domain functions

    def showHomePage(self):
        self.ui.StackedWidgetMain.setCurrentIndex(0)

    def showErrorPage(self):
        self.ui.StackedWidgetMain.setCurrentIndex(1)

    def showUserPage(self):
        self.ui.StackedWidgetMain.setCurrentIndex(2)

    def showGuestPage(self):
        self.ui.StackedWidgetUserTypes.setCurrentIndex(0)
        self.loadFilterMenu()
        self.loadBuildingMenu()
        self.ui.ButtonGrid.click()
        self.showGrid()

    def showLoggedUserPage(self):
        self.ui.StackedWidgetUserTypes.setCurrentIndex(1)
        self.loadFilterMenu()
        self.loadBuildingMenu()
        self.ui.ButtonGrid.click()
        self.showGrid()

    def showGrid(self):
        self.ui.MainView.setCurrentIndex(0)
        selected_building = session.selected_building
        if selected_building:
            self.showRooms(selected_building,session.selected_floor)
        else:
            self.showBuildings()
        self.fillEvents()

    def showBuildings(self):
        self.ui.ButtonBackToBuildings.hide()
        self.ui.LabelFloor.hide()
        self.ui.SpinBoxFloor.hide()
        self.ui.ComboBoxBuildings.setCurrentIndex(0)
        self.grid_button_list = []
        # delete previous buttons
        for i in reversed(range(self.ui.Grid.count())):
            self.ui.Grid.takeAt(i).widget().deleteLater()
        #load buildings buttons
        for i, building in enumerate(building_list.building_list):
            building_button = QPushButton(self.ui.gridLayoutWidget)
            building_button.setObjectName(u"pushButton")
            sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            sizePolicy.setHeightForWidth(building_button.sizePolicy().hasHeightForWidth())
            building_button.setSizePolicy(sizePolicy)
            building_button.setMinimumSize(QSize(100, 100))
            building_button.setMaximumSize(QSize(100, 100))
            building_button.setText(QCoreApplication.translate("MainWindow", building.name, None))
            self.grid_button_list.append(building_button)
            self.ui.Grid.addWidget(self.grid_button_list[i], 0, i)
            self.grid_button_list[i].clicked.connect(self.selectBuilding)

    def selectBuilding(self):
        selected_building = self.sender().text()
        for i,building in enumerate(building_list.building_list):
            if building.name == selected_building:
                self.ui.ComboBoxBuildings.setCurrentIndex(i+1) #ορισε την επιλογή στο buildings combo box (connected with updateSelectedBuilding)
                break

    def showRooms(self,building,floor):
        self.ui.ButtonBackToBuildings.show()
        self.ui.LabelFloor.show()

        #load floor spin box
        self.ui.SpinBoxFloor.show()
        max_floor = 0
        for room in session.selected_building.room_list:
            if room.floor > max_floor:
                max_floor = room.floor
        self.ui.SpinBoxFloor.setMaximum(max_floor)

        # delete previous buttons
        self.grid_button_list = []
        for i in reversed(range(self.ui.Grid.count())):
            self.ui.Grid.takeAt(i).widget().deleteLater()

        #load room buttons
        i = 0
        for room in building.room_list:
            if room.floor == floor:
                room_button = QPushButton(self.ui.gridLayoutWidget)
                room_button.setObjectName(u"pushButton")
                sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                sizePolicy.setHeightForWidth(room_button.sizePolicy().hasHeightForWidth())
                room_button.setSizePolicy(sizePolicy)
                room_button.setMinimumSize(QSize(100, 100))
                room_button.setMaximumSize(QSize(100, 100))
                room_button.setText(QCoreApplication.translate("MainWindow", room.name, None))
                self.grid_button_list.append(room_button)
                self.ui.Grid.addWidget(self.grid_button_list[i], 0, i)
                self.grid_button_list[i].clicked.connect(self.selectRoom)
                i+=1

    def selectRoom(self):
        selected_room = self.sender().text()
        for room in room_list.room_list:
            if room.name == selected_room:
                for event in schedule.event_list:
                    if (event['datetime'] == datetime.now()) & (event['room'] == selected_room):
                        self.eventInfoWindow = EventInfoWindow()
                        self.eventInfoWindow.ui.LabelEventName.setText(event['object'].name)
                        self.eventInfoWindow.ui.LabelRoomValue.setText(event['room'].name)
                        self.eventInfoWindow.ui.LabelTimeValue.setText(event['datetime'].strftime("%x %X"))
                        self.eventInfoWindow.ui.LabelDurationValue.setText(str(event['object'].duration))
                        self.eventInfoWindow.ui.LabelOrganizerValue.setText(event['object'].organizer.fullname)
                        self.eventInfoWindow.showWindow()
                        break
                break

    def showCalendar(self):
        self.ui.MainView.setCurrentIndex(1)
        self.fillEvents()

    def enterOrganization(self):
        global session
        org = self.ui.LineOrg.text()
        if account_list.valOrganization(org):
            session = Session(None, org)
            self.showUserPage()
            self.showGuestPage()
        else:
            self.showErrorPage()

    def logIn(self):
        global session
        username = self.ui.LineUser.text()
        password = self.ui.LinePass.text()
        account = account_list.accountExists(username, password)
        if account:
            session = Session(account, session.current_org)
            self.showLoggedUserPage()
            self.ui.LabelLoggedUser.setText(account.username)
        else:
            #show Error MessageWindow
            self.messageWindow = MessageWindow()
            self.messageWindow.showLogInError()
            self.messageWindow.showWindow()
            self.ui.LineUser.clear()
            self.ui.LinePass.clear()

    def logOut(self):
        global session
        session = Session(None,session.current_org)
        self.ui.LineUser.setText(None)
        self.ui.LinePass.setText(None)
        self.showGuestPage()

    def selectEventList(self):
        self.eventListWindow = EventListWindow()
        self.eventListWindow.showWindow()
        if session.getUserType() == "Admin":
            self.eventListWindow.ui.ExtraButtons.setCurrentIndex(0)
            self.eventListWindow.ui.stackedWidget_2.setCurrentIndex(1)
        else:
            self.eventListWindow.ui.ExtraButtons.setCurrentIndex(1)
            self.eventListWindow.ui.stackedWidget_2.setCurrentIndex(0)

    def selectSearch(self):
        self.searchWindow = SearchWindow()
        self.searchWindow.showWindow()


    def loadFilterMenu(self):  # φορτώνεται στο showLoggedUserPage kαι showGuestPage
        self.ui.ComboBoxFilters.clear()
        self.ui.ComboBoxFilters.addItem("No Filter Selected")
        for tag in tag_list.tag_list:
            self.ui.ComboBoxFilters.addItem(tag.name)
            if session.selected_filters: #και αν υπάρχει selected filter απο το session
                if session.selected_filters[0].name == tag.name:
                    self.ui.ComboBoxFilters.setCurrentIndex(i+1) # επελεξε το στο combobox (0 = no filter selected)
            else: # αλλιως επελεξε no filter selected
                self.ui.ComboBoxFilters.setCurrentIndex(0)

    def loadBuildingMenu(self):  # φορτώνεται στο showLoggedUserPage kαι showGuestPage
        self.ui.ComboBoxBuildings.clear()
        self.ui.ComboBoxBuildings.addItem("No Building Selected")
        for i,building in enumerate(building_list.building_list): #για καθε building στο building list
            self.ui.ComboBoxBuildings.addItem(building.name) #προσθεσε στοιχειο στο combo box
            if session.selected_building: #και αν υπάρχει selected building απο το session
                if session.selected_building.name == building.name:
                    self.ui.ComboBoxBuildings.setCurrentIndex(i+1) # επελεξε το στο combobox (0 = no building selected)
            else: # αλλιως επελεξε no building selected
                self.ui.ComboBoxBuildings.setCurrentIndex(0)

    def selectFilter(self):
        selected_filter = self.ui.ComboBoxFilters.currentText()
        session.selected_filters.clear() # κανουμε clear την λίστα γιατι λόγω UI limitations θεωρούμε ότι μπορεί να εφαρμοστεί μόνο ενα φιλτρο
        if selected_filter != "No Filter Selected":
            for tag in tag_list.tag_list: #βρες τo tag object
                if selected_filter == tag.name:
                    session.selected_filters.append(tag)
                    break
        self.fillEvents() # με το fillEvents ξανακαλείται η paintCells του Calendar η οποία καλεί την filter() που επιστρέφει τις εκδηλώσεις τις οποίες θα κάνει paint στο Calendar

    def updateSelectedBuilding(self):
        selected_building = self.ui.ComboBoxBuildings.currentText()
        session.selected_building = None
        if selected_building != "No Building Selected":
            for building in building_list.building_list:
                if selected_building == building.name:
                    session.selected_building = building
                    session.selected_floor = 0
                    self.showRooms(session.selected_building,session.selected_floor)
                    break
        else:
            self.showBuildings()

        self.fillEvents()  # με το fillEvents ξανακαλείται η paintCells του Calendar η οποία καλεί την filter() που επιστρέφει τις εκδηλώσεις τις οποίες θα κάνει paint στο Calendar

    def filter(self,event_list):
        filtered_event_list = []
        if event_list: # αν υπαρχουν εκδηλωσεις
            if session.selected_filters: # αν υπαρχουν επιλεγμενα filters
                for event in event_list:
                        for tag in event["object"].tag_list:
                            if session.selected_filters[0].name == tag.name:  # και καποιο tag του event περιέχεται στα επιλεγμένα filters (λογω ui limitations μπορει να επιλέξει μόνο ένα filter)
                                filtered_event_list.append(event)  # περιέλαβε το στα αποτελέσματα
                                break
            else: # αν δεν υπαρχουν επιλεγμενα filters
                    for event in event_list:
                            filtered_event_list.append(event)
        return filtered_event_list


    def fillEvents(self): #κανει update τα views
        # update grid view
        # update calendar view
        self.ui.Calendar.updateCells() #ξανακαλει την paintCells του Calendar
        self.fillCalEventList()  # refresh την λιστα με τις εκδηλωσεις

    def fillCalEventList(self): # για την λίστα που εμφανίζεται με το πατημα ενός κελιού στο Calendar
        # reset την λίστα
        self.ui.ListWidgetEvents.clear()
        # εκτύπωσε events της selected date στην λίστα
        selected_date = self.ui.Calendar.selectedDate()
        self.ui.LabelSelectedDate.setText(datetime.strptime(selected_date.toString("ddMMyy"), "%d%m%y").strftime("%b %d %Y"))  # μετατροπη σε string -> datetime -> string γιατι το PySide εβγαζε το format στα ελληνικα
        filtered_event_list = []
        if session.selected_building:  # αν υπαρχει selected building
            filtered_event_list = self.filter(schedule.getSchedule(session.selected_building,None,None,None))
        else:
            filtered_event_list = self.filter(schedule.event_list)
        for event in filtered_event_list:
            if selected_date == event["datetime"].date():
                self.ui.ListWidgetEvents.addItem(event["object"].name)

    def download(self):
        self.rangeWindow = RangeWindow()
        self.rangeWindow.showWindow()

    def selectEvent(self):
        selected_event_name = self.ui.ListWidgetEvents.selectedItems()[0].text()
        selected_event = self.getEventInfo(selected_event_name)
        if selected_event:
            self.eventInfoWindow = EventInfoWindow()
            self.eventInfoWindow.ui.LabelEventName.setText(selected_event['object'].name)
            self.eventInfoWindow.ui.LabelRoomValue.setText(selected_event['room'].name)
            self.eventInfoWindow.ui.LabelTimeValue.setText(selected_event['datetime'].strftime("%x %X"))
            self.eventInfoWindow.ui.LabelDurationValue.setText(str(selected_event['object'].duration))
            self.eventInfoWindow.ui.LabelOrganizerValue.setText(selected_event['object'].organizer.fullname)
            self.eventInfoWindow.showWindow()

    def getEventInfo(self,event_name):
        for event in schedule.event_list:
            if event_name == event['object'].name:
                return event

    def changeFloor(self):
         selected_floor = self.ui.SpinBoxFloor.value()
         session.selected_floor = selected_floor
         self.showRooms(session.selected_building,session.selected_floor)















