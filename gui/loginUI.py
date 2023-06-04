from PyQt5 import QtCore, QtGui, QtWidgets

import gui.login.res  # noqa
from api_connect import VerificationThread
from navigator import navigate_to_main_app


class LoginUI(QtWidgets.QWidget):
    def __init__(self, parent=None, url=''):
        super().__init__(parent)
        self.url = url
        self.window = parent
        self.setupUi()

    def setupUi(self):
        self.window.switch_to_frameless()
        self.widget = QtWidgets.QWidget(self.window)
        self.widget.setGeometry(QtCore.QRect(30, 30, 1051, 691))
        self.widget.setObjectName('widget')
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(340, 160, 351, 481))
        self.label_2.setStyleSheet(
            "background-color: rgba(0, 0, 0, 150);\n"
            "border-radius: 40px;"
        )
        self.label_2.setText('')
        self.label_2.setObjectName('label_2')
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(340, 60, 351, 91))
        self.label_3.setStyleSheet("border-image: url(:/img/images/od.png);")
        self.label_3.setText('')
        self.label_3.setObjectName('label_3')
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(460, 210, 121, 51))
        font = QtGui.QFont()
        font.setFamily('Sans Serif Collection')
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgba(255, 255, 255, 210);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName('label_4')
        self.line_edit_style = """
            background-color: rgba(0, 0, 0, 0);\n
            border: none;\n
            border-bottom: 2px solid rgba(105, 118, 132, 255);\n
            color: rgba(255, 255, 255, 230);\n
            padding-bottom: 7px;
        """
        self.user_input = QtWidgets.QLineEdit(self.widget)
        self.user_input.setGeometry(QtCore.QRect(390, 290, 251, 61))
        font = QtGui.QFont()
        font.setFamily('Sans Serif Collection')
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.warning_label = QtWidgets.QLabel(self.widget)
        self.warning_label.setStyleSheet("color: rgba(255, 0, 0, 200);")
        self.warning_label.setGeometry(QtCore.QRect(410, 335, 251, 61))
        self.warning_label.setFont(font)
        self.warning_label.setText('')
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.user_input.setFont(font)
        self.user_input.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.user_input.setStyleSheet(self.line_edit_style)
        self.user_input.setText('')
        self.user_input.setAlignment(QtCore.Qt.AlignCenter)
        self.user_input.setObjectName('lineEdit')
        self.password_input = QtWidgets.QLineEdit(self.widget)
        self.password_input.setGeometry(QtCore.QRect(390, 410, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.password_input.setFont(font)
        self.password_input.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.password_input.setStyleSheet(self.line_edit_style)
        self.password_input.setText('')
        self.password_input.setAlignment(QtCore.Qt.AlignCenter)
        self.password_input.setObjectName('lineEdit_2')
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_button = QtWidgets.QPushButton(self.widget)
        self.login_button.setGeometry(QtCore.QRect(420, 510, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.login_button.setFont(font)
        self.login_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.login_button.setStyleSheet(
            "QPushButton#pushButton{\n"
            "background-color: qconicalgradient(cx:0.5, cy:0.5, angle:45,"
            "stop:0 rgba(85, 98, 112, 226), stop:0.5 rgba(20, 47, 78, 219),"
            "stop:1 rgba(85, 98, 112, 226));"
            "    color: rgba(255, 255, 255, 210);\n"
            "    border-radius: 5px;    \n"
            "}\n"
            "QPushButton#pushButton:hover{    \n"
            "    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:45,"
            "stop:0 rgba(105, 118, 132, 226), stop:0.5 rgba(40, 67, 98, 219),"
            "stop:1 rgba(105, 118, 132, 226));"
            "}\n"
            "QPushButton#pushButton:pressed{\n"
            "    padding-left:5px;\n"
            "    padding-top:5px;\n"
            "    background-color: rgba(105, 118, 132, 200);\n"
            "}\n"
            ""
        )
        self.login_button.setObjectName('pushButton')
        self.bg_cover = QtWidgets.QLabel(self.widget)
        self.bg_cover.setGeometry(QtCore.QRect(30, 30, 991, 631))
        self.bg_cover.setStyleSheet(
            "border-radius: 20px;\n"
            "background-color: rgba(0, 0, 0, 40);"
        )
        self.bg_cover.setText('')
        self.bg_cover.setObjectName('label_5')
        self.bg_widget = QtWidgets.QLabel(self.widget)
        self.bg_widget.setGeometry(QtCore.QRect(30, 30, 991, 631))
        self.bg_widget.setStyleSheet(
            "border-radius: 20px;\n"
            "border-image: url(:/img/images/bg.png);\n"
            "background-color: rgba(0, 0, 0, 120);"
        )
        self.bg_widget.setText("")
        self.bg_widget.setObjectName("label_6")
        self.closeButton = QtWidgets.QPushButton(self.widget)
        self.closeButton.setGeometry(QtCore.QRect(980, 40, 31, 31))
        self.closeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.closeButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.closeButton.setStyleSheet(
            "QPushButton#closeButton {\n"
            "    background-color: transparent;\n"
            "    border: none;\n"
            "    image: url(:/img/images/x.png);\n"
            "}"
        )
        self.closeButton.setText('')
        self.closeButton.setObjectName('closeButton')
        self.minimizeButton = QtWidgets.QPushButton(self.widget)
        self.minimizeButton.setGeometry(QtCore.QRect(940, 40, 31, 31))
        self.minimizeButton.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.minimizeButton.setStyleSheet(
            "QPushButton#minimizeButton {\n"
            "    background-color: transparent;\n"
            "    border: none;\n"
            "    image: url(:/img/images/min.png);\n"
            "}"
        )
        self.minimizeButton.setText('')
        self.minimizeButton.setObjectName('minimizeButton')
        self.bg_widget.raise_()
        self.bg_cover.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.user_input.raise_()
        self.password_input.raise_()
        self.warning_label.raise_()
        self.login_button.raise_()
        self.closeButton.raise_()
        self.minimizeButton.raise_()
        self.login_button.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(
                blurRadius=25, xOffset=3, yOffset=3,
                color=QtGui.QColor(105, 118, 132, 100)
            )
        )
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.window)
        self.closeButton.clicked.connect(self.on_close_app)
        self.minimizeButton.clicked.connect(self.on_minimize_window)
        self.login_button.clicked.connect(self.on_login_clicked)

    def on_close_app(self):
        QtWidgets.QApplication.quit()

    def on_minimize_window(self):
        self.window.showMinimized()

    def on_login_clicked(self):
        username = self.user_input.text()
        password = self.password_input.text()
        self.set_widgets_enabled(False)
        print('Logging in...')
        self.warning_label.setText('Logging in...')
        self.warning_label.setStyleSheet("color: rgba(220, 0, 0, 200);")
        self.user_input.setStyleSheet(self.line_edit_style)
        self.password_input.setStyleSheet(self.line_edit_style)
        if not username or not password:
            self.warning_label.setText('Enter your credentials')
            print('Username and password cannot be empty')
            self.user_input.setStyleSheet(
                self.line_edit_style +
                "background-color: rgba(255, 0, 0, 50);"
            )
            self.password_input.setStyleSheet(
                self.line_edit_style +
                "background-color: rgba(255, 0, 0, 50);"
            )
            self.user_input.setToolTip(
                'Username and password cannot be empty'
            )
        else:
            self.verification_thread = VerificationThread(
                {'username': username, 'password': password},
                self.url,
            )
            self.verification_thread.finished.connect(
                self.on_verification_finished
            )
            self.verification_thread.start()

    def on_verification_finished(self, access_token):
        self.set_widgets_enabled(True)
        self.login_user(access_token)

    def login_user(self, access_token):
        if access_token:
            print('Login Successful!')
            navigate_to_main_app(
                self.window,
                self.user_input.text(),
                self.url,
                access_token
            )
            self.warning_label.setText('Login Successful')
            self.warning_label.setStyleSheet("color: rgba(0, 255, 0, 200);")
        else:
            self.warning_label.setText('Invalid Credentials')
            self.warning_label.setStyleSheet("color: rgba(255, 0, 0, 200);")
            print('Incorrect username or password')
            self.user_input.setStyleSheet(
                self.line_edit_style +
                "background-color: rgba(255, 0, 0, 50);"
            )
            self.password_input.setStyleSheet(
                self.line_edit_style +
                "background-color: rgba(255, 0, 0, 50);"
            )
            self.user_input.setToolTip(
                'Incorrect username or password'
            )

    def set_widgets_enabled(self, enabled):
        self.user_input.setEnabled(enabled)
        self.password_input.setEnabled(enabled)
        self.login_button.setEnabled(enabled)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.window.setWindowTitle(_translate("Form", "OdontoDj"))
        self.label_4.setText(_translate("Form", "Login"))
        self.user_input.setPlaceholderText(
            _translate("Form", "Username")
        )
        self.password_input.setPlaceholderText(
            _translate("Form", "Password")
        )
        self.login_button.setText(_translate("Form", "L o g i n"))
        self.login_button.setFocus()
