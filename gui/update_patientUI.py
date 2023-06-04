from PyQt5 import QtCore, QtGui, QtWidgets

import gui.main.res  # noqa
from api_connect import retrieve_patient_details, update_patient


class UpdatePatientUI(QtWidgets.QWidget):
    def __init__(self, parent=None, main_app=None):
        super().__init__(parent)
        self.access_token = main_app.access_token
        self.username = main_app.username
        self.url = main_app.url
        self.window = parent
        self.current_patient = None
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
        self.update_button = QtWidgets.QPushButton(self.frame_7)
        self.update_button.setGeometry(
            QtCore.QRect(430, 0, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.update_button.setFont(font)
        self.update_button.setStyleSheet(
            "QPushButton#update_patient_button {\n"
            "    border-image: none;\n"
            "    background-color: qconicalgradient(cx:0.5,"
            " cy:0.5, angle:45, stop:0 rgba(85, 98, 112, 226),"
            " stop:0.5 rgba(20, 47, 78, 219), stop:1 "
            "rgba(85, 98, 112, 226));\n"
            "    color: rgba(255, 255, 255, 210);\n"
            "    border-radius: 5px;\n"
            "}\n"
            "\n"
            "QPushButton#update_patient_button:hover {\n"
            "    background-color: qconicalgradient(cx:0.5,"
            " cy:0.5, angle:45, stop:0 rgba(105, 118, 132, 226),"
            " stop:0.5 rgba(40, 67, 98, 219), stop:1"
            " rgba(105, 118, 132, 226));\n"
            "}\n"
            "\n"
            "QPushButton#update_patient_button:pressed {\n"
            "    padding-left: 5px;\n"
            "    padding-top: 5px;\n"
            "    background-color: rgba(105, 118, 132, 200);\n"
            "}"
        )
        self.update_button.setObjectName("update_patient_button")
        self.gridLayout.addWidget(self.frame_7, 4, 0, 1, 1)
        self.form_frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
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
        self.first_name_label.setGeometry(QtCore.QRect(110, 90, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.first_name_label.setFont(font)
        self.first_name_label.setStyleSheet("color: rgba(255, 255, 255, 210);")
        self.first_name_label.setObjectName("first_name_label")
        self.first_name_input = QtWidgets.QLineEdit(self.form_frame)
        self.first_name_input.setGeometry(QtCore.QRect(250, 90, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.first_name_input.setFont(font)
        self.first_name_input.setText("")
        self.first_name_input.setAlignment(QtCore.Qt.AlignCenter)
        self.first_name_input.setObjectName("first_name_input")
        self.last_name_label = QtWidgets.QLabel(self.form_frame)
        self.last_name_label.setGeometry(QtCore.QRect(570, 90, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.last_name_label.setFont(font)
        self.last_name_label.setStyleSheet("color: rgba(255, 255, 255, 210);")
        self.last_name_label.setObjectName("last_name_label")
        self.last_name_input = QtWidgets.QLineEdit(self.form_frame)
        self.last_name_input.setGeometry(QtCore.QRect(710, 90, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.last_name_input.setFont(font)
        self.last_name_input.setText("")
        self.last_name_input.setAlignment(QtCore.Qt.AlignCenter)
        self.last_name_input.setObjectName("last_name_input")
        self.patient_label = QtWidgets.QLabel(self.form_frame)
        self.patient_label.setGeometry(QtCore.QRect(340, 0, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.patient_label.setFont(font)
        self.patient_label.setStyleSheet("color: rgba(255, 255, 255, 210);")
        self.patient_label.setObjectName("patient_label")
        self.patient_input = QtWidgets.QLineEdit(self.form_frame)
        self.patient_input.setGeometry(QtCore.QRect(450, 0, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.patient_input.setFont(font)
        self.patient_input.setText("")
        self.patient_input.setAlignment(QtCore.Qt.AlignCenter)
        self.patient_input.setObjectName("patient_input")
        self.search_button = QtWidgets.QPushButton(self.form_frame)
        self.search_button.setGeometry(QtCore.QRect(700, 0, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.search_button.setFont(font)
        self.search_button.setStyleSheet(
            "QPushButton#search_button {\n"
            "    border-image: none;\n"
            "    background-color: qconicalgradient(cx:0.5,"
            " cy:0.5, angle:45, stop:0 rgba(85, 98, 112, 226),"
            " stop:0.5 rgba(20, 47, 78, 219), stop:1 "
            "rgba(85, 98, 112, 226));\n"
            "    color: rgba(255, 255, 255, 210);\n"
            "    border-radius: 5px;\n"
            "}\n"
            "\n"
            "QPushButton#search_button:hover {\n"
            "    background-color: qconicalgradient(cx:0.5,"
            " cy:0.5, angle:45, stop:0 rgba(105, 118, 132, 226),"
            " stop:0.5 rgba(40, 67, 98, 219), stop:1"
            " rgba(105, 118, 132, 226));\n"
            "}\n"
            "\n"
            "QPushButton#search_button:pressed {\n"
            "    padding-left: 5px;\n"
            "    padding-top: 5px;\n"
            "    background-color: rgba(105, 118, 132, 200);\n"
            "}"
        )
        self.search_button.setObjectName("search_button")
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
        self.email_input.setGeometry(QtCore.QRect(250, 30, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.email_input.setFont(font)
        self.email_input.setText("")
        self.email_input.setAlignment(QtCore.Qt.AlignCenter)
        self.email_input.setObjectName("email_input")
        self.email_label = QtWidgets.QLabel(self.time_frame)
        self.email_label.setGeometry(QtCore.QRect(110, 30, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.email_label.setFont(font)
        self.email_label.setStyleSheet("color: rgba(255, 255, 255, 210);")
        self.email_label.setObjectName("email_label")
        self.phone_number = QtWidgets.QLabel(self.time_frame)
        self.phone_number.setGeometry(QtCore.QRect(570, 30, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.phone_number.setFont(font)
        self.phone_number.setStyleSheet("color: rgba(255, 255, 255, 210);")
        self.phone_number.setObjectName("phone_number")
        self.phone_number_input = QtWidgets.QLineEdit(self.time_frame)
        self.phone_number_input.setGeometry(QtCore.QRect(710, 30, 271, 51))
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
        self.username_input = QtWidgets.QLineEdit(self.last_name)
        self.username_input.setGeometry(QtCore.QRect(250, 60, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.username_input.setFont(font)
        self.username_input.setText("")
        self.username_input.setAlignment(QtCore.Qt.AlignCenter)
        self.username_input.setObjectName("username_input")
        self.username_label = QtWidgets.QLabel(self.last_name)
        self.username_label.setGeometry(QtCore.QRect(110, 60, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.username_label.setFont(font)
        self.username_label.setStyleSheet("color: rgba(255, 255, 255, 210);")
        self.username_label.setObjectName("username_label")
        self.cpf_input = QtWidgets.QLineEdit(self.last_name)
        self.cpf_input.setGeometry(QtCore.QRect(710, 60, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.cpf_input.setFont(font)
        self.cpf_input.setText("")
        self.cpf_input.setAlignment(QtCore.Qt.AlignCenter)
        self.cpf_input.setObjectName("cpf_input")
        self.cpf_label = QtWidgets.QLabel(self.last_name)
        self.cpf_label.setGeometry(QtCore.QRect(570, 60, 141, 41))
        self.cpf_input.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cpf_label.setFont(font)
        self.cpf_label.setStyleSheet("color: rgba(255, 255, 255, 210);")
        self.cpf_label.setObjectName("cpf_label")
        self.gridLayout.addWidget(self.last_name, 2, 0, 1, 1)
        self.window.setCentralWidget(self.centralwidget)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.window)
        self.search_button.clicked.connect(self.on_search_click)
        self.update_button.clicked.connect(self.on_update_click)
        self.window.show()

    def on_search_click(self):
        try:
            patient_id = self.patient_input.text()
            int(patient_id)
        except ValueError:
            title, text = 'Error', 'Invalid Patient ID'
            self.clear_fields()
            self.show_error_message(title, text)
        else:
            data = retrieve_patient_details(
                self.url, self.access_token, patient_id)
            if not data:
                title, text = 'Error', 'Patient not found'
                self.clear_fields()
                self.show_error_message(title, text)
            else:
                self.first_name_input.setText(data.get('first_name'))
                self.last_name_input.setText(data.get('last_name'))
                self.username_input.setText(data.get('username'))
                self.email_input.setText(data.get('email'))
                self.phone_number_input.setText(data.get('phone_number'))
                self.cpf_input.setText(data.get('cpf'))
                self.current_patient = patient_id

    def on_update_click(self):
        if not self.current_patient:
            self.show_error_message('Error', 'Please search a patient first')
            return
        first_name = self.first_name_input.text()
        last_name = self.last_name_input.text()
        username = self.username_input.text()
        email = self.email_input.text()
        phone_number = self.phone_number_input.text()
        if not all([first_name, last_name, username, email]):
            title, text = 'Error', 'Please fill all required fields'
            self.show_error_message(title, text)
        else:
            data = {
                "username": username,
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "phone_number": phone_number,
            }
            update_patient(
                self.url, self.access_token, data, self.current_patient)

    def show_error_message(self, title, text):
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

    def clear_fields(self):
        self.first_name_input.setText('')
        self.last_name_input.setText('')
        self.username_input.setText('')
        self.email_input.setText('')
        self.phone_number_input.setText('')
        self.cpf_input.setText('')
        self.current_patient = None

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.window.setWindowTitle(_translate("MainWindow", "OdontoDj"))
        self.title.setText(_translate("MainWindow", "Update Patient Details"))
        self.update_button.setText(_translate("MainWindow", "Update"))
        self.first_name_label.setText(_translate("MainWindow", "First Name"))
        self.last_name_label.setText(_translate("MainWindow", "Last Name"))
        self.patient_label.setText(_translate("MainWindow", "Patient"))
        self.search_button.setText(_translate("MainWindow", "Search"))
        self.email_label.setText(_translate("MainWindow", "Email"))
        self.phone_number.setText(_translate("MainWindow", "Phone Number"))
        self.username_label.setText(_translate("MainWindow", "Username"))
        self.cpf_label.setText(_translate("MainWindow", "CPF"))
