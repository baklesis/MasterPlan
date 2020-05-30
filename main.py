# This Python file uses the following encoding: utf-8
import sys

from PySide2.QtWidgets import QApplication, QMainWindow, QDialog

from MainWindow import Ui_MainWindow
from MessageWindow import Ui_MessageWindow

if __name__ == "__main__":
    MasterPlan = QApplication()

    MainWindow = QMainWindow()
    MessageWindow = QDialog()

    Ui_MainWindow = Ui_MainWindow()
    Ui_MainWindow.setupUi(MainWindow)
    Ui_MainWindow.connectSignals()

    Ui_MessageWindow = Ui_MessageWindow()
    Ui_MessageWindow.setupUi(MessageWindow)

    MainWindow.show()
    #MessageWindow.show()

    sys.exit(MasterPlan.exec_())
