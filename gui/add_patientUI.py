from PyQt5 import QtCore, QtGui, QtWidgets

import gui.main.res  # noqa
from api_connect import add_new_patient


class AddPatientUI(QtWidgets.QWidget):
    def __init__(self, parent=None, main_app=None):
        super().__init__(parent)
        self.access_token = main_app.access_token
        self.username = main_app.username
        self.url = main_app.url
        self.window = parent
        self.setupUi()

    def setupUi(self):
        self.window.switch_to_framed(show=False)
        self.window.setObjectName("MainWindow")
        self.window.resize(1120, 760)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.window.sizePolicy().hasHeightForWidth())
        self.window.setSizePolicy(sizePolicy)
        self.window.setStyleSheet(
            "border-image: url(:/newPrefix/images/app_bg.jpg);")
        self.centralwidget = QtWidgets.QWidget(self.window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.logo_frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.logo_frame.sizePolicy().hasHeightForWidth())
        self.logo_frame.setSizePolicy(sizePolicy)
        self.logo_frame.setStyleSheet("border-image: none;")
        self.logo_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo_frame.setObjectName("logo_frame")
        self.logo = QtWidgets.QLabel(self.logo_frame)
        self.logo.setGeometry(QtCore.QRect(10, 10, 91, 91))
        self.logo.setStyleSheet(
            "border-image: url(:/newPrefix/images/od_logo.png);")
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.title = QtWidgets.QLabel(self.logo_frame)
        self.title.setGeometry(QtCore.QRect(380, 30, 481, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet("color: rgba(255, 255, 255, 210);")
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.logo_frame, 0, 0, 1, 2)
        self.frame_7 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setStyleSheet("border-image: none;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.add_patient_button = QtWidgets.QPushButton(self.frame_7)
        self.add_patient_button.setGeometry(QtCore.QRect(430, 0, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.add_patient_button.setFont(font)
        self.add_patient_button.setStyleSheet(
            "QPushButton#add_patient_button {\n"
            "    border-image: none;\n"
            "    background-color: qconicalgradient(cx:0.5,"
            " cy:0.5, angle:45, stop:0 rgba(85, 98, 112, 226),"
            " stop:0.5 rgba(20, 47, 78, 219), stop:1 "
            "rgba(85, 98, 112, 226));\n"
            "    color: rgba(255, 255, 255, 210);\n"
            "    border-radius: 5px;\n"
            "}\n"
            "\n"
            "QPushButton#add_patient_button:hover {\n"
            "    background-color: qconicalgradient(cx:0.5,"
            " cy:0.5, angle:45, stop:0 rgba(105, 118, 132, 226),"
            " stop:0.5 rgba(40, 67, 98, 219), stop:1"
            " rgba(105, 118, 132, 226));\n"
            "}\n"
            "\n"
            "QPushButton#add_patient_button:pressed {\n"
            "    padding-left: 5px;\n"
            "    padding-top: 5px;\n"
            "    background-color: rgba(105, 118, 132, 200);\n"
            "}"
        )
        self.add_patient_button.setObjectName("add_patient_button")
        self.gridLayout.addWidget(self.frame_7, 4, 0, 1, 1)
        self.form_frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.form_frame.sizePolicy().hasHeightForWidth())
        self.form_frame.setSizePolicy(sizePolicy)
        self.form_frame.setStyleSheet("border-image: none;")
        self.form_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.form_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.form_frame.setObjectName("form_frame")
        self.first_name_label = QtWidgets.QLabel(self.form_frame)
        self.first_name_label.setGeometry(QtCore.QRect(110, 60, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.first_name_label.setFont(font)
        self.first_name_label.setStyleSheet(
            "color: rgba(255, 255, 255, 210);")
        self.first_name_label.setObjectName("first_name_label")
        self.first_name_input = QtWidgets.QLineEdit(self.form_frame)
        self.first_name_input.setGeometry(QtCore.QRect(250, 60, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.first_name_input.setFont(font)
        self.first_name_input.setText("")
        self.first_name_input.setAlignment(QtCore.Qt.AlignCenter)
        self.first_name_input.setObjectName("first_name_input")
        self.last_name_label = QtWidgets.QLabel(self.form_frame)
        self.last_name_label.setGeometry(QtCore.QRect(570, 60, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.last_name_label.setFont(font)
        self.last_name_label.setStyleSheet(
            "color: rgba(255, 255, 255, 210);")
        self.last_name_label.setObjectName("last_name_label")
        self.last_name_input = QtWidgets.QLineEdit(self.form_frame)
        self.last_name_input.setGeometry(QtCore.QRect(710, 60, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.last_name_input.setFont(font)
        self.last_name_input.setText("")
        self.last_name_input.setAlignment(QtCore.Qt.AlignCenter)
        self.last_name_input.setObjectName("last_name_input")
        self.gridLayout.addWidget(self.form_frame, 1, 0, 1, 1)
        self.time_frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.time_frame.sizePolicy().hasHeightForWidth())
        self.time_frame.setSizePolicy(sizePolicy)
        self.time_frame.setStyleSheet("border-image: none;")
        self.time_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.time_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.time_frame.setObjectName("time_frame")
        self.email_input = QtWidgets.QLineEdit(self.time_frame)
        self.email_input.setGeometry(QtCore.QRect(250, 10, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.email_input.setFont(font)
        self.email_input.setText("")
        self.email_input.setAlignment(QtCore.Qt.AlignCenter)
        self.email_input.setObjectName("email_input")
        self.email_label = QtWidgets.QLabel(self.time_frame)
        self.email_label.setGeometry(QtCore.QRect(110, 10, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.email_label.setFont(font)
        self.email_label.setStyleSheet("color: rgba(255, 255, 255, 210);")
        self.email_label.setObjectName("email_label")
        self.phone_number = QtWidgets.QLabel(self.time_frame)
        self.phone_number.setGeometry(QtCore.QRect(570, 10, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.phone_number.setFont(font)
        self.phone_number.setStyleSheet("color: rgba(255, 255, 255, 210);")
        self.phone_number.setObjectName("phone_number")
        self.phone_number_input = QtWidgets.QLineEdit(self.time_frame)
        self.phone_number_input.setGeometry(QtCore.QRect(710, 10, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.phone_number_input.setFont(font)
        self.phone_number_input.setText("")
        self.phone_number_input.setAlignment(QtCore.Qt.AlignCenter)
        self.phone_number_input.setObjectName("phone_number_input")
        self.gridLayout.addWidget(self.time_frame, 3, 0, 1, 1)
        self.last_name = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.last_name.sizePolicy().hasHeightForWidth())
        self.last_name.setSizePolicy(sizePolicy)
        self.last_name.setStyleSheet("border-image: none;")
        self.last_name.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.last_name.setFrameShadow(QtWidgets.QFrame.Raised)
        self.last_name.setObjectName("last_name")
        self.password_label = QtWidgets.QLabel(self.last_name)
        self.password_label.setGeometry(QtCore.QRect(110, 0, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.password_label.setFont(font)
        self.password_label.setStyleSheet("color: rgba(255, 255, 255, 210);")
        self.password_label.setObjectName("password_label")
        self.password_input = QtWidgets.QLineEdit(self.last_name)
        self.password_input.setGeometry(QtCore.QRect(250, 0, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.password_input.setFont(font)
        self.password_input.setText("")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setAlignment(QtCore.Qt.AlignCenter)
        self.password_input.setObjectName("password_input")
        self.password_input_2 = QtWidgets.QLineEdit(self.last_name)
        self.password_input_2.setGeometry(QtCore.QRect(710, 0, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.password_input_2.setFont(font)
        self.password_input_2.setText("")
        self.password_input_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input_2.setAlignment(QtCore.Qt.AlignCenter)
        self.password_input_2.setObjectName("password_input_2")
        self.password_label_2 = QtWidgets.QLabel(self.last_name)
        self.password_label_2.setGeometry(QtCore.QRect(570, 0, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.password_label_2.setFont(font)
        self.password_label_2.setStyleSheet("color: rgba(255, 255, 255, 210);")
        self.password_label_2.setObjectName("password_label_2")
        self.username_input = QtWidgets.QLineEdit(self.last_name)
        self.username_input.setGeometry(QtCore.QRect(250, 80, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.username_input.setFont(font)
        self.username_input.setText("")
        self.username_input.setAlignment(QtCore.Qt.AlignCenter)
        self.username_input.setObjectName("username_input")
        self.username_label = QtWidgets.QLabel(self.last_name)
        self.username_label.setGeometry(QtCore.QRect(110, 80, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.username_label.setFont(font)
        self.username_label.setStyleSheet("color: rgba(255, 255, 255, 210);")
        self.username_label.setObjectName("username_label")
        self.cpf_input = QtWidgets.QLineEdit(self.last_name)
        self.cpf_input.setGeometry(QtCore.QRect(710, 80, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.cpf_input.setFont(font)
        self.cpf_input.setText("")
        self.cpf_input.setAlignment(QtCore.Qt.AlignCenter)
        self.cpf_input.setObjectName("cpf_input")
        self.cpf_label = QtWidgets.QLabel(self.last_name)
        self.cpf_label.setGeometry(QtCore.QRect(570, 80, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cpf_label.setFont(font)
        self.cpf_label.setStyleSheet("color: rgba(255, 255, 255, 210);")
        self.cpf_label.setObjectName("cpf_label")
        self.gridLayout.addWidget(self.last_name, 2, 0, 1, 1)
        self.last_name_input.setTabOrder(
            self.last_name_input, self.password_input)
        self.password_input.setTabOrder(
            self.password_input, self.password_input_2)
        self.password_input_2.setTabOrder(
            self.password_input_2, self.username_input)
        self.cpf_input.setTabOrder(
            self.cpf_input, self.email_input)
        self.email_input.setTabOrder(
            self.email_input, self.phone_number_input)
        self.phone_number_input.setTabOrder(
            self.phone_number_input, self.add_patient_button)
        self.window.setCentralWidget(self.centralwidget)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.window)
        self.add_patient_button.clicked.connect(self.on_add_patient_click)
        self.window.show()

    def on_add_patient_click(self):
        first_name = self.first_name_input.text()
        last_name = self.last_name_input.text()
        cpf = self.cpf_input.text()
        email = self.email_input.text()
        username = self.username_input.text()
        password = self.password_input.text()
        password2 = self.password_input_2.text()
        phone_number = self.phone_number_input.text()
        data = {
            'first_name': first_name,
            'last_name': last_name,
            'cpf': cpf,
            'email': email,
            'password': password,
            'password2': password2,
            'username': username,
            'phone_number': phone_number,
        }
        close = False
        if not all([first_name, last_name, cpf, email, username, password]):
            title, text = 'Error', 'Please fill in all fields'
        elif add_new_patient(self.url, self.access_token, data):
            close = True
            title, text = 'Success', 'Patient added successfully'
        else:
            title, text = 'Error', 'Failed to add patient'
        message_box = QtWidgets.QMessageBox()
        message_box.setWindowTitle(title)
        message_box.setText(text)
        message_box.setFixedSize(150, 80)
        message_box.setWindowModality(QtCore.Qt.ApplicationModal)
        message_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        message_box.setDefaultButton(QtWidgets.QMessageBox.Ok)
        message_box.setIcon(QtWidgets.QMessageBox.Information)
        message_box.setWindowIcon(QtGui.QIcon('img/od_logo.png'))
        message_box.setWindowFlags(
            message_box.windowFlags() &
            ~QtCore.Qt.WindowCloseButtonHint
        )
        message_box.exec_()
        if close:
            self.centralwidget.close()
            self.window.close()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.window.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "Add New Patient"))
        self.add_patient_button.setText(_translate(
            "MainWindow", "Add Patient"))
        self.first_name_label.setText(_translate("MainWindow", "First Name"))
        self.last_name_label.setText(_translate("MainWindow", "Last Name"))
        self.email_label.setText(_translate("MainWindow", "Email"))
        self.phone_number.setText(_translate("MainWindow", "Phone Number"))
        self.password_label.setText(_translate("MainWindow", "Password"))
        self.password_label_2.setText(_translate(
            "MainWindow", "Repeat Password"))
        self.username_label.setText(_translate("MainWindow", "Username"))
        self.cpf_label.setText(_translate("MainWindow", "CPF"))
