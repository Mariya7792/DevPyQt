from PySide6 import QtCore, QtWidgets, QtGui
from notes import Ui_MainWindow
import json

"""Реализовать приложение для работы с заметками

Обязательные функции в приложении:

Добавление, изменение, удаление заметок
Сохранение времени добавления заметки и отслеживание времени до дэдлайна.
Реализация хранения заметок остаётся на ваш выбор (БД, json и т.д.)."""
"""
1) создать в designer форму окна
2) создать файл для хранения заметок
3) реализовать добавление / изменение / удаление
4) дэдлайн и отслеживание времени 
"""
class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._initSignals()
        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(, file)
            3self. -
            self.file = json.load(file)
            self.notes_dict = self.file["notes_dict"]
            self.last = self.file["last"]
    def _initSignals(self):
        self.ui.pushButton.clicked.connect(self.add_note)
        self.ui.pushButton_2.clicked.connect(self.change_note)
        self.ui.pushButton_3.clicked.connect(self.delete_note)
    def add_note(self):
        self.ui.textEdit.

    def change_note(self):
        self.ui.
    def delete_note(self):


if __name__ ==  "__main__":
    app = QtWidgets.QApplication

    window = Window()
    window.show()

    app.exec()

