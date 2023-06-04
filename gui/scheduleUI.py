from PyQt5 import QtCore, QtGui, QtWidgets

import gui.main.res  # noqa
from api_connect import (retrieve_datetimes, retrieve_procedures,
                         schedule_appointment)


class CenteredDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignCenter

    def createEditor(self, parent, option, index):
        return None


class ScheduleUI(QtWidgets.QWidget):
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
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.window.sizePolicy().hasHeightForWidth()
        )
        self.window.setSizePolicy(sizePolicy)
        self.window.setStyleSheet(
            "border-image: url(:/newPrefix/images/app_bg.jpg);"
        )
        self.centralwidget = QtWidgets.QWidget(self.window)
        self.centralwidget.setFixedSize(1120, 760)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.logo_frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.logo_frame.sizePolicy().hasHeightForWidth()
        )
        self.logo_frame.setSizePolicy(sizePolicy)
        self.logo_frame.setStyleSheet("border-image: none;")
        self.logo_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo_frame.setObjectName("logo_frame")
        self.logo = QtWidgets.QLabel(self.logo_frame)
        self.logo.setGeometry(QtCore.QRect(10, 10, 91, 91))
        self.logo.setStyleSheet(
            "border-image: url(:/newPrefix/images/od_logo.png);"
        )
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.title = QtWidgets.QLabel(self.logo_frame)
        self.title.setGeometry(QtCore.QRect(320, 30, 481, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet("color: rgba(255, 255, 255, 210);")
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.logo_frame, 0, 0, 1, 2)
        self.procedure_frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.procedure_frame.sizePolicy().hasHeightForWidth()
        )
        self.procedure_frame.setSizePolicy(sizePolicy)
        self.procedure_frame.setStyleSheet("border-image: none;")
        self.procedure_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.procedure_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.procedure_frame.setObjectName("procedure_frame")
        self.procedures = QtWidgets.QComboBox(self.procedure_frame)
        self.procedures.setGeometry(QtCore.QRect(310, 80, 221, 41))
        self.procedures.setObjectName("procedures")
        procedures = retrieve_procedures(self.url, self.access_token)
        procedures = [procedure['name'] for procedure in procedures]
        items = procedures or ['------']
        self.procedures.addItems(items)
        self.procedure_label = QtWidgets.QLabel(self.procedure_frame)
        self.procedure_label.setGeometry(QtCore.QRect(170, 80, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.procedure_label.setFont(font)
        self.procedure_label.setStyleSheet("color: rgba(255, 255, 255, 210);")
        self.procedure_label.setObjectName("procedure_label")
        self.gridLayout.addWidget(self.procedure_frame, 1, 0, 1, 1)
        self.list_frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.list_frame.sizePolicy().hasHeightForWidth()
        )
        self.list_frame.setSizePolicy(sizePolicy)
        self.list_frame.setStyleSheet("border-image: none;")
        self.list_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.list_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.list_frame.setObjectName("list_frame")
        self.listView = QtWidgets.QListView(self.list_frame)
        self.listView.setGeometry(QtCore.QRect(140, 70, 311, 421))
        self.listView.setObjectName("listView")
        model = QtCore.QStringListModel()
        self.listView.setModel(model)
        delegate = CenteredDelegate(self.listView)
        self.listView.setItemDelegate(delegate)
        datetimes = retrieve_datetimes(self.url, self.access_token)
        self.listView.setStyleSheet(
            "background-color: rgba(195, 195, 195, 180);"
        )
        items = datetimes[:20] or ["No Available Times"]
        initial_datetime = items[0].split()
        year, month, day = map(int, initial_datetime[0].split('-'))
        initial_date = QtCore.QDate(year, month, day)
        hour, minute = map(int, initial_datetime[1].split(':'))
        initial_time = QtCore.QTime(hour, minute, 0)
        model.setStringList(items)
        self.list_label = QtWidgets.QLabel(self.list_frame)
        self.list_label.setGeometry(QtCore.QRect(180, 30, 311, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.list_label.setFont(font)
        self.list_label.setStyleSheet("color: rgba(255, 255, 255, 210);")
        self.list_label.setObjectName("list_label")
        self.gridLayout.addWidget(self.list_frame, 1, 1, 4, 1)
        self.date_frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.date_frame.sizePolicy().hasHeightForWidth()
        )
        self.date_frame.setSizePolicy(sizePolicy)
        self.date_frame.setStyleSheet("border-image: none;")
        self.date_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.date_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.date_frame.setObjectName("date_frame")
        self.date_label = QtWidgets.QLabel(self.date_frame)
        self.date_label.setGeometry(QtCore.QRect(170, 30, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.date_label.setFont(font)
        self.date_label.setStyleSheet("color: rgba(255, 255, 255, 210);")
        self.date_label.setObjectName("date_label")
        self.date_input = QtWidgets.QDateEdit(self.date_frame)
        self.date_input.setGeometry(QtCore.QRect(310, 30, 221, 51))
        self.date_input.setObjectName("date_input")
        self.date_input.setDate(initial_date)
        self.gridLayout.addWidget(self.date_frame, 2, 0, 1, 1)
        self.time_frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.time_frame.sizePolicy().hasHeightForWidth()
        )
        self.time_frame.setSizePolicy(sizePolicy)
        self.time_frame.setStyleSheet("border-image: none;")
        self.time_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.time_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.time_frame.setObjectName("time_frame")
        self.time_label = QtWidgets.QLabel(self.time_frame)
        self.time_label.setGeometry(QtCore.QRect(170, 0, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.time_label.setFont(font)
        self.time_label.setStyleSheet("color: rgba(255, 255, 255, 210);")
        self.time_label.setObjectName("time_label")
        self.time_input = QtWidgets.QTimeEdit(self.time_frame)
        self.time_input.setGeometry(QtCore.QRect(310, -10, 221, 51))
        self.time_input.setObjectName("timeEdit")
        self.time_input.setTime(initial_time)
        self.gridLayout.addWidget(self.time_frame, 3, 0, 1, 1)
        self.frame_7 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_7.sizePolicy().hasHeightForWidth()
        )
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setStyleSheet("border-image: none;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.schedule_button = QtWidgets.QPushButton(self.time_frame)
        self.schedule_button.setObjectName("pushButton")
        self.schedule_button.setGeometry(QtCore.QRect(240, 80, 211, 61))
        button_style = """
            {\nborder-image: none;\n
            background-color: qconicalgradient(cx:0.5, cy:0.5, angle:45,
            stop:0 rgba(85, 98, 112, 226), stop:0.5 rgba(20, 47, 78, 219),
            stop:1 rgba(85, 98, 112, 226));
            color: rgba(255, 255, 255, 210);\n
            border-radius: 5px;\n}\n
        """
        hover_style = """
            {\nbackground-color: qconicalgradient(cx:0.5, cy:0.5, angle:45,
            stop:0 rgba(105, 118, 132, 226), stop:0.5 rgba(40, 67, 98, 219),
            stop:1 rgba(105, 118, 132, 226));\n}\n
        """
        pressed_style = """
            {\npadding-left:5px;\n
            padding-top:5px;\n
            background-color: rgba(105, 118, 132, 200);\n}\n
        """
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.schedule_button.setFont(font)
        self.schedule_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.schedule_button.setStyleSheet(
            "QPushButton#pushButton" + button_style +
            "QPushButton#pushButton:hover" + hover_style +
            "QPushButton#pushButton:pressed" + pressed_style
        )
        self.gridLayout.addWidget(self.time_frame, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_7, 4, 0, 1, 1)
        self.window.setCentralWidget(self.centralwidget)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.window)
        self.schedule_button.clicked.connect(self.on_schedule_click)
        self.window.show()

    def on_schedule_click(self):
        procedure = self.procedures.currentText()
        date = self.date_input.date()
        time = self.time_input.time()
        date_str = date.toString("yyyy-MM-dd")
        time_str = time.toString("hh:mm:ss")
        message_box = QtWidgets.QMessageBox()
        if procedure == '' or date == QtCore.QDate() or time == QtCore.QTime():
            title, text = 'Error', 'Please fill in all fields'
        elif schedule_appointment(self.url, self.access_token,
                                  procedure, date_str, time_str):
            title, text = 'Success', 'Appointment scheduled successfully'
        else:
            title, text = 'Error', 'Failed to schedule appointment'
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
        self.centralwidget.show()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.window.setWindowTitle(_translate("MainWindow", "OdontoDj"))
        self.title.setText(_translate("MainWindow", "Schedule Appointment"))
        self.procedure_label.setText(_translate("MainWindow", "Procedure"))
        self.list_label.setText(_translate(
            "MainWindow", "Available Times"
        ))
        self.date_label.setText(_translate("MainWindow", "Date"))
        self.time_label.setText(_translate("MainWindow", "Time"))
        self.schedule_button.setText(_translate("MainWindow", "Schedule"))
