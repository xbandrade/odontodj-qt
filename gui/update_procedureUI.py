from PyQt5 import QtCore, QtGui, QtWidgets

import gui.main.res  # noqa
from api_connect import retrieve_procedure_details, update_procedure


class UpdateProcedureUI(QtWidgets.QWidget):
    def __init__(self, parent=None, main_app=None):
        super().__init__(parent)
        self.access_token = main_app.access_token
        self.username = main_app.username
        self.url = main_app.url
        self.window = parent
        self.current_procedure = None
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
        self.description_label = QtWidgets.QLabel(self.form_frame)
        self.description_label.setGeometry(QtCore.QRect(90, 10, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.description_label.setFont(font)
        self.description_label.setStyleSheet(
            "color: rgba(255, 255, 255, 210);")
        self.description_label.setObjectName("description_label")
        self.description_pt_label = QtWidgets.QLabel(self.form_frame)
        self.description_pt_label.setGeometry(QtCore.QRect(570, 10, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.description_pt_label.setFont(font)
        self.description_pt_label.setStyleSheet(
            "color: rgba(255, 255, 255, 210);")
        self.description_pt_label.setObjectName("description_pt_label")
        self.description_input = QtWidgets.QTextEdit(self.form_frame)
        self.description_input.setGeometry(QtCore.QRect(230, 20, 271, 231))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.description_input.setFont(font)
        self.description_input.setObjectName("description_input")
        self.update_procedure_button = QtWidgets.QPushButton(self.form_frame)
        self.update_procedure_button.setGeometry(
            QtCore.QRect(720, 280, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.update_procedure_button.setFont(font)
        self.update_procedure_button.setStyleSheet(
            "QPushButton#update_procedure_button {\n"
            "    border-image: none;\n"
            "    background-color: qconicalgradient(cx:0.5,"
            " cy:0.5, angle:45, stop:0 rgba(85, 98, 112, 226),"
            " stop:0.5 rgba(20, 47, 78, 219), stop:1 "
            "rgba(85, 98, 112, 226));\n"
            "    color: rgba(255, 255, 255, 210);\n"
            "    border-radius: 5px;\n"
            "}\n"
            "\n"
            "QPushButton#update_procedure_button:hover {\n"
            "    background-color: qconicalgradient(cx:0.5,"
            " cy:0.5, angle:45, stop:0 rgba(105, 118, 132, 226),"
            " stop:0.5 rgba(40, 67, 98, 219), stop:1"
            " rgba(105, 118, 132, 226));\n"
            "}\n"
            "\n"
            "QPushButton#update_procedure_button:pressed {\n"
            "    padding-left: 5px;\n"
            "    padding-top: 5px;\n"
            "    background-color: rgba(105, 118, 132, 200);\n"
            "}"
        )
        self.update_procedure_button.setObjectName("update_procedure_button")
        self.description_pt_input = QtWidgets.QTextEdit(self.form_frame)
        self.description_pt_input.setGeometry(QtCore.QRect(720, 20, 271, 231))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.description_pt_input.setFont(font)
        self.description_pt_input.setObjectName("description_pt_input")
        self.price_label = QtWidgets.QLabel(self.form_frame)
        self.price_label.setGeometry(QtCore.QRect(100, 290, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.price_label.setFont(font)
        self.price_label.setStyleSheet("color: rgba(255, 255, 255, 210);")
        self.price_label.setObjectName("price_label")
        self.price_input = QtWidgets.QLineEdit(self.form_frame)
        self.price_input.setGeometry(QtCore.QRect(230, 290, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.price_input.setFont(font)
        self.price_input.setText("")
        self.price_input.setAlignment(QtCore.Qt.AlignCenter)
        self.price_input.setObjectName("price_input")
        self.gridLayout.addWidget(self.form_frame, 1, 0, 1, 1)
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
        self.title.setGeometry(QtCore.QRect(350, 20, 561, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet("color: rgba(255, 255, 255, 210);")
        self.title.setObjectName("title")
        self.search_button = QtWidgets.QPushButton(self.logo_frame)
        self.search_button.setGeometry(QtCore.QRect(630, 140, 101, 51))
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
        self.procedure_input = QtWidgets.QLineEdit(self.logo_frame)
        self.procedure_input.setGeometry(QtCore.QRect(530, 140, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.procedure_input.setFont(font)
        self.procedure_input.setText("")
        self.procedure_input.setAlignment(QtCore.Qt.AlignCenter)
        self.procedure_input.setObjectName("procedure_input")
        self.procedure_label = QtWidgets.QLabel(self.logo_frame)
        self.procedure_label.setGeometry(QtCore.QRect(330, 140, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.procedure_label.setFont(font)
        self.procedure_label.setStyleSheet("color: rgba(255, 255, 255, 210);")
        self.procedure_label.setObjectName("procedure_label")
        self.name_label = QtWidgets.QLabel(self.logo_frame)
        self.name_label.setGeometry(QtCore.QRect(100, 250, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.name_label.setFont(font)
        self.name_label.setStyleSheet("color: rgba(255, 255, 255, 210);")
        self.name_label.setObjectName("name_label")
        self.name_input = QtWidgets.QLineEdit(self.logo_frame)
        self.name_input.setGeometry(QtCore.QRect(230, 250, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.name_input.setFont(font)
        self.name_input.setText("")
        self.name_input.setAlignment(QtCore.Qt.AlignCenter)
        self.name_input.setObjectName("name_input")
        self.name_pt_label = QtWidgets.QLabel(self.logo_frame)
        self.name_pt_label.setGeometry(QtCore.QRect(580, 250, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.name_pt_label.setFont(font)
        self.name_pt_label.setStyleSheet("color: rgba(255, 255, 255, 210);")
        self.name_pt_label.setObjectName("name_pt_label")
        self.name_pt_input = QtWidgets.QLineEdit(self.logo_frame)
        self.name_pt_input.setGeometry(QtCore.QRect(720, 250, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.name_pt_input.setFont(font)
        self.name_pt_input.setText("")
        self.name_pt_input.setAlignment(QtCore.Qt.AlignCenter)
        self.name_pt_input.setObjectName("name_pt_input")
        self.gridLayout.addWidget(self.logo_frame, 0, 0, 1, 2)
        self.window.setCentralWidget(self.centralwidget)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.window)
        self.search_button.clicked.connect(self.on_search_click)
        self.update_procedure_button.clicked.connect(
            self.on_update_click)
        self.window.show()

    def on_search_click(self):
        try:
            procedure_id = self.procedure_input.text()
            int(procedure_id)
        except ValueError:
            title, text = 'Error', 'Invalid Procedure ID'
            self.clear_fields()
            self.show_message_box(title, text)
        else:
            data = retrieve_procedure_details(
                self.url, self.access_token, procedure_id)
            if not data:
                title, text = 'Error', 'Procedure not found'
                self.clear_fields()
                self.show_message_box(title, text)
            else:
                self.name_input.setText(data.get('name'))
                self.name_pt_input.setText(data.get('name_pt'))
                self.description_input.setText(data.get('description'))
                self.description_input.setText(data.get('description'))
                self.description_pt_input.setText(
                    data.get('description_pt'))
                self.price_input.setText(data.get('price'))
                self.current_procedure = procedure_id

    def on_update_click(self):
        if not self.current_procedure:
            self.show_message_box(
                'Error', 'Please search a procedure first')
            return
        name = self.name_input.text()
        name_pt = self.name_pt_input.text()
        description = self.description_input.toPlainText()
        description_pt = self.description_pt_input.toPlainText()
        price = self.price_input.text()
        if not all([name, name_pt, description, description_pt, price]):
            title, text = 'Error', 'Please fill all required fields'
            self.show_message_box(title, text)
        else:
            data = {
                "name": name,
                "name_pt": name_pt,
                "description": description,
                "description_pt": description_pt,
                "price": price,
            }
            update_procedure(
                self.url, self.access_token, data, self.current_procedure)
            self.show_message_box(
                'Success', 'Procedure updated successfully')
            return

    def show_message_box(self, title, text):
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
        self.name_input.setText('')
        self.name_pt_input.setText('')
        self.description_input.setText('')
        self.description_pt_input.setText('')
        self.price_input.setText('')
        self.current_procedure = None

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.window.setWindowTitle(_translate("MainWindow", "OdontoDj"))
        self.description_label.setText(_translate("MainWindow", "Description"))
        self.description_pt_label.setText(_translate(
            "MainWindow", "Description PT-BR"))
        self.update_procedure_button.setText(_translate(
            "MainWindow", "Update"))
        self.price_label.setText(_translate("MainWindow", "Price"))
        self.title.setText(_translate(
            "MainWindow", "Update Procedure Details"))
        self.search_button.setText(_translate("MainWindow", "Search"))
        self.procedure_label.setText(_translate("MainWindow", "Procedure ID"))
        self.name_label.setText(_translate("MainWindow", "Name"))
        self.name_pt_label.setText(_translate("MainWindow", "Name PT-BR"))
