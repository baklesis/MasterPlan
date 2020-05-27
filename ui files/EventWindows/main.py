# This Python file uses the following encoding: utf-8
import sys
import os


from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader


class EventCreateWindow(QMainWindow):
    def __init__(self):
        super(EventCreateWindow, self).__init__()
        self.load_ui()

    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "EventCreateWindow.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()

def loadTestWindow(filename):
    loader = QUiLoader()
    path = os.path.join(os.path.dirname(__file__), filename)
    ui_file = QFile(path)
    ui_file.open(QFile.ReadOnly)
    window = loader.load(ui_file)
    return window

if __name__ == "__main__":
    app = QApplication([])
    widget = EventCreateWindow()
    eventCreate=loadTestWindow("EventCreateWindow.ui")
    eventEdit=loadTestWindow("EventEditWindow.ui")
    organizerList=loadTestWindow("OrganizerListWindow.ui")
    eventCreate.show()
    eventEdit.show()
    organizerList.show()
    sys.exit(app.exec_())
