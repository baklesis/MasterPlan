# This Python file uses the following encoding: utf-8
import sys

from PySide2.QtWidgets import QApplication, QMainWindow

from gui_classes.MainWindow import Ui_MainWindow

if __name__ == "__main__":
    MasterPlan = QApplication()

    MainWindow = QMainWindow()

    ui_MainWindow = Ui_MainWindow()
    ui_MainWindow.setupUi(MainWindow)
    ui_MainWindow.connectSignals()


    MainWindow.show()

    sys.exit(MasterPlan.exec_())
