from PyQt5.QtWidgets import QApplication

from window import LoginWindow


def main():
    app = QApplication([])
    window = LoginWindow(1200, 800)
    window.show()
    app.exec_()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
