"""
Файл для повторения темы QSettings

Напомнить про работу с QSettings.

Предлагается создать виджет с plainTextEdit на нём, при закрытии приложения,
сохранять введённый в нём текст с помощью QSettings, а при открытии устанавливать
в него сохранённый текст
"""

from PySide6 import QtWidgets, QtCore, QtGui


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.settings = QtCore.QSettings()
        self.initUI()
        self.settings_()

    def initUI(self):
        self.setFixedSize(300, 100)
        self.text_ = QtWidgets.QPlainTextEdit()
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.text_)
        self.setLayout(layout)

    def settings_(self):
        self.text_.("Text", self.text_.toPlainText())

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        """
        Событие закрытия окна

        :param event: QtGui.QCloseEvent
        :return: None
        """

        self.settings.setValue("Text", self.text_.toPlainText())




if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()

