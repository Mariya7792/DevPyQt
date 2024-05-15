"""
Файл для повторения темы QThread

Напомнить про работу с QThread.

Предлагается создать небольшое приложение, которое будет с помощью модуля request
получать доступность того или иного сайта (возвращать из потока status_code сайта).

Поработать с сигналами, которые возникают при запуске/остановке потока,
передать данные в поток (в данном случае url),
получить данные из потока (статус код сайта),
попробовать управлять потоком (запуск, остановка).

Опционально поработать с валидацией url
"""
import time
from PySide6 import QtWidgets, QtCore
import requests

class Worker(QtCore.QThread):
    progress = QtCore.Signal(int)
    def __init__(self, parent):
    #     self.timer = QtCore.QTimer()
    #     self.timer.setInterval(1000)
    #     self.timer.timeout.connect(self.view_print)
    #     super.__init__(parent)

    def run(self) -> None:
        while True:
            for i in range(10):
                time.sleep(0.2)
            print('Прошла сек')
    #     self.timer = QtCore.QTimer()
    #     self.timer.setInterval(1000)
    #     self.timer.timeout.connect(self.view_print)
    #     self.timer.start()
    #
    # def view_print(self):
    #     time.sleep(2)
    #     print('Прошла сек')


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.timer = Worker()
        self.timer.run()


    # def initUi(self):
    #     self.label = QtWidgets.QLabel("Выполнение долгой задачи: ")
    #     self.pushbutton = QtWidgets.QPushButton('Запуск долгой задачи')
    #
    #     layout = QtWidgets.QVBoxLayout()
    #     layout.addWidget(self.label)
    #     layout.addWidget(self.pushbutton)
    #
    #     self.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
