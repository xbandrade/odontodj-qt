from PyQt5.QtWidgets import QApplication, QWidget

from gui.loginUI import Ui_Form as UI


def main():
    app = QApplication([])
    window = QWidget()
    ui = UI()
    ui.setupUi(window)
    window.show()
    app.exec_()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
