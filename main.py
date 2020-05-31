# This Python file uses the following encoding: utf-8
import sys

from PySide2.QtWidgets import QApplication, QMainWindow, QDialog

from ui_classes.MainWindow import MainWindow
from ui_classes.EventCreateWindow import EventCreateWindow


if __name__ == "__main__":
    MasterPlan = QApplication()

    mainWindow = MainWindow()
    mainWindow.show()

## display EventCreateWindow
    eventCreateWindow = EventCreateWindow()
    eventCreateWindow.show()



    sys.exit(MasterPlan.exec_())


