from PyQt6.QtWidgets import QFileDialog, QWidget, QErrorMessage
from open_dialog_mode import OpenDialogMode
from about_window import AboutWindow


def open_file_dialog(parent: QWidget, dialog_title: str, mode: OpenDialogMode, file_filter: str = "") -> str:
    """ Open file dialog.

    Args:
        parent (QWidget): The parent widget.
        dialog_title (str): Title of the dialog.
        mode (OpenDialogMode): Mode of the open dialog. Either open or write.
        file_filter (str): Filter for file types.

    Returns:
        str: Path of the selected file.

    """
    file_path: str = ""
    if mode is OpenDialogMode.OPEN:
        file_path, _ = QFileDialog.getOpenFileName(parent, dialog_title, file_filter, "")
    elif mode is OpenDialogMode.WRITE:
        file_path, _ = QFileDialog.getSaveFileName(parent, dialog_title, file_filter, "")

    return file_path


def show_error_dialog(error_content: str):
    """Opens error dialog.

    Args:
        error_content (str): Content of the error.

    """
    error_dialog = QErrorMessage()
    error_dialog.showMessage(error_content)
    error_dialog.exec()


def show_about_dialog():
    """Opens about window."""
    about_dialog = AboutWindow()
    about_dialog.exec()
