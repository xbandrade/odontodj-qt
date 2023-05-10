import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QFontDatabase, QIcon, QPixmap
from PyQt5.QtWidgets import (QFormLayout, QHBoxLayout, QLabel, QLineEdit,
                             QPushButton, QVBoxLayout, QWidget)


class LoginWindow(QWidget):
    def __init__(self, width, height):
        super().__init__()
        self.setFixedSize(width, height)
        self.setWindowTitle('OdontoDJ')
        self.setStyleSheet('background-color: #a8a8ea;')
        self.setWindowIcon(QIcon('img/od_logo.png'))
        img_path = os.path.join(os.path.dirname(__file__), 'img', 'od.png')
        pixmap = QPixmap(img_path)
        self.logo = QLabel(self)
        self.logo.setPixmap(pixmap)
        self.username_label = QLabel('Username')
        self.username_edit = QLineEdit()
        self.username_edit.setMaximumWidth(200)
        self.password_label = QLabel('Password')
        self.password_edit = QLineEdit()
        self.password_edit.setMaximumWidth(200)
        self.password_edit.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton('Login')
        self.login_button.clicked.connect(self._login_clicked)
        self.label_layout = self._create_label_layout()
        self.logo_layout = self._create_logo_layout()
        self.login_layout = self._create_login_layout()
        self.main_layout = self._create_main_layout()
        self.setLayout(self.main_layout)

    def _create_label_layout(self):
        label_layout = QFormLayout()
        label_layout.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        label_layout.addRow(self.username_label, self.username_edit)
        label_layout.addRow(self.password_label, self.password_edit)
        label_layout.setSpacing(20)
        label_layout.setAlignment(Qt.AlignCenter)
        return label_layout

    def _create_logo_layout(self):
        logo_layout = QHBoxLayout()
        logo_layout.addWidget(self.logo, 0, Qt.AlignTop | Qt.AlignHCenter)
        return logo_layout

    def _create_login_layout(self):
        login_layout = QVBoxLayout()
        login_layout.addStretch(1)
        login_layout.addLayout(self.label_layout)
        login_layout.addWidget(self.login_button, 0, Qt.AlignHCenter)
        login_layout.addStretch(1)
        return login_layout

    def _create_main_layout(self):
        main_layout = QVBoxLayout()
        main_layout.addLayout(self.logo_layout)
        main_layout.addLayout(self.login_layout)
        return main_layout

    def _login_clicked(self):
        # TODO: verify login credentials
        print('Login button clicked!')
        main_window = MainWindow()
        self.setLayout(main_window.main_layout)  # FIXME: remove old one first


class MainWindow(QWidget):  # <-> MainLayout (?)
    def __init__(self):
        super().__init__()
        self.label = QLabel('Logged in!')
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(
            self.label, 0, Qt.AlignTop | Qt.AlignHCenter
        )
        self.setLayout(self.main_layout)

    def _load_font(self, font_size):
        font_filename = "RobotoSlab-ExtraBold.ttf"
        font_path = os.path.join(
            os.path.dirname(__file__), 'fonts', font_filename
        )
        font_id = QFontDatabase.addApplicationFont(font_path)
        font = QFont("Roboto Slab", font_size)
        if font_id != -1:
            font_families = QFontDatabase.applicationFontFamilies(font_id)
            if font_families:
                font.setFamily(font_families[0])
        return font
