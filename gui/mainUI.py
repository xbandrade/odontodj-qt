from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout

import gui.main.res  # noqa
from gui.add_patientUI import AddPatientUI
from gui.datetimesUI import DateTimesUI
from gui.historyUI import HistoryUI
from gui.scheduleUI import ScheduleUI
from gui.update_patientUI import UpdatePatientUI
from gui.update_procedureUI import UpdateProcedureUI
from navigator import navigate_to_login_page
from window import CustomNewWindow


class MainUI(QtWidgets.QWidget):
    def __init__(self, parent=None, username='NONE', url='', access_token=''):
        super().__init__(parent)
        self.url = url
        self.access_token = access_token
        self.window = parent
        self.username = username
        self.setupUi()

    def setupUi(self):
        self.window.switch_to_framed()
        self.widget = QtWidgets.QWidget(self.window)
        self.widget.setFixedSize(1121, 761)
        self.widget.setObjectName('widget')
        self.layout = QVBoxLayout(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 1120, 760))
        self.widget_2.setStyleSheet(
            "border-image: url(:/newPrefix/images/app_bg.jpg);"
        )
        self.widget_2.setObjectName('widget_2')
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(10, 10, 91, 91))
        self.label.setStyleSheet(
            "border-image: url(:/newPrefix/images/od_logo.png);"
        )
        self.label.setText('')
        self.label.setObjectName('label')
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(420, 0, 551, 81))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(
            "border-image: none;\n"
            "color: rgba(255, 255, 255, 210);"
        )
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName('label_2')
        self.logout_button = QtWidgets.QPushButton(self.widget_2)
        self.logout_button.setGeometry(QtCore.QRect(970, 20, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.logout_button.setFont(font)
        self.logout_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.logout_button.setStyleSheet(
            "QPushButton#logoutButton{\n"
            "    border-image: none;\n"
            "background-color: qconicalgradient(cx:0.5, cy:0.5, angle:45,"
            "stop:0 rgba(85, 98, 112, 226), stop:0.5 rgba(20, 47, 78, 219),"
            "stop:1 rgba(85, 98, 112, 226));"
            "    color: rgba(255, 55, 55, 210);\n"
            "    border-radius: 5px;    \n"
            "}\n"
            "QPushButton#logoutButton:hover{\n"
            "    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:45,"
            "stop:0 rgba(105, 118, 132, 226), stop:0.5 rgba(40, 67, 98, 219),"
            "stop:1 rgba(105, 118, 132, 226));"
            "}\n"
            "QPushButton#logoutButton:pressed{\n"
            "    padding-left:5px;\n"
            "    padding-top:5px;\n"
            "    background-color: rgba(105, 118, 132, 200);\n"
            "}\n"
            ""
        )
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
        self.logout_button.setObjectName('logoutButton')
        self.calendarWidget = QtWidgets.QCalendarWidget(self.widget_2)
        self.calendarWidget.setGeometry(QtCore.QRect(470, 130, 631, 601))
        self.calendarWidget.setStyleSheet(
            "border-image: none;"
        )
        self.calendarWidget.setObjectName('calendarWidget')
        self.schedule_button = QtWidgets.QPushButton(self.widget_2)
        self.schedule_button.setGeometry(QtCore.QRect(10, 150, 211, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.schedule_button.setFont(font)
        self.schedule_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.schedule_button.setStyleSheet(
            "QPushButton#scheduleButton" + button_style +
            "QPushButton#scheduleButton:hover" + hover_style +
            "QPushButton#scheduleButton:pressed" + pressed_style
        )
        self.schedule_button.setObjectName('scheduleButton')
        self.update_appointment_button = QtWidgets.QPushButton(self.widget_2)
        self.update_appointment_button.setGeometry(
            QtCore.QRect(10, 270, 211, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.update_appointment_button.setFont(font)
        self.update_appointment_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.update_appointment_button.setStyleSheet(
            "QPushButton#updateScheduleButton" + button_style +
            "QPushButton#updateScheduleButton:hover" + hover_style +
            "QPushButton#updateScheduleButton:pressed" + pressed_style
        )
        self.update_appointment_button.setObjectName('updateScheduleButton')
        self.custom_schedule_button = QtWidgets.QPushButton(self.widget_2)
        self.custom_schedule_button.setGeometry(
            QtCore.QRect(10, 390, 211, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.custom_schedule_button.setFont(font)
        self.custom_schedule_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.custom_schedule_button.setStyleSheet(
            "QPushButton#customScheduleButton" + button_style +
            "QPushButton#customScheduleButton:hover" + hover_style +
            "QPushButton#customScheduleButton:pressed" + pressed_style
        )
        self.custom_schedule_button.setObjectName('customScheduleButton')
        self.next_appointments_button = QtWidgets.QPushButton(self.widget_2)
        self.next_appointments_button.setGeometry(
            QtCore.QRect(10, 510, 211, 101)
        )
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.next_appointments_button.setFont(font)
        self.next_appointments_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.next_appointments_button.setStyleSheet(
            "QPushButton#nextAppointmentsButton" + button_style +
            "QPushButton#nextAppointmentsButton:hover" + hover_style +
            "QPushButton#nextAppointmentsButton:pressed" + pressed_style
        )
        self.next_appointments_button.setObjectName('nextAppointmentsButton')
        self.update_patient_button = QtWidgets.QPushButton(self.widget_2)
        self.update_patient_button.setGeometry(
            QtCore.QRect(240, 270, 211, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.update_patient_button.setFont(font)
        self.update_patient_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.update_patient_button.setStyleSheet(
            "QPushButton#patientDetailsButton" + button_style +
            "QPushButton#patientDetailsButton:hover" + hover_style +
            "QPushButton#patientDetailsButton:pressed" + pressed_style
        )
        self.update_patient_button.setObjectName("patientDetailsButton")
        self.add_patient_button = QtWidgets.QPushButton(self.widget_2)
        self.add_patient_button.setGeometry(QtCore.QRect(240, 150, 211, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.add_patient_button.setFont(font)
        self.add_patient_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.add_patient_button.setStyleSheet(
            "QPushButton#addPatientButton" + button_style +
            "QPushButton#addPatientButton:hover" + hover_style +
            "QPushButton#addPatientButton:pressed" + pressed_style
        )
        self.add_patient_button.setObjectName("addPatientButton")
        self.patient_history_button = QtWidgets.QPushButton(self.widget_2)
        self.patient_history_button.setGeometry(
            QtCore.QRect(240, 390, 211, 101)
        )
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.patient_history_button.setFont(font)
        self.patient_history_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.patient_history_button.setStyleSheet(
            "QPushButton#patientHistoryButton" + button_style +
            "QPushButton#patientHistoryButton:hover" + hover_style +
            "QPushButton#patientHistoryButton:pressed" + pressed_style
        )
        self.patient_history_button.setObjectName("patientHistoryButton")
        self.available_times_button = QtWidgets.QPushButton(self.widget_2)
        self.available_times_button.setGeometry(
            QtCore.QRect(240, 510, 211, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.available_times_button.setFont(font)
        self.available_times_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.available_times_button.setStyleSheet(
            "QPushButton#availableTimesButton" + button_style +
            "QPushButton#availableTimesButton:hover" + hover_style +
            "QPushButton#availableTimesButton:pressed" + pressed_style
        )
        self.available_times_button.setObjectName("availableTimesButton")
        self.send_results_button = QtWidgets.QPushButton(self.widget_2)
        self.send_results_button.setGeometry(QtCore.QRect(240, 630, 211, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.send_results_button.setFont(font)
        self.send_results_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.send_results_button.setStyleSheet(
            "QPushButton#sendResultsButton" + button_style +
            "QPushButton#sendResultsButton:hover" + hover_style +
            "QPushButton#sendResultsButton:pressed" + pressed_style
        )
        self.send_results_button.setObjectName("sendResultsButton")
        self.update_procedure_button = QtWidgets.QPushButton(self.widget_2)
        self.update_procedure_button.setGeometry(
            QtCore.QRect(10, 630, 211, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.update_procedure_button.setFont(font)
        self.update_procedure_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.update_procedure_button.setStyleSheet(
            "QPushButton#updateProceduresButton" + button_style +
            "QPushButton#updateProceduresButton:hover" + hover_style +
            "QPushButton#updateProceduresButton:pressed" + pressed_style
        )
        self.update_procedure_button.setObjectName("updateProceduresButton")
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.window)
        self.patient_history_button.clicked.connect(self.on_history_click)
        self.schedule_button.clicked.connect(self.on_schedule_click)
        self.add_patient_button.clicked.connect(self.on_add_patient_click)
        self.update_patient_button.clicked.connect(
            self.on_update_patient_click)
        self.logout_button.clicked.connect(self.on_logout)
        self.update_procedure_button.clicked.connect(
            self.on_update_procedure_click)
        self.available_times_button.clicked.connect(
            self.on_available_times_click)
        self.send_results_button.setEnabled(False)
        self.update_appointment_button.setEnabled(False)
        self.custom_schedule_button.setEnabled(False)
        self.next_appointments_button.setEnabled(False)

    def on_logout(self):
        navigate_to_login_page(self.window)

    def on_history_click(self):
        new_window = CustomNewWindow()
        history_ui = HistoryUI(new_window, self)
        new_window.setCentralWidget(history_ui.centralwidget)
        new_window.show()

    def on_add_patient_click(self):
        new_window = CustomNewWindow()
        add_patient_ui = AddPatientUI(new_window, self)
        new_window.setCentralWidget(add_patient_ui.centralwidget)
        new_window.show()

    def on_update_patient_click(self):
        new_window = CustomNewWindow()
        update_patient_ui = UpdatePatientUI(new_window, self)
        new_window.setCentralWidget(update_patient_ui.centralwidget)
        new_window.show()

    def on_update_procedure_click(self):
        new_window = CustomNewWindow()
        update_procedure_ui = UpdateProcedureUI(new_window, self)
        new_window.setCentralWidget(update_procedure_ui.centralwidget)
        new_window.show()

    def on_schedule_click(self):
        new_window = CustomNewWindow()
        schedule_ui = ScheduleUI(new_window, self)
        new_window.setCentralWidget(schedule_ui.centralwidget)
        new_window.show()

    def on_available_times_click(self):
        new_window = CustomNewWindow()
        available_times_ui = DateTimesUI(new_window, self)
        new_window.setCentralWidget(available_times_ui.centralwidget)
        new_window.show()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.window.setWindowTitle(_translate('Form', 'OdontoDj'))
        self.label_2.setText(_translate(
            'Form', f"You're logged in as {self.username}"))
        self.logout_button.setText(_translate(
            'Form', 'Logout'))
        self.schedule_button.setText(_translate(
            'Form', 'New Appointment'))
        self.update_appointment_button.setText(_translate(
            'Form', 'Update Appointment'))
        self.custom_schedule_button.setText(_translate(
            'Form', 'Custom Appointment'))
        self.next_appointments_button.setText(_translate(
            'Form', 'Next Appointments'))
        self.update_patient_button.setText(_translate(
            'Form', 'Patient Details'))
        self.add_patient_button.setText(_translate(
            'Form', 'Add New Patient'))
        self.patient_history_button.setText(_translate(
            'Form', 'Patient History'))
        self.available_times_button.setText(_translate(
            'Form', 'Available Times'))
        self.send_results_button.setText(_translate(
            'Form', 'Send Procedure Results'))
        self.update_procedure_button.setText(_translate(
            'Form', 'Update Procedures'))
