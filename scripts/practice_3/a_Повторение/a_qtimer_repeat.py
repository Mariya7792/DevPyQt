"""
Файл для повторения темы QTimer

Напомнить про работу с QTimer.

Предлагается создать приложение-которое будет
с некоторой периодичностью вызывать определённую функцию.
"""

from PySide6 import QtWidgets, QtCore
import time

class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.view_print)
        self.timer.start()

    def view_print(self):
        time.sleep(2)
        print('Прошла сек')


    def initUI(self):

        self.labelTime = QtWidgets.QLabel()

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
