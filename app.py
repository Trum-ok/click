import os
import sys
import pyautogui
import time
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
import threading


class Clicker(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        # Settings
        self.delay = 1000
        self.is_running = False
        self.click_thread = None

        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir, "guardian.png")
        style_path = os.path.join(current_dir, "MaterialDark.qss")

        # UI
        self.setWindowTitle("Буль")
        self.layout = QtWidgets.QVBoxLayout()
        icon = QIcon(image_path)
        self.setWindowIcon(icon)

        # Input
        self.delay_input = QtWidgets.QLineEdit()
        self.delay_input.setText(str(self.delay))
        self.delay_input.editingFinished.connect(self.set_delay)
        self.layout.addWidget(self.delay_input)

        # Start button
        self.start_button = QtWidgets.QPushButton("Старт")
        self.start_button.clicked.connect(self.start_click)
        self.layout.addWidget(self.start_button)

        # Stop button
        self.stop_button = QtWidgets.QPushButton("Стоп")
        self.stop_button.clicked.connect(self.stop_click)
        self.layout.addWidget(self.stop_button)

        # Style
        with open(style_path, 'r') as file:
            style = file.read()
            self.setStyleSheet(style)

        self.setLayout(self.layout)

        self.show()

    def start_click(self):
        if not self.is_running:
            self.is_running = True
            self.click_thread = threading.Thread(target=self.click)
            self.click_thread.start()

    def stop_click(self):
        if self.is_running:
            self.is_running = False
            self.delay_input.setText(str(self.delay))
            self.click_thread.join()

    def set_delay(self):
        try:
            self.delay = int(self.delay_input.text())
        except ValueError:
            self.delay = 1000

    def click(self):
        try:
            while self.is_running:
                pyautogui.click()
                time.sleep(self.delay / 1000)
        except pyautogui.FailSafeException as e:
            self.is_running = False


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    clicker = Clicker()
    clicker.show()
    sys.exit(app.exec())
