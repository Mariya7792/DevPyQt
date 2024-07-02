import datetime
import json
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import QDeadlineTimer
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
        self.saved_notes = {}
        self.file = {"saved_notes": self.saved_notes}
        self.save_note()
        self.create_note()

        try:
            with open("data.json", "r", encoding="utf8") as file:
                self.file = json.load(file)
                self.saved_notes = self.file['notes_dict']
        except:
            with open("data.json", "w", encoding="utf-8") as file:
                self.file = {'notes_dict': self.saved_notes}
                json.dump(self.file, file, indent=4)
    def create_note(self):
        self.ui.NotesText.clear()
        self.ui.DeadlineData.setDateTime(datetime.datetime.now())
        self.ui.CurrentDate.setDateTime(datetime.datetime.now())
        #done
    def _initSignals(self):
        self.ui.AddButton.clicked.connect(self.create_note)
        self.ui.SaveButton.clicked.connect(lambda: self.save_note)
        self.ui.DeleteButton.clicked.connect(self.delete_note)
    def save_note(self):
        current_data = self.ui.CurrentDate.text()
        deadline = self.ui.DeadlineData.text()
        if not self.saved_notes:
            self.saved_notes[1] = {"date": current_data,
                                   "text": self.ui.NotesText.toPlainText(),
                                   "deadline": deadline
                                   }
        else:
            key = len(self.saved_notes) + 1
            self.saved_notes[key] = {"date": current_data,
                                     "text": self.ui.NotesText.toPlainText(),
                                     "deadline": deadline
                                     }
        with open("data.json", "w", encoding="utf-8") as file:
            self.file = {'notes_dict': self.saved_notes}
            json.dump(self.file, file, indent=4)
        # self.draw_list_menu()
        # self.ui.
    def delete_note(self):
        pass
    def show_list_menu(self):
        self.ui.NotesStorage.clear()
        # for element in list(self.notes_dict):

if __name__ ==  "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()
    app.exec()

