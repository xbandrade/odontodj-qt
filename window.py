from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QMouseEvent
from PyQt5.QtWidgets import QMainWindow


class CustomMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.draggable = True
        self.mousePressPos = None
        self.mouseMovePos = None
        self.setObjectName('OdontoDj')
        self.resize(1118, 750)
        icon = QIcon('img/od_logo.png')
        self.setWindowIcon(icon)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton and self.draggable:
            self.mousePressPos = event.globalPos()
            self.mouseMovePos = event.globalPos()
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent):
        if not self.mouseMovePos:
            return
        if event.buttons() == Qt.LeftButton and self.draggable:
            delta = event.globalPos() - self.mouseMovePos
            self.move(self.pos() + delta)
            self.mouseMovePos = event.globalPos()
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton and self.draggable:
            self.mousePressPos = None
            self.mouseMovePos = None
        super().mouseReleaseEvent(event)

    def switch_to_framed(self):
        self.setWindowFlags(QtCore.Qt.Widget)
        flags = self.windowFlags()
        flags &= ~Qt.WindowMaximizeButtonHint
        self.setWindowFlags(flags)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, False)
        self.show()

    def switch_to_frameless(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.show()


class CustomNewWindow(CustomMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
