from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidget

import gui.main.res  # noqa


class HistoryUI(QtWidgets.QWidget):
    def __init__(self, parent=None, username='NONE'):
        super().__init__(parent)
        self.window = parent
        self.username = username
        self.setupUi()

    def setupUi(self):
        self.widget = QtWidgets.QWidget(self.window)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1121, 761))
        self.widget.setObjectName('widget')
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
        self.label_2.setGeometry(QtCore.QRect(10, 10, 1091, 81))
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
        self.appointment_banner = QtWidgets.QPushButton(self.widget_2)
        self.appointment_banner.setGeometry(QtCore.QRect(10, 150, 1101, 81))
        self.appointment_banner.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.appointment_banner.setFont(font)
        self.appointment_banner.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.appointment_banner.setStyleSheet(
            "QPushButton#scheduleButton{\n"
            "    border-image: none;\n"
            "    background-color: qlineargradient(spread:pad,x1:0,"
            " y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219),"
            " stop:1 rgba(85, 98, 112, 226));\n"
            "    color: rgba(255, 255, 255, 210);\n"
            "    border-radius: 5px;    \n"
            "}\n"
            "QPushButton#scheduleButton:hover{    \n"
            "    background-color: qlineargradient(spread:pad,x1:0,"
            " y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219),"
            " stop:1 rgba(105, 118, 132, 226));\n"
            "}\n"
            "QPushButton#scheduleButton:pressed{\n"
            "    padding-left:5px;\n"
            "    padding-top:5px;\n"
            "    background-color: rgba(105, 118, 132, 200);\n"
            "}\n"
            ""
        )
        self.appointment_banner.setObjectName('scheduleButton')
        self.tableWidget = QtWidgets.QTableWidget(self.widget_2)
        self.tableWidget.setGeometry(QtCore.QRect(50, 250, 1011, 101))
        self.tableWidget.setStyleSheet("border-image: none;")
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setObjectName('tableWidget')
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(126)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(49)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidget.setFocusPolicy(Qt.NoFocus)
        self.tableWidget.setSelectionMode(QTableWidget.NoSelection)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.window)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.window.setWindowTitle(_translate('Form', 'OdontoDj'))
        self.label_2.setText(_translate('Form', 'Patient History'))
        self.appointment_banner.setText(_translate(
            'Form', f"{self.username}'s Appointments")
        )
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate('Form', 'ID'))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate('Form', 'Procedure'))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate('Form', 'Date'))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate('Form', 'Time'))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate('Form', 'Price'))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate('Form', 'Confirmed'))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate('Form', 'Completed'))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate('Form', 'URL'))
