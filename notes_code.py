import datetime

from PySide6 import QtCore, QtWidgets, QtGui
from notes import Ui_MainWindow
import json

"""Реализовать приложение для работы с заметками

Обязательные функции в приложении:

Добавление, изменение, удаление заметок
Сохранение времени добавления заметки и отслеживание времени до дэдлайна.
Реализация хранения заметок остаётся на ваш выбор (БД, json и т.д.)."""
"""
1) создать в designer форму окна - готово
2) создать файл для хранения заметок
3) реализовать добавление / изменение / удаление
4) дэдлайн и отслеживание времени 
"""
class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._initSignals()
        self.create_note()
        self.saved_notes = {}
    def create_note(self):
        with open("data.json", "w", encoding="utf-8") as file:
            self.file = {"saved_notes": self.saved_notes}
            json.dump(self.file, file)

    def _initSignals(self):
        self.ui.AddButton.clicked.connect(self.add_note)
        self.ui.ChangeButton.clicked.connect(self.change_note)
        self.ui.DeleteButton.clicked.connect(self.delete_note)
    def add_note(self):
        # input_text = self.ui.NotesText.textChanged()
        time_added = datetime.datetime.now()
        data_to_deadline = self.ui.DeadlineData() - time_added
        self.notes_dict = {"date": time_added,
                           "text": self.ui.NotesText.textChanged(),
                           "deadline": self.ui.DeadlineData()
                           }
        with open("data.json", "w", encoding="utf-8") as file:
            self.file = {}
        pass
        # self.ui.textEdit.

    def change_note(self):
        pass
        # self.ui.
    def delete_note(self):
        pass

if __name__ ==  "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()

