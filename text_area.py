from PyQt6.QtWidgets import QWidget, QPlainTextEdit, QLabel
from PyQt6.QtGui import QTextBlock, QPainter, QPaintEvent, QColor
from PyQt6.QtCore import Qt
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
        self.line_number_area: QWidget = self.findChild(QPlainTextEdit, "lineNumberArea")
        self.file_path: str = ""

        self.editor_area.blockCountChanged.connect(self.set_line_numbers)

    def set_content(self, file_path: str):
        """Sets the area content.

        Args:
            file_path (str): path of the file which contains the content..
        """
        self.file_path = file_path
        content: str = read_file(file_path)
        self.editor_area.setPlainText(content)
        self.set_line_numbers()

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
    
    def set_line_numbers(self, event: QPaintEvent):
        painter = QPainter(self.line_number_area)
        block = self.editor_area.firstVisibleBlock()
        block_number: int = block.blockNumber()
        top: int = round(self.editor_area.blockBoundingGeometry(block)
                         .translated(self.editor_area.contentOffset()).top())
        bottom: int = top + round(self.editor_area.blockBoundingRect(block).height())
        while block.isValid() and top <= event.rect().bottom():
            if block.isVisible() and bottom >= event.rect().top():
                number: str = str(block_number + 1)
                painter.setPen(QColor.black)
                painter.drawText(0, top, self.line_number_area.width(), self.editor_area.fontMetrics().height(),
                                 Qt.AlignmentFlag.AlignRight, number)
            block = block.next()
            top = bottom
            bottom = top + round(self.editor_area.blockBoundingRect(block).height())
            block_number += 1
