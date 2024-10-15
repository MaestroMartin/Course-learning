import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow

# Calculator class inheriting from QMainWindow
class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(1000, 300, 500, 500)  # Set the window size and position
        self.initUI()

    # Initialize the UI components (labels, text fields, buttons)
    def initUI(self):
        # Label and input for the first number
        self.lbl_number1 = QtWidgets.QLabel(self)
        self.lbl_number1.setText("Number1: ")
        self.lbl_number1.move(50, 30)
        
        self.txt_number1 = QtWidgets.QLineEdit(self)
        self.txt_number1.move(150, 30)
        self.txt_number1.resize(200, 32)

        # Label and input for the second number
        self.lbl_number2 = QtWidgets.QLabel(self)
        self.lbl_number2.setText("Number2: ")
        self.lbl_number2.move(50, 80)
        
        self.txt_number2 = QtWidgets.QLineEdit(self)
        self.txt_number2.move(150, 80)
        self.txt_number2.resize(200, 32)

        # Addition button
        self.btn_add = QtWidgets.QPushButton(self)
        self.btn_add.setText("Addition")
        self.btn_add.move(150, 130)
        self.btn_add.clicked.connect(self.calculate)

        # Subtraction button
        self.btn_sub = QtWidgets.QPushButton(self)
        self.btn_sub.setText("Substraction")
        self.btn_sub.move(150, 180)
        self.btn_sub.clicked.connect(self.calculate)

        # Division button
        self.btn_div = QtWidgets.QPushButton(self)
        self.btn_div.setText("Division")
        self.btn_div.move(150, 230)
        self.btn_div.clicked.connect(self.calculate)

        # Multiplication button
        self.btn_mul = QtWidgets.QPushButton(self)
        self.btn_mul.setText("Multiplication")
        self.btn_mul.move(150, 280)
        self.btn_mul.clicked.connect(self.calculate)

        # Label for displaying the result
        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.setText("Result: ")
        self.lbl_result.move(150, 330)

    # Function to perform calculations based on the button clicked
    def calculate(self):
        sender = self.sender()  # Get which button was clicked
        result = 0

        try:
            num1 = float(self.txt_number1.text())  # Get the first number from the input
            num2 = float(self.txt_number2.text())  # Get the second number from the input

            # Perform the calculation based on which button was clicked
            if sender.text() == "Addition":
                result = num1 + num2
            elif sender.text() == "Substraction": 
                result = num1 - num2
            elif sender.text() == "Division":
                result = num1 / num2
            elif sender.text() == "Multiplication":
                result = num1 * num2

            # Update the result label
            self.lbl_result.setText("Result: " + str(result))

        except ValueError:
            self.lbl_result.setText("Invalid input!")  # Handle invalid input (e.g., non-numeric)

# Main function to start the application
def app():
    app = QApplication(sys.argv)
    win = Calculator()
    win.show()
    sys.exit(app.exec())

app()
