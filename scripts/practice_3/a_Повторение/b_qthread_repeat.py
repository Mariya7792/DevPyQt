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
from requests import get

class GetUrlStatusThread(QtCore.QThread):
    status_code = QtCore.Signal(int)
    def __init__(self, url=None, delay=5, parent=None):
        super().__init__(parent)
        self.url = url
        self.delay = delay


    def run(self) -> None:
        while True:
            self.status_code.emit(get_status_code(self.url))
            time.sleep(self.delay)
    #     self.timer = QtCore.QTimer()
    #     self.timer.setInterval(1000)
    #     self.timer.timeout.connect(self.view_print)
    #     self.timer.start()
    #
    # def view_print(self):
    #     time.sleep(2)
    #     print('Прошла сек')

def get_status_code(url):
    response = get(url)
    return response.status_code
class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUi()
        self.__init_Threads()
        self.__init_Signals()
    # def get_status_code(url):
    #     response = get(url)
    #     return response.status_code

    def initUi(self):
        self.lineEditUrl = QtWidgets.QLineEdit()
        self.lineEditUrl.setPlaceholderText('Введите url')
        self.spinboxDely = QtWidgets.QSpinBox()
        self.spinboxDely.setMaximum(5)
        self.labelStatus = QtWidgets.QLabel()
        self.labelStatus.setText('Статус сайта:')
        self.TextEditlog = QtWidgets.QTextEdit()
        self.pushButton_ = QtWidgets.QPushButton('Клик')
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.lineEditUrl)
        layout.addWidget(self.spinboxDely)
        layout.addWidget(self.labelStatus)
        layout.addWidget(self.TextEditlog)
        layout.addWidget(self.pushButton_)


        self.setLayout(layout)
    def __init_Signals(self):
        self.getUrlStatusThread.status_code.connect(self.__changeStatus)
    def __init_Threads(self):
        url = self.lineEditUrl.text()
        self.getUrlStatusThread = GetUrlStatusThread()
        self.getUrlStatusThread.url = url
        self.getUrlStatusThread.delay = self.spinboxDely.value()
        self.getUrlStatusThread.start()
    def __changeStatus(self, status):
        self.TextEditlog.append(status)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
