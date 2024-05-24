from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QLineEdit, QMessageBox
)
from PySide6.QtGui import QFont
from PySide6.QtCore import QSize

class CustomWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.label = QLabel("Masukkan detail Anda:")
        self.label.setFont(QFont('Arial'))

        self.name_textbox = QLineEdit()
        self.name_textbox.setFont(QFont('Arial'))
        self.name_textbox.setPlaceholderText("Nama")

        self.nim_textbox = QLineEdit()
        self.nim_textbox.setFont(QFont('Arial'))
        self.nim_textbox.setPlaceholderText("NIM")

        self.hobby_textbox = QLineEdit()
        self.hobby_textbox.setFont(QFont('Arial'))
        self.hobby_textbox.setPlaceholderText("Hobi")

        self.button_send = QPushButton("Kirim")
        self.button_send.setFont(QFont('Arial'))
        self.button_send.setStyleSheet("background-color: #82E0AA;")
        self.button_send.clicked.connect(self.display_info)

        self.button_reset = QPushButton("Reset")
        self.button_reset.setFont(QFont('Arial'))
        self.button_reset.setStyleSheet("background-color: #E9F5AA;")
        self.button_reset.clicked.connect(self.reset)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.name_textbox)
        self.layout.addWidget(self.nim_textbox)
        self.layout.addWidget(self.hobby_textbox)
        self.layout.addWidget(self.button_send)
        self.layout.addWidget(self.button_reset)

    def display_info(self):
        name = self.name_textbox.text()
        nim = self.nim_textbox.text()
        hobby = self.hobby_textbox.text()

        if not name:
            QMessageBox.warning(self, "Input Error", "Nama harus diisi!")
            return

        if not nim.isdigit():
            QMessageBox.warning(self, "Input Error", "NIM harus berupa angka!")
            return

        self.label.setText(f"Nama: {name}\nNIM: {nim}\nHobi: {hobby}")

    def reset(self):
        self.name_textbox.clear()
        self.nim_textbox.clear()
        self.hobby_textbox.clear()
        self.label.setText("Masukkan detail Anda:")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aplikasi Input Detail")
        self.setFixedSize(400, 300)

        self.widget = CustomWidget()
        self.setCentralWidget(self.widget)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
