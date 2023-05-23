import requests  # noqa
from PyQt5 import QtCore, QtGui, QtWidgets

import gui.login.res  # noqa
from navigator import navigate_to_main_app


class LoginUI(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
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
        self.user_line_edit = QtWidgets.QLineEdit(self.widget)
        self.user_line_edit.setGeometry(QtCore.QRect(390, 290, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.user_line_edit.setFont(font)
        self.user_line_edit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.user_line_edit.setStyleSheet(
            "background-color: rgba(0, 0, 0, 0);\n"
            "border: none;\n"
            "border-bottom: 2px solid rgba(105, 118, 132, 255);\n"
            "color: rgba(255, 255, 255, 230);\n"
            "padding-bottom: 7px;"
        )
        self.user_line_edit.setText('')
        self.user_line_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.user_line_edit.setObjectName('lineEdit')
        self.password_line_edit = QtWidgets.QLineEdit(self.widget)
        self.password_line_edit.setGeometry(QtCore.QRect(390, 410, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.password_line_edit.setFont(font)
        self.password_line_edit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.password_line_edit.setStyleSheet(
            "background-color: rgba(0, 0, 0, 0);\n"
            "border: none;\n"
            "border-bottom: 2px solid rgba(105, 118, 132, 255);\n"
            "color: rgba(255, 255, 255, 230);\n"
            "padding-bottom: 7px;"
        )
        self.password_line_edit.setText('')
        self.password_line_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.password_line_edit.setObjectName('lineEdit_2')
        self.password_line_edit.setEchoMode(QtWidgets.QLineEdit.Password)
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
            "    background-color: qlineargradient(spread:pad,x1:0, "
            "y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), "
            "stop:1 rgba(85, 98, 112, 226));\n"
            "    color: rgba(255, 255, 255, 210);\n"
            "    border-radius: 5px;    \n"
            "}\n"
            "QPushButton#pushButton:hover{    \n"
            "    background-color: qlineargradient(spread:pad,x1:0, "
            "y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219),"
            " stop:1 rgba(105, 118, 132, 226));\n"
            "}\n"
            "QPushButton#pushButton:pressed{\n"
            "    padding-left:5px;\n"
            "    padding-top:5px;\n"
            "    background-color: rgba(105, 118, 132, 200);\n"
            "}\n"
            ""
        )
        self.login_button.setObjectName('pushButton')
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(30, 30, 991, 631))
        self.label_5.setStyleSheet(
            "border-radius: 20px;\n"
            "background-color: rgba(0, 0, 0, 30);"
        )
        self.label_5.setText('')
        self.label_5.setObjectName('label_5')
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(30, 30, 991, 631))
        self.label_6.setStyleSheet(
            "border-radius: 20px;\n"
            "border-image: url(:/img/images/bg.png);\n"
            "background-color: rgba(0, 0, 0, 120);"
        )
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
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
        self.label_6.raise_()
        self.label_5.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.user_line_edit.raise_()
        self.password_line_edit.raise_()
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
        username = self.user_line_edit.text()
        password = self.password_line_edit.text()
        if username == '' or password == '':
            print('Username and password cannot be empty')
        else:
            self.login_user(username, password)

    def login_user(self, username, password):
        us, ps = 'baxx', 't123'
        if (username, password) == (us, ps):
            print('Login Successful!')
            navigate_to_main_app(self.window, username)
        else:
            print('Incorrect username or password')

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.window.setWindowTitle(_translate("Form", "OdontoDj"))
        self.label_4.setText(_translate("Form", "Login"))
        self.user_line_edit.setPlaceholderText(
            _translate("Form", "Username")
        )
        self.password_line_edit.setPlaceholderText(
            _translate("Form", "Password")
        )
        self.login_button.setText(_translate("Form", "L o g i n"))
        self.login_button.setFocus()
