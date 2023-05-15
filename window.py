from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QMainWindow


class CustomMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.draggable = True
        self.mousePressPos = None
        self.mouseMovePos = None

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
