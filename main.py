import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from info import Info
from display import Display
from main_window import MainWindow
from variables import WINDOW_ICON_PATH
from buttons import ButtonsGrid


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    # Icon
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info(' ')
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
