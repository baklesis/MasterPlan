# This Python file uses the following encoding: utf-8
import sys
import os

from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader

from MainWindow import Ui_MainWindow
from gui_classes import *
from data_classes import *
from global_vars import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainView, self).__init__()
        self.load_ui()

    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "MainWindow.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()


if __name__ == "__main__":
    MasterPlan = QApplication()
    MainWindow = QMainWindow()
    Ui_MainWindow = Ui_MainWindow()
    Ui_MainWindow.setupUi(MainWindow)
    Ui_MainWindow.connectSignals()
    MainWindow.show()
    sys.exit(MasterPlan.exec_())
