from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit


class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet('font-size: 40px;')
        self.setMinimumHeight(80)
        self.setMinimumWidth(400)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(15, 15, 15, 15)
