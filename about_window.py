from PyQt6.QtWidgets import QDialog
from PyQt6 import uic


class AboutWindow(QDialog):
    """About window"""
    def __init__(self):
        super(AboutWindow, self).__init__()
        uic.loadUi("forms/aboutWindow.ui", self)
