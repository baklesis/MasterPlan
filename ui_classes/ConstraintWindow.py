from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from global_vars import *
from data_classes.constraint import *
class Ui_ConstraintWindow(object):
    def setupUi(self, ConstraintWindow):
        if not ConstraintWindow.objectName():
            ConstraintWindow.setObjectName(u"ConstraintWindow")
        ConstraintWindow.resize(225, 362)
        self.stackedWidget = QStackedWidget(ConstraintWindow)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 60, 181, 191))
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        self.stackedWidget.setFont(font)
        self.AddTimeConst = QWidget()
        self.AddTimeConst.setObjectName(u"AddTimeConst")
        self.dateTimeEdit = QDateTimeEdit(self.AddTimeConst)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setGeometry(QRect(30, 30, 121, 22))
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit_2 = QDateTimeEdit(self.AddTimeConst)
        self.dateTimeEdit_2.setObjectName(u"dateTimeEdit_2")
        self.dateTimeEdit_2.setGeometry(QRect(30, 90, 121, 22))
        self.dateTimeEdit_2.setCalendarPopup(True)
        self.label_3 = QLabel(self.AddTimeConst)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 10, 61, 16))
        font1 = QFont()
        font1.setPointSize(10)
        self.label_3.setFont(font1)
        self.label_4 = QLabel(self.AddTimeConst)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 70, 47, 13))
        self.label_4.setFont(font1)
        self.label_5 = QLabel(self.AddTimeConst)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 130, 71, 16))
        self.label_5.setFont(font1)
        self.comboBox = QComboBox(self.AddTimeConst)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(30, 150, 69, 22))
        self.stackedWidget.addWidget(self.AddTimeConst)
        self.AddTagConst = QWidget()
        self.AddTagConst.setObjectName(u"AddTagConst")
        self.label_7 = QLabel(self.AddTagConst)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 50, 61, 20))
        self.label_7.setFont(font1)
        self.label_8 = QLabel(self.AddTagConst)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(250, 70, 71, 21))
        self.label_8.setFont(font1)
        self.comboBox_2 = QComboBox(self.AddTagConst)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(20, 70, 69, 22))
        self.stackedWidget.addWidget(self.AddTagConst)
        self.label = QLabel(ConstraintWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 151, 21))
        font2 = QFont()
        font2.setPointSize(13)
        font2.setBold(True)
        font2.setWeight(75)
        self.label.setFont(font2)
        self.label_2 = QLabel(ConstraintWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 40, 41, 21))
        self.Add_btn = QPushButton(ConstraintWindow)
        self.Add_btn.setObjectName(u"Add_btn")
        self.Add_btn.setGeometry(QRect(30, 330, 61, 21))
        self.weightSlider = QSlider(ConstraintWindow)
        self.weightSlider.setObjectName(u"weightSlider")
        self.weightSlider.setGeometry(QRect(30, 270, 131, 21))
        self.weightSlider.setMaximum(2)
        self.weightSlider.setOrientation(Qt.Horizontal)
        self.weightSlider.setTickPosition(QSlider.TicksBothSides)
        self.label_6 = QLabel(ConstraintWindow)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 250, 71, 16))
        self.label_6.setFont(font1)
        self.EventValue = QLabel(ConstraintWindow)
        self.EventValue.setObjectName(u"EventValue")
        self.EventValue.setGeometry(QRect(50, 40, 71, 20))

        self.retranslateUi(ConstraintWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ConstraintWindow)
    # setupUi

    def retranslateUi(self, ConstraintWindow):
        ConstraintWindow.setWindowTitle(QCoreApplication.translate("ConstraintWindow", u"Dialog", None))
        self.label_3.setText(QCoreApplication.translate("ConstraintWindow", u"Starts at:", None))
        self.label_4.setText(QCoreApplication.translate("ConstraintWindow", u"Ends at:", None))
        self.label_5.setText(QCoreApplication.translate("ConstraintWindow", u"Repetition:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("ConstraintWindow", u"None", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("ConstraintWindow", u"Daily", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("ConstraintWindow", u"Weekly", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("ConstraintWindow", u"Monthly", None))

        self.label_7.setText(QCoreApplication.translate("ConstraintWindow", u"Add Tag:", None))
        self.label_8.setText(QCoreApplication.translate("ConstraintWindow", u"Set Weight:", None))
        self.label.setText(QCoreApplication.translate("ConstraintWindow", u"Add Constraint", None))
        self.label_2.setText(QCoreApplication.translate("ConstraintWindow", u"Event: ", None))
        self.Add_btn.setText(QCoreApplication.translate("ConstraintWindow", u"Add", None))
        self.label_6.setText(QCoreApplication.translate("ConstraintWindow", u"Set weight:", None))
        self.EventValue.setText(QCoreApplication.translate("ConstraintWindow", u"Event Name", None))
    # retranslateUi

class ConstraintWindow(QDialog):
    def __init__(self, selected_event):
        super().__init__()
        self.ui = Ui_ConstraintWindow()
        self.ui.setupUi(self)
        self.selected_event = selected_event["object"]
        self.connectSignals()

    def connectSignals(self):
        self.ui.Add_btn.clicked.connect(self.accept)

    def showWindow(self):
        for tag in reversed(range(self.ui.comboBox_2.count())):
            self.ui.comboBox_2.removeItem(tag)
        for tag in self.selected_event.tag_list:
            self.ui.comboBox_2.addItem(tag.name)
        return self.exec()

    def saveTimeConstraint(self):
        start_date = self.ui.dateTimeEdit.dateTime()
        end_date = self.ui.dateTimeEdit_2.dateTime()
        repetition = self.ui.comboBox.currentText()
        weight=self.ui.weightSlider.sliderPosition()
        if weight == 0:
            weight = "low"
        elif weight == 1:
            weight = "medium"
        elif weight == 2:
            weight = "high"
        newconstraint = TimeConstraint(session.current_user, start_date, end_date, repetition,weight)
        self.selected_event.addConstraint(newconstraint)



    def saveTagConstraint(self):
        tag_name = self.ui.comboBox_2.currentText()
        weight = self.ui.weightSlider.sliderPosition()
        if weight == 0:
            weight = "low"
        elif weight == 1:
            weight = "medium"
        elif weight == 2:
            weight = "high"


        self.selected_event.addConstraint(TagConstraint(session.current_user,tag_list.getTag(tag_name),weight))

    def saveConstraint(self):
        page=self.ui.stackedWidget.currentIndex()
        if page==0:
            self.saveTimeConstraint()
        else:
             self.saveTagConstraint()


