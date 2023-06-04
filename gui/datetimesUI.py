from PyQt5 import QtCore, QtGui, QtWidgets

import gui.main.res  # noqa
from api_connect import retrieve_datetimes


class CenteredDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignCenter

    def createEditor(self, parent, option, index):
        return None


class DateTimesUI(QtWidgets.QWidget):
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
        self.title.setGeometry(QtCore.QRect(310, 30, 561, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet("color: rgba(255, 255, 255, 210);")
        self.title.setObjectName("title")
        self.listView = QtWidgets.QListView(self.logo_frame)
        self.listView.setGeometry(QtCore.QRect(390, 150, 361, 541))
        self.listView.setStyleSheet(
            "background-color: rgba(195, 195, 195, 180);")
        self.listView.setObjectName("listView")
        model = QtCore.QStringListModel()
        self.listView.setModel(model)
        delegate = CenteredDelegate(self.listView)
        self.listView.setItemDelegate(delegate)
        datetimes = retrieve_datetimes(self.url, self.access_token)
        self.listView.setStyleSheet(
            "background-color: rgba(195, 195, 195, 180);"
        )
        items = datetimes or ["No Available Times"]
        model.setStringList(items)
        self.gridLayout.addWidget(self.logo_frame, 0, 0, 1, 2)
        self.window.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.window)
        self.window.show()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.window.setWindowTitle(_translate(
            "MainWindow", "MainWindow"))
        self.title.setText(_translate(
            "MainWindow", "Available Dates and Times"))
