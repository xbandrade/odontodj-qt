from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout

import gui.main.res  # noqa
from historyUI import HistoryUI
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
        # self.widget.setGeometry(QtCore.QRect(0, 0, 1121, 761))
        self.widget.setFixedSize(1121, 761)
        self.widget.setObjectName('widget')
        # flags = self.window.windowFlags()
        # flags &= ~Qt.WindowMaximizeButtonHint
        # self.window.setWindowFlags(flags)
        self.layout = QVBoxLayout(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 1121, 761))
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
        self.logoutButton = QtWidgets.QPushButton(self.widget_2)
        self.logoutButton.setGeometry(QtCore.QRect(970, 20, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.logoutButton.setFont(font)
        self.logoutButton.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.logoutButton.setStyleSheet(
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
        self.logoutButton.setObjectName('logoutButton')
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
        self.updateScheduleButton = QtWidgets.QPushButton(self.widget_2)
        self.updateScheduleButton.setGeometry(QtCore.QRect(10, 270, 211, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.updateScheduleButton.setFont(font)
        self.updateScheduleButton.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.updateScheduleButton.setStyleSheet(
            "QPushButton#updateScheduleButton" + button_style +
            "QPushButton#updateScheduleButton:hover" + hover_style +
            "QPushButton#updateScheduleButton:pressed" + pressed_style
        )
        self.updateScheduleButton.setObjectName('updateScheduleButton')
        self.customScheduleButton = QtWidgets.QPushButton(self.widget_2)
        self.customScheduleButton.setGeometry(QtCore.QRect(10, 390, 211, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.customScheduleButton.setFont(font)
        self.customScheduleButton.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.customScheduleButton.setStyleSheet(
            "QPushButton#customScheduleButton" + button_style +
            "QPushButton#customScheduleButton:hover" + hover_style +
            "QPushButton#customScheduleButton:pressed" + pressed_style
        )
        self.customScheduleButton.setObjectName('customScheduleButton')
        self.nextAppointmentsButton = QtWidgets.QPushButton(self.widget_2)
        self.nextAppointmentsButton.setGeometry(
            QtCore.QRect(10, 510, 211, 101)
        )
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.nextAppointmentsButton.setFont(font)
        self.nextAppointmentsButton.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.nextAppointmentsButton.setStyleSheet(
            "QPushButton#nextAppointmentsButton" + button_style +
            "QPushButton#nextAppointmentsButton:hover" + hover_style +
            "QPushButton#nextAppointmentsButton:pressed" + pressed_style
        )
        self.nextAppointmentsButton.setObjectName('nextAppointmentsButton')
        self.patientDetailsButton = QtWidgets.QPushButton(self.widget_2)
        self.patientDetailsButton.setGeometry(QtCore.QRect(240, 270, 211, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.patientDetailsButton.setFont(font)
        self.patientDetailsButton.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.patientDetailsButton.setStyleSheet(
            "QPushButton#patientDetailsButton" + button_style +
            "QPushButton#patientDetailsButton:hover" + hover_style +
            "QPushButton#patientDetailsButton:pressed" + pressed_style
        )
        self.patientDetailsButton.setObjectName("patientDetailsButton")
        self.addPatientButton = QtWidgets.QPushButton(self.widget_2)
        self.addPatientButton.setGeometry(QtCore.QRect(240, 150, 211, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.addPatientButton.setFont(font)
        self.addPatientButton.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.addPatientButton.setStyleSheet(
            "QPushButton#addPatientButton" + button_style +
            "QPushButton#addPatientButton:hover" + hover_style +
            "QPushButton#addPatientButton:pressed" + pressed_style
        )
        self.addPatientButton.setObjectName("addPatientButton")
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
        self.availableTimesButton = QtWidgets.QPushButton(self.widget_2)
        self.availableTimesButton.setGeometry(QtCore.QRect(240, 510, 211, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.availableTimesButton.setFont(font)
        self.availableTimesButton.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.availableTimesButton.setStyleSheet(
            "QPushButton#availableTimesButton" + button_style +
            "QPushButton#availableTimesButton:hover" + hover_style +
            "QPushButton#availableTimesButton:pressed" + pressed_style
        )
        self.availableTimesButton.setObjectName("availableTimesButton")
        self.sendResultsButton = QtWidgets.QPushButton(self.widget_2)
        self.sendResultsButton.setGeometry(QtCore.QRect(240, 630, 211, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sendResultsButton.setFont(font)
        self.sendResultsButton.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.sendResultsButton.setStyleSheet(
            "QPushButton#sendResultsButton" + button_style +
            "QPushButton#sendResultsButton:hover" + hover_style +
            "QPushButton#sendResultsButton:pressed" + pressed_style
        )
        self.sendResultsButton.setObjectName("sendResultsButton")
        self.updateProceduresButton = QtWidgets.QPushButton(self.widget_2)
        self.updateProceduresButton.setGeometry(
            QtCore.QRect(10, 630, 211, 101)
        )
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.updateProceduresButton.setFont(font)
        self.updateProceduresButton.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.updateProceduresButton.setStyleSheet(
            "QPushButton#updateProceduresButton" + button_style +
            "QPushButton#updateProceduresButton:hover" + hover_style +
            "QPushButton#updateProceduresButton:pressed" + pressed_style
        )
        self.updateProceduresButton.setObjectName("updateProceduresButton")
        # self.add_widgets_to_layout()
        # self.widget.setLayout(self.layout)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.window)
        self.patient_history_button.clicked.connect(self.on_history_click)
        self.logoutButton.clicked.connect(self.on_logout)

    def on_logout(self):
        navigate_to_login_page(self.window)

    def on_history_click(self):
        new_window = CustomNewWindow()
        history_ui = HistoryUI(new_window, self)
        new_window.setCentralWidget(history_ui.widget)
        new_window.show()

    def add_widgets_to_layout(self):
        self.layout.addWidget(self.widget_2)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.label_2)
        self.layout.addWidget(self.logoutButton)
        self.layout.addWidget(self.calendarWidget)
        self.layout.addWidget(self.schedule_button)
        self.layout.addWidget(self.updateScheduleButton)
        self.layout.addWidget(self.customScheduleButton)
        self.layout.addWidget(self.nextAppointmentsButton)
        self.layout.addWidget(self.patientDetailsButton)
        self.layout.addWidget(self.addPatientButton)
        self.layout.addWidget(self.patient_history_button)
        self.layout.addWidget(self.availableTimesButton)
        self.layout.addWidget(self.sendResultsButton)
        self.layout.addWidget(self.updateProceduresButton)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.window.setWindowTitle(_translate('Form', 'OdontoDj'))
        self.label_2.setText(_translate(
            'Form', f"You're logged in as {self.username}"
        ))
        self.logoutButton.setText(_translate(
            'Form', 'Logout'
        ))
        self.schedule_button.setText(_translate(
            'Form', 'New Appointment'
        ))
        self.updateScheduleButton.setText(_translate(
            'Form', 'Update Appointment'
        ))
        self.customScheduleButton.setText(_translate(
            'Form', 'Custom Appointment'
        ))
        self.nextAppointmentsButton.setText(_translate(
            'Form', 'Next Appointments'
        ))
        self.patientDetailsButton.setText(_translate(
            'Form', 'Patient Details'
        ))
        self.addPatientButton.setText(_translate(
            'Form', 'Add New Patient'
        ))
        self.patient_history_button.setText(_translate(
            'Form', 'Patient History'
        ))
        self.availableTimesButton.setText(_translate(
            'Form', 'Available Times'
        ))
        self.sendResultsButton.setText(_translate(
            'Form', 'Send Procedure Results'
        ))
        self.updateProceduresButton.setText(_translate(
            'Form', 'Update Procedures'
        ))
