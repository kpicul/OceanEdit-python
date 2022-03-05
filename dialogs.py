from PyQt6.QtWidgets import QFileDialog, QWidget, QErrorMessage


def open_file_dialog(parent: QWidget, dialog_title: str, file_filter: str = "") -> str:
    """ Open file dialog.

    Args:
        parent (QWidget): The parent widget.
        dialog_title (str): Title of the dialog.
        file_filter (str): Filter for file types.

    Returns:
        str: Path of the selected file.

    """
    file_path: str
    file_path, _ = QFileDialog.getOpenFileName(parent, dialog_title, file_filter, "")
    return file_path


def show_error_dialog(error_content: str):
    """Opens error dialog.

    Args:
        error_content (str): Content of the error.

    """
    error_dialog = QErrorMessage()
    error_dialog.showMessage(error_content)
    error_dialog.exec()
