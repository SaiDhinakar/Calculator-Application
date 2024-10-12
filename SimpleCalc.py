from PyQt5.QtWidgets import QApplication, QLineEdit, QGridLayout, QPushButton, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QIcon, QFont


class CalcApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon(r"C:\Users\{user name}\Downloads\Calculator_37533.ico")) # path to load icon of your application
        self.resize(250,300)

        self.text_area = QLineEdit()
        self.text_area.setFont(QFont("Helvetica", 32))
        self.grid = QGridLayout()

        self.Delete = QPushButton('<-')
        self.Clear = QPushButton('C')

        self.Delete.setStyleSheet("QPushButton {  font: 25pt Comic Sans MS; padding: 10px; }")
        self.Clear.setStyleSheet("QPushButton {  font: 25pt Comic Sans MS; padding: 10px; background-color: yellow;}")

        self.buttons = [
            '7','8','9','/',
            '4','5','6','*',
            '1','2','3','-',
            '0','.','=','+',
        ]

        row = 0
        col = 0

        for value in self.buttons:
            button = QPushButton(value)
            button.setStyleSheet("QPushButton { font: 25pt Comic Sans MS; }")
            button.clicked.connect(self.button_clicked)
            self.grid.addWidget(button,row,col)

            col += 1
            if col>3:
                col = 0
                row += 1
            
        master_layout = QVBoxLayout()
        master_layout.addWidget(self.text_area)
        master_layout.addLayout(self.grid)

        button_row = QHBoxLayout()
        button_row.addWidget(self.Clear)
        button_row.addWidget(self.Delete)

        self.Clear.clicked.connect(self.button_clicked)
        self.Delete.clicked.connect(self.button_clicked)
        master_layout.addLayout(button_row)
        master_layout.setContentsMargins(35,35,35,35)
        self.setLayout(master_layout)

    def button_clicked(self):
        button = app.sender()
        text = button.text()

        if text == '=':
            try:
                result = eval(self.text_area.text())
                self.text_area.setText(str(result))
            except:
                self.text_area.setText('Error')
        elif text == '<-':
            self.text_area.setText(str(self.text_area.text()[:-1]))
        elif text == 'C':
            self.text_area.clear()
        else:
            self.text_area.setText(self.text_area.text() + text)
        


if __name__ == '__main__':
    app = QApplication([])
    main_window = CalcApp()
    main_window.setStyleSheet("CalcApp { background-color: grey; }")
    main_window.show()
    app.exec_()