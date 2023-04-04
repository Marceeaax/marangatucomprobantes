import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox, QDateEdit, QLabel, QLineEdit, QGridLayout, QMessageBox, QSpacerItem, QSizePolicy)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize, QDate


class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login Form')
        self.resize(500, 120)

        # Create a grid layout
        layout = QGridLayout()
        layout.setSpacing(10)

        # Create labels and line edits for username and password
        label_name = QLabel('Usuario')
        label_name.setFont(QFont('Calibri', 12))
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Please enter your username')
        self.lineEdit_username.setFont(QFont('Calibri', 12))
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)

        label_password = QLabel('Password')
        label_password.setFont(QFont('Calibri', 12))
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText('Please enter your password')
        self.lineEdit_password.setFont(QFont('Calibri', 12))
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)

        # Create a login button with an icon
        button_login = QPushButton('Login')
        button_login.setFont(QFont('Calibri', 12))
        button_login.setIcon(QIcon('login.png'))
        button_login.setIconSize(QSize(24, 24))
        button_login.setStyleSheet('background-color: #2196F3; color: #FFFFFF; border-radius: 5px; padding: 10px;')
        button_login.clicked.connect(self.check_password)
        layout.addWidget(button_login, 2, 0, 1, 2)

        # Add a spacer to push the button to the bottom of the layout
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer, 3, 0, 1, 2)

        # Set the layout for the widget
        self.setLayout(layout)

        # Set the stylesheet for the widget
        self.setStyleSheet('background-color: #333333; color: #FFFFFF;')

    def check_password(self):
        msg = QMessageBox()

        if self.lineEdit_username.text() == '123' and self.lineEdit_password.text() == '000':
            self.form2 = MainForm()
            self.form2.show()
            self.hide()
            
        else:
            msg.setText('Incorrect Password')
            msg.exec_()


class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Form')
        self.resize(400, 200)

        # Create widgets for the form
        label_date_start = QLabel('Initial Date')
        self.date_edit_start = QDateEdit()
        self.date_edit_start.setCalendarPopup(True)
        self.date_edit_start.setDate(self.date_edit_start.minimumDate())

        label_date_end = QLabel('Final Date')
        self.date_edit_end = QDateEdit()
        self.date_edit_end.setCalendarPopup(True)
        self.date_edit_end.setDate(self.date_edit_end.maximumDate())

        label_option = QLabel('Select an option')
        self.combo_box_option = QComboBox()
        self.combo_box_option.addItem('Compras')
        self.combo_box_option.addItem('Ventas')
        self.combo_box_option.addItem('Egresos')
        self.combo_box_option.addItem('Ingresos')

        button_submit = QPushButton('Submit')
        button_submit.clicked.connect(self.submit_form)

        # Create layouts for the form
        layout_dates = QVBoxLayout()
        layout_dates.addWidget(label_date_start)
        layout_dates.addWidget(self.date_edit_start)
        layout_dates.addWidget(label_date_end)
        layout_dates.addWidget(self.date_edit_end)

        layout_option = QVBoxLayout()
        layout_option.addWidget(label_option)
        layout_option.addWidget(self.combo_box_option)

        layout_form = QHBoxLayout()
        layout_form.addLayout(layout_dates)
        layout_form.addLayout(layout_option)

        layout_button = QVBoxLayout()
        layout_button.addWidget(button_submit)

        main_layout = QVBoxLayout()
        main_layout.addLayout(layout_form)
        main_layout.addLayout(layout_button)

        # Set the layout for the widget
        self.setLayout(main_layout)

    def submit_form(self):
        date_start = self.date_edit_start.date()
        date_end = self.date_edit_end.date()
        option = self.combo_box_option.currentText()

        # Do something with the form data
        print(date_start.toString('yyyy-MM-dd'))
        print(date_end.toString('yyyy-MM-dd'))
        print(option)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    form = LoginForm()
    form.show()

    sys.exit(app.exec_())
