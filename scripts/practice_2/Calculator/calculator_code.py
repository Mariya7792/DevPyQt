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
        self.ui.DeleteButton.clicked.connect(self.clear_button)
        self.ui.PlusButton.clicked.connect(self.summ)
        self.ui.MinusButton.clicked.connect(self.minus)
        self.ui.DivisionButton.clicked.connect(self.division)
        self.ui.MultiplyButton.clicked.connect(self.multiply)
        self.ui.ResultButton.clicked.connect(self.equals)

        # (lambda x: self.ui.NumberButton.setText(self.ui.pushButton_1.text()))

    def button1(self):
        input_text = self.ui.pushButton_1.text()
        self.ui.Display_field.insert(input_text)

    def button2(self):
        input_text = self.ui.pushButton_2.text()
        self.ui.Display_field.insert(input_text)

    def button3(self):
        input_text = self.ui.pushButton_3.text()
        self.ui.Display_field.insert(input_text)

    def button4(self):
        input_text = self.ui.pushButton_4.text()
        self.ui.Display_field.insert(input_text)

    def button5(self):
        input_text = self.ui.pushButton_5.text()
        self.ui.Display_field.insert(input_text)

    def button6(self):
        input_text = self.ui.pushButton_6.text()
        self.ui.Display_field.insert(input_text)

    def button7(self):
        input_text = self.ui.pushButton_7.text()
        self.ui.Display_field.insert(input_text)

    def button8(self):
        input_text = self.ui.pushButton_8.text()
        self.ui.Display_field.insert(input_text)

    def button9(self):
        input_text = self.ui.pushButton_9.text()
        self.ui.Display_field.insert(input_text)

    def clear_button(self):
        self.ui.Display_field.clear()

    def summ(self):
        input_text = self.ui.PlusButton.text()
        self.ui.Display_field.insert(input_text)

    def minus(self):
        input_text = self.ui.MinusButton.text()
        self.ui.Display_field.insert(input_text)

    def division(self):
        input_text = self.ui.DivisionButton.text()
        self.ui.Display_field.insert(input_text)

    def multiply(self):
        input_text = self.ui.MultiplyButton.text()
        self.ui.Display_field.insert(input_text)

    def equals(self):
        try:
            input_text = self.ui.Display_field.text()
            ans = eval(input_text)
            self.ui.Display_field.setText(str(ans))
        except SyntaxError:
            self.ui.Display_field.setText('Error')


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
