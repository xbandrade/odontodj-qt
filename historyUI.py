from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidget

import gui.main.res  # noqa
from api_connect import retrieve_appointments


class HistoryUI(QtWidgets.QWidget):
    def __init__(self, parent=None, main_app=None):
        super().__init__(parent)
        self.access_token = main_app.access_token
        self.username = main_app.username
        self.url = main_app.url
        self.window = parent
        self.table_widget = None
        self.setupUi()

    def setupUi(self):
        self.window.switch_to_framed()
        self.centralwidget = QtWidgets.QWidget(self.window)
        self.centralwidget.setFixedSize(1120, 760)
        self.centralwidget.setObjectName('widget')
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
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
            "background-color: qconicalgradient(cx:0.5, cy:0.5, angle:45,"
            "stop:0 rgba(85, 98, 112, 226), stop:0.5 rgba(20, 47, 78, 219),"
            "stop:1 rgba(85, 98, 112, 226));"
            "    color: rgba(255, 255, 255, 210);\n"
            "    border-radius: 5px;    \n"
            "}\n"
            "QPushButton#scheduleButton:hover{    \n"
            "    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:45,"
            "stop:0 rgba(105, 118, 132, 226), stop:0.5 rgba(40, 67, 98, 219),"
            "stop:1 rgba(105, 118, 132, 226));"
            "}\n"
            "QPushButton#scheduleButton:pressed{\n"
            "    padding-left:5px;\n"
            "    padding-top:5px;\n"
            "    background-color: rgba(105, 118, 132, 200);\n"
            "}\n"
            ""
        )
        self.appointment_banner.setObjectName('scheduleButton')
        appointments = retrieve_appointments(self.url, self.access_token)
        gray_bg = """
            background-color: rgba(195, 195, 195, 180);
            border-image: none;
        """
        if appointments:
            self.table_widget = QtWidgets.QTableWidget(self.widget_2)
            self.table_widget.setGeometry(QtCore.QRect(50, 250, 1011, 611))
            self.table_widget.setStyleSheet(gray_bg)
            self.table_widget.setRowCount(1)
            self.table_widget.setColumnCount(8)
            self.table_widget.setObjectName('tableWidget')
            item = QtWidgets.QTableWidgetItem()
            self.table_widget.setHorizontalHeaderItem(0, item)
            item = QtWidgets.QTableWidgetItem()
            self.table_widget.setHorizontalHeaderItem(1, item)
            item = QtWidgets.QTableWidgetItem()
            self.table_widget.setHorizontalHeaderItem(2, item)
            item = QtWidgets.QTableWidgetItem()
            self.table_widget.setHorizontalHeaderItem(3, item)
            item = QtWidgets.QTableWidgetItem()
            self.table_widget.setHorizontalHeaderItem(4, item)
            item = QtWidgets.QTableWidgetItem()
            self.table_widget.setHorizontalHeaderItem(5, item)
            item = QtWidgets.QTableWidgetItem()
            self.table_widget.setHorizontalHeaderItem(6, item)
            item = QtWidgets.QTableWidgetItem()
            self.table_widget.setHorizontalHeaderItem(7, item)
            self.table_widget.horizontalHeader().setVisible(True)
            self.table_widget.horizontalHeader().setCascadingSectionResizes(False)  # noqa
            self.table_widget.horizontalHeader().setDefaultSectionSize(126)
            self.table_widget.horizontalHeader().setHighlightSections(True)
            self.table_widget.horizontalHeader().setMinimumSectionSize(49)
            self.table_widget.horizontalHeader().setSortIndicatorShown(False)
            self.table_widget.horizontalHeader().setStretchLastSection(False)
            self.table_widget.verticalHeader().setVisible(False)
            self.table_widget.verticalHeader().setHighlightSections(True)
            self.table_widget.setEditTriggers(QTableWidget.NoEditTriggers)
            self.table_widget.setFocusPolicy(Qt.NoFocus)
            self.table_widget.setSelectionMode(QTableWidget.NoSelection)
            data = []
            for appt in appointments:
                data.append([
                    f'#0{appt.get("id")}', appt.get('procedure'),
                    appt.get('date'), appt.get('time'),
                    'R$' + str(appt.get('price', '')),
                    '✔️' if appt.get('is_confirmed') else '✖️',
                    '✔️' if appt.get('is_completed') else '✖️', '---',  # url
                ])
            for row in data:
                self.table_widget.insertRow(self.table_widget.rowCount())
                for column, item in enumerate(row):
                    self.table_widget.setItem(
                        self.table_widget.rowCount() - 1,
                        column, QtWidgets.QTableWidgetItem(item)
                    )
            row_height = self.table_widget.rowHeight(0)
            desired_height = self.table_widget.rowCount() * row_height
            self.table_widget.setFixedHeight(desired_height)
            # self.table_widget.resizeColumnsToContents()
            header_horizontal = self.table_widget.horizontalHeader()
            header_horizontal.setStyleSheet(
                "QHeaderView::section { "
                "background-color: rgba(195, 195, 195, 180); }"
            )
            scroll_bar_style = """
                QScrollBar:vertical {
                    background-color: gray;
                    width: 25px;
                }
                QScrollBar:horizontal {
                    background-color: gray;
                    height: 25px;
                }
                QScrollBar::handle {
                    background-color: lightGray;
                }
                QScrollBar::handle:hover {
                    background-color: rgba(195, 195, 195, 180);
                }
                QScrollBar::sub-page, QScrollBar::add-page {
                    background-color: none;
                }
            """
            self.table_widget.verticalScrollBar().setStyleSheet(
                scroll_bar_style
            )
            self.table_widget.horizontalScrollBar().setStyleSheet(
                scroll_bar_style
            )
        else:
            print('No Appointments')
            self.label_3 = QtWidgets.QLabel(self.widget_2)
            self.label_3.setGeometry(QtCore.QRect(10, 250, 1091, 81))
            font = QtGui.QFont()
            font.setPointSize(17)
            font.setBold(True)
            font.setWeight(75)
            self.label_3.setFont(font)
            self.label_3.setStyleSheet(
                "border-image: none;\n"
                "color: rgba(255, 255, 255, 210);"
            )
            self.label_3.setAlignment(QtCore.Qt.AlignCenter)
            self.label_3.setObjectName('label_2')
            self.label_3.setText('No Appointments Found')
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.window)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.window.setWindowTitle(_translate('Form', 'OdontoDj'))
        self.label_2.setText(_translate('Form', 'Patient History'))
        self.appointment_banner.setText(_translate(
            'Form', f"{self.username}'s Appointments")
        )
        if self.table_widget:
            item = self.table_widget.horizontalHeaderItem(0)
            item.setText(_translate('Form', 'ID'))
            item = self.table_widget.horizontalHeaderItem(1)
            item.setText(_translate('Form', 'Procedure'))
            item = self.table_widget.horizontalHeaderItem(2)
            item.setText(_translate('Form', 'Date'))
            item = self.table_widget.horizontalHeaderItem(3)
            item.setText(_translate('Form', 'Time'))
            item = self.table_widget.horizontalHeaderItem(4)
            item.setText(_translate('Form', 'Price'))
            item = self.table_widget.horizontalHeaderItem(5)
            item.setText(_translate('Form', 'Confirmed'))
            item = self.table_widget.horizontalHeaderItem(6)
            item.setText(_translate('Form', 'Completed'))
            item = self.table_widget.horizontalHeaderItem(7)
            item.setText(_translate('Form', 'URL'))
