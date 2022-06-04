import traceback
from PyQt6.QtWidgets import QMainWindow, QTabWidget
from PyQt6.QtGui import QAction
from PyQt6 import uic
from file_operations import read_file, write_file, get_file_name
from dialogs import open_file_dialog, show_error_dialog, show_about_dialog
from open_dialog_mode import OpenDialogMode
from text_area import TextArea


class MainWindow(QMainWindow):
    """Main window class.

    Attributes:
        editor_tabs (QTabWidget): Tab widget that contains open editors.
        action_open (QAction): Action that activates open function.
        action_save (QAction): Action that saves file.
        action_copy (QAction): Action that activates copy function.
        action_paste (QAction): Action that activates paste function.
        action_cut (QAction): Action that activates cut function.
    """

    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("forms/mainWindow.ui", self)

        # Elements
        self.editor_tabs: QTabWidget = self.findChild(QTabWidget, "editorTabs")

        # Actions
        self.action_open: QAction = self.findChild(QAction, "actionOpen")
        self.action_save: QAction = self.findChild(QAction, "actionSave")
        self.action_copy: QAction = self.findChild(QAction, "actionCopy")
        self.action_paste: QAction = self.findChild(QAction, "actionPaste")
        self.action_cut: QAction = self.findChild(QAction, "actionCut")
        self.action_about: QAction = self.findChild(QAction, "actionAbout")

        self.set_events()
        self.show()

    def set_events(self):
        """Sets the main window events."""
        self.action_open.triggered.connect(self.open_file)
        self.action_save.triggered.connect(self.save_file)
        self.action_copy.triggered.connect(self.copy_operation)
        self.action_paste.triggered.connect(self.paste_operation)
        self.action_cut.triggered.connect(self.cut_operation)
        self.action_about.triggered.connect(show_about_dialog)

    def open_file(self):
        """Opens file in main area."""
        try:
            file_path = open_file_dialog(self, "Select file", OpenDialogMode.OPEN, "")
            if len(file_path) != 0:
                new_text_area = self.add_new_tab(get_file_name(file_path))
                new_text_area.set_content(file_path)
        except FileNotFoundError:
            show_error_dialog(traceback.format_exc())

    def save_file(self):
        """Opens save file dialog and saves file"""
        try:
            file_path = open_file_dialog(self, "Select file", OpenDialogMode.WRITE)
            if len(file_path) != 0:
                self.get_current_tab().save_content(True, file_path)
        except FileNotFoundError:
            show_error_dialog(traceback.format_exc())

    def add_new_tab(self, file_name: str = "new file") -> TextArea:
        """Adds new tab and sets it as selected.

        Args:
            file_name (str): File name. New file as default.

        Returns:
            TextArea: new editor.
        """
        new_text_area = TextArea()
        self.editor_tabs.addTab(new_text_area, file_name)
        self.editor_tabs.setCurrentWidget(new_text_area)

        return new_text_area

    def get_current_tab(self) -> TextArea:
        """Returns current editor.

        Returns:
            TextArea: current editor.
        """
        return self.editor_tabs.currentWidget()

    def copy_operation(self):
        if self.editor_tabs.count() > 0:
            self.get_current_tab().copy_operation()

    def paste_operation(self):
        if self.editor_tabs.count() > 0:
            self.get_current_tab().paste_operation()

    def cut_operation(self):
        self.get_current_tab().cut_operation()
