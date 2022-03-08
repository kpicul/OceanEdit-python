import traceback
from PyQt6.QtWidgets import QMainWindow, QApplication, QPlainTextEdit
from PyQt6.QtGui import QAction
from PyQt6 import uic
from file_operations import read_file, write_file
from dialogs import open_file_dialog, show_error_dialog
from open_dialog_mode import OpenDialogMode
import sys


class MainWindow(QMainWindow):
    """Main window class.

    Attributes:
        main_area (QPlainTextEdit): Main text area.
        action_open (QAction): Action that activates open function

    """

    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("forms/mainWindow.ui", self)
        self.main_area: QPlainTextEdit = self.findChild(QPlainTextEdit, "mainArea")

        self.action_open: QAction = self.findChild(QAction, "actionOpen")
        self.action_save: QAction = self.findChild(QAction, "actionSave")

        self.set_events()
        self.show()

    def set_events(self):
        """Sets the main window events."""
        self.action_open.triggered.connect(self.open_file)
        self.action_save.triggered.connect(self.save_file)

    def open_file(self):
        """Opens file in main area."""
        try:
            file_path = open_file_dialog(self, "Select file", OpenDialogMode.OPEN, "")
            content: str = read_file(file_path)
            if content != "":
                self.main_area.setPlainText(content)
        except:
            show_error_dialog(traceback.format_exc())

    def save_file(self):
        """Opens save file dialog and saves file"""
        try:
            file_path = open_file_dialog(self, "Select file", OpenDialogMode.WRITE)
            if file_path != "":
                content: str = self.main_area.toPlainText()
                write_file(file_path, content)
        except:
            show_error_dialog(traceback.format_exc())


app = QApplication(sys.argv)
window = MainWindow()
app.exec()
