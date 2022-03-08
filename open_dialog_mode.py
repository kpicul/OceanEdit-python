from enum import Enum


class OpenDialogMode(Enum):
    """Tells us in what mode we set file dialog."""

    """Mode for opening files."""
    OPEN = 0,

    """Mode for writing file."""
    WRITE = 1
