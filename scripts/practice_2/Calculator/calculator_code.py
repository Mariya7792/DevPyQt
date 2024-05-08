
from PySide6 import QtWidgets
from a_calculator import Ui_Form

class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton_1.clicked.connect(self.button1)
        self.ui.pushButton_2.clicked.connect(self.button2)
            # (lambda x: self.ui.NumberButton.setText(self.ui.pushButton_1.text()))

    def button1(self):
        input_text = self.ui.pushButton_1.text()
        self.ui.NumberButton.setText(input_text)
    def button2(self):
        input_text = self.ui.pushButton_2.text()
        self.ui.NumberButton.setText(input_text)
    def clearbutton(self):
        input_text =

    # def



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()