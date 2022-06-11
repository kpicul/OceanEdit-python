from PyQt6.QtWidgets import QWidget, QPlainTextEdit
from PyQt6 import uic
from file_operations import read_file, write_file


class TextArea(QWidget):
    """Text area which contains the text.

    Attributes
        editor_area (QPlainTextEdit): Area that contains the text.
        file_path (str): Path of the file or empty string if file is not yet saved.
    """

    def __init__(self):
        super(TextArea, self).__init__()
        uic.loadUi("forms/textArea.ui", self)

        # Setting the properties.
        self.editor_area: QPlainTextEdit = self.findChild(QPlainTextEdit, "editorArea")
        self.file_path: str = ""

    def set_content(self, file_path: str):
        """Sets the area content.

        Args:
            file_path (str): path of the file which contains the content..
        """
        self.file_path = file_path
        content: str = read_file(file_path)
        self.editor_area.setPlainText(content)

    def save_content(self, save_as: bool = False, file_path: str = ""):
        """Saves the content of the file and if it is a new file sets the file path.

        Args:
            save_as (bool): if it is a save as operation. False by default.
            file_path (str): path of the file.
        """
        if save_as:
            self.file_path = file_path
        content: str = self.editor_area.toPlainText()
        write_file(self.file_path, content)

    def copy_operation(self):
        """Performs copy operation."""
        self.editor_area.copy()

    def paste_operation(self):
        """Performs paste operation."""
        self.editor_area.paste()

    def cut_operation(self):
        """Performs cut operation."""
        self.editor_area.cut()

    def get_cursor_column(self) -> int:
        """Returns the current column number in which the cursor is.

        Returns:
            (int): Current column number.
        """
        return self.editor_area.textCursor().columnNumber() + 1

    def get_cursor_line(self) -> int:
        """Returns the current line number in which the cursor is.

        Returns:
            (int): Current line number.
        """
        return self.editor_area.textCursor().blockNumber() + 1
