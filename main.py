# This Python file uses the following encoding: utf-8

import sys

from PySide2.QtWidgets import QApplication

from ui_classes.MainWindow import MainWindow

if __name__ == "__main__":
    MasterPlan = QApplication()

    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(MasterPlan.exec_())
