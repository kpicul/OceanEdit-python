from PyQt6.QtWidgets import QFileDialog, QWidget, QErrorMessage


def open_file_dialog(parent: QWidget, dialog_title: str, file_filter: str = "") -> str:
    file_path: str
    file_path, _ = QFileDialog.getOpenFileName(parent, dialog_title, file_filter, "")
    return file_path


def show_error_dialog(error_content: str):
    error_dialog = QErrorMessage()
    error_dialog.showMessage(error_content)
    error_dialog.exec()
