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
        ConstraintWindow.resize(217, 299)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ConstraintWindow.sizePolicy().hasHeightForWidth())
        ConstraintWindow.setSizePolicy(sizePolicy)
        self.stackedWidget = QStackedWidget(ConstraintWindow)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 30, 181, 181))
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        self.stackedWidget.setFont(font)
        self.AddTimeConst = QWidget()
        self.AddTimeConst.setObjectName(u"AddTimeConst")
        self.FieldStartDate = QDateTimeEdit(self.AddTimeConst)
        self.FieldStartDate.setObjectName(u"FieldStartDate")
        self.FieldStartDate.setGeometry(QRect(30, 30, 121, 22))
        self.FieldStartDate.setDateTime(QDateTime(QDate(2020, 1, 1), QTime(0, 0, 0)))
        self.FieldStartDate.setMinimumDateTime(QDateTime(QDate(1819, 9, 14), QTime(0, 0, 0)))
        self.FieldStartDate.setCalendarPopup(True)
        self.FieldEndDate = QDateTimeEdit(self.AddTimeConst)
        self.FieldEndDate.setObjectName(u"FieldEndDate")
        self.FieldEndDate.setGeometry(QRect(30, 90, 121, 22))
        self.FieldEndDate.setAccelerated(False)
        self.FieldEndDate.setDateTime(QDateTime(QDate(2020, 1, 1), QTime(0, 0, 0)))
        self.FieldEndDate.setMinimumDateTime(QDateTime(QDate(1819, 9, 14), QTime(0, 0, 0)))
        self.FieldEndDate.setMaximumTime(QTime(23, 59, 59))
        self.FieldEndDate.setCalendarPopup(True)
        self.LabelStarts = QLabel(self.AddTimeConst)
        self.LabelStarts.setObjectName(u"LabelStarts")
        self.LabelStarts.setGeometry(QRect(30, 10, 61, 16))
        font1 = QFont()
        font1.setPointSize(10)
        self.LabelStarts.setFont(font1)
        self.LabelEnds = QLabel(self.AddTimeConst)
        self.LabelEnds.setObjectName(u"LabelEnds")
        self.LabelEnds.setGeometry(QRect(30, 70, 47, 13))
        self.LabelEnds.setFont(font1)
        self.LabelRepetition = QLabel(self.AddTimeConst)
        self.LabelRepetition.setObjectName(u"LabelRepetition")
        self.LabelRepetition.setGeometry(QRect(30, 130, 71, 16))
        self.LabelRepetition.setFont(font1)
        self.ComboRepetition = QComboBox(self.AddTimeConst)
        self.ComboRepetition.addItem("")
        self.ComboRepetition.addItem("")
        self.ComboRepetition.addItem("")
        self.ComboRepetition.addItem("")
        self.ComboRepetition.setObjectName(u"ComboRepetition")
        self.ComboRepetition.setGeometry(QRect(30, 150, 103, 26))
        self.ComboRepetition.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.stackedWidget.addWidget(self.AddTimeConst)
        self.AddTagConst = QWidget()
        self.AddTagConst.setObjectName(u"AddTagConst")
        self.LabelSelect = QLabel(self.AddTagConst)
        self.LabelSelect.setObjectName(u"LabelSelect")
        self.LabelSelect.setGeometry(QRect(20, 50, 61, 20))
        self.LabelSelect.setFont(font1)
        self.ComboTag = QComboBox(self.AddTagConst)
        self.ComboTag.setObjectName(u"ComboTag")
        self.ComboTag.setGeometry(QRect(20, 70, 104, 26))
        self.ComboTag.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.stackedWidget.addWidget(self.AddTagConst)
        self.LabelEvent = QLabel(ConstraintWindow)
        self.LabelEvent.setObjectName(u"LabelEvent")
        self.LabelEvent.setGeometry(QRect(10, 10, 41, 21))
        self.Add_btn = QPushButton(ConstraintWindow)
        self.Add_btn.setObjectName(u"Add_btn")
        self.Add_btn.setGeometry(QRect(40, 260, 61, 21))
        self.weightSlider = QSlider(ConstraintWindow)
        self.weightSlider.setObjectName(u"weightSlider")
        self.weightSlider.setGeometry(QRect(40, 230, 131, 21))
        self.weightSlider.setMaximum(2)
        self.weightSlider.setOrientation(Qt.Horizontal)
        self.weightSlider.setTickPosition(QSlider.TicksBothSides)
        self.LabelWeight = QLabel(ConstraintWindow)
        self.LabelWeight.setObjectName(u"LabelWeight")
        self.LabelWeight.setGeometry(QRect(40, 210, 71, 16))
        self.LabelWeight.setFont(font1)
        self.EventValue = QLabel(ConstraintWindow)
        self.EventValue.setObjectName(u"EventValue")
        self.EventValue.setGeometry(QRect(50, 40, 71, 20))

        self.retranslateUi(ConstraintWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ConstraintWindow)
    # setupUi

    def retranslateUi(self, ConstraintWindow):
        ConstraintWindow.setWindowTitle(QCoreApplication.translate("ConstraintWindow", u"New Constraint", None))
        self.LabelStarts.setText(QCoreApplication.translate("ConstraintWindow", u"Starts at:", None))
        self.LabelEnds.setText(QCoreApplication.translate("ConstraintWindow", u"Ends at:", None))
        self.LabelRepetition.setText(QCoreApplication.translate("ConstraintWindow", u"Repetition:", None))
        self.ComboRepetition.setItemText(0, QCoreApplication.translate("ConstraintWindow", u"None", None))
        self.ComboRepetition.setItemText(1, QCoreApplication.translate("ConstraintWindow", u"Daily", None))
        self.ComboRepetition.setItemText(2, QCoreApplication.translate("ConstraintWindow", u"Weekly", None))
        self.ComboRepetition.setItemText(3, QCoreApplication.translate("ConstraintWindow", u"Monthly", None))

        self.LabelSelect.setText(QCoreApplication.translate("ConstraintWindow", u"Select Tag:", None))
        self.LabelEvent.setText(QCoreApplication.translate("ConstraintWindow", u"Event: ", None))
        self.Add_btn.setText(QCoreApplication.translate("ConstraintWindow", u"Add", None))
        self.LabelWeight.setText(QCoreApplication.translate("ConstraintWindow", u"Set weight:", None))
        self.EventValue.setText("")
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
        for tag in reversed(range(self.ui.ComboTag.count())):
            self.ui.ComboTag.removeItem(tag)
        for tag in self.selected_event.tag_list:
            self.ui.ComboTag.addItem(tag.name)
        return self.exec()

    def saveTimeConstraint(self):
        start_date = self.ui.FieldStartDate.dateTime().toPython()
        end_date = self.ui.FieldEndDate.dateTime().toPython()
        if start_date > end_date:
            return None
        repetition = self.ui.ComboRepetition.currentText()
        weight = self.ui.weightSlider.sliderPosition()
        if weight == 0:
            weight = "low"
        elif weight == 1:
            weight = "medium"
        elif weight == 2:
            weight = "high"
        newconstraint = TimeConstraint(session.current_user, start_date, end_date, repetition, weight)
        self.selected_event.addConstraint(newconstraint)



    def saveTagConstraint(self):
        tag_name = self.ui.ComboTag.currentText()
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


