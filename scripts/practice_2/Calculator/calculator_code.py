
from PySide6 import QtWidgets
from a_calculator import Ui_Form

class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton_1.clicked.connect(self.button1)
        self.ui.pushButton_2.clicked.connect(self.button2)
        self.ui.pushButton_3.clicked.connect(self.button3)
        self.ui.pushButton_4.clicked.connect(self.button4)
        self.ui.pushButton_5.clicked.connect(self.button5)
        self.ui.pushButton_6.clicked.connect(self.button6)
        self.ui.pushButton_7.clicked.connect(self.button7)
        self.ui.pushButton_8.clicked.connect(self.button8)
        self.ui.pushButton_9.clicked.connect(self.button9)
        self.ui.DeleteButton.clicked.connect(self.clearbutton)
        self.ui.PlusButton.clicked.connect(self.summ)
        self.ui.MinusButton.clicked.connect(self.minus)
        self.ui.DivisionButton.clicked.connect(self.division)
        self.ui.MultipleButton.clicked.connect(self.multiply)


        # (lambda x: self.ui.NumberButton.setText(self.ui.pushButton_1.text()))

    def button1(self):
        input_text = self.ui.pushButton_1.text()
        self.ui.NumberButton.insert(input_text)

    def button2(self):
        input_text = self.ui.pushButton_2.text()
        self.ui.NumberButton.insert(input_text)

    def button3(self):
        input_text = self.ui.pushButton_3.text()
        self.ui.NumberButton.insert(input_text)

    def button4(self):
        input_text = self.ui.pushButton_4.text()
        self.ui.NumberButton.insert(input_text)

    def button5(self):
        input_text = self.ui.pushButton_5.text()
        self.ui.NumberButton.insert(input_text)

    def button6(self):
        input_text = self.ui.pushButton_6.text()
        self.ui.NumberButton.insert(input_text)

    def button7(self):
        input_text = self.ui.pushButton_7.text()
        self.ui.NumberButton.insert(input_text)

    def button8(self):
        input_text = self.ui.pushButton_8.text()
        self.ui.NumberButton.insert(input_text)

    def button9(self):
        input_text = self.ui.pushButton_9.text()
        self.ui.NumberButton.insert(input_text)

    def clearbutton(self):
        self.ui.NumberButton.clear()

    def summ(self):
        input_text = self.ui.PlusButton.text()
        self.ui.NumberButton.insert(input_text)

    def minus(self):
        input_text = self.ui.MinusButton.text()
        self.ui.NumberButton.insert(input_text)

    def division(self):
        input_text = self.ui.DivisionButton.text()
        self.ui.NumberButton.insert(input_text)

    def multiply(self):
        input_text = self.ui.MultipleButton.text()
        self.ui.NumberButton.insert(input_text)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()