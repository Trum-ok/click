import os
import pyautogui
import time
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon


class Clicker(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        # Настройки
        self.delay = 1000
        self.is_running = False
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir, "guardian.png")
        style_path = os.path.join(current_dir, "MaterialDark.qss")

        # Создание интерфейса
        self.setWindowTitle("Буль")
        self.layout = QtWidgets.QVBoxLayout()
        icon = QIcon(image_path)
        self.setWindowIcon(icon)

        # Поле для ввода задержки
        self.delay_input = QtWidgets.QLineEdit()
        self.delay_input.setText(str(self.delay))
        self.delay_input.editingFinished.connect(self.set_delay)
        self.layout.addWidget(self.delay_input)

        # Кнопка Старт
        self.start_button = QtWidgets.QPushButton("Старт")
        self.start_button.clicked.connect(self.start_click)
        self.layout.addWidget(self.start_button)

        # Кнопка Стоп
        self.stop_button = QtWidgets.QPushButton("Стоп")
        self.stop_button.clicked.connect(self.stop_click)
        self.layout.addWidget(self.stop_button)

        # Стиль
        # # style_file = os.path.join("MaterialDark.qss")
        # style_file = os.path.join("/MaterialDark.qss")
        # # style_file = 'MaterialDark.qss'
        with open(style_path, 'r') as file:
            style = file.read()
            self.setStyleSheet(style)

        # self.setStyleSheet(
        #     "QPushButton { background-color: #4CAF50; color: white; border-radius: 5px; padding: 5px; border: none; }"
        #     "QWidget { background-color: #333; color: white; }")

        self.setLayout(self.layout)

    def start_click(self):
        self.is_running = True
        self.click()

    def stop_click(self):
        self.is_running = False
        self.delay_input.setText(str(self.delay))

    def set_delay(self):
        try:
            self.delay = int(self.delay_input.text())
        except ValueError:
            self.delay = 1000

    def click(self):
        while self.is_running:
            pyautogui.click()
            time.sleep(self.delay / 1000)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    clicker = Clicker()
    clicker.show()
    app.exec()
