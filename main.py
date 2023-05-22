from PyQt5.QtWidgets import QApplication

from loginUI import LoginUI
from window import CustomMainWindow


def main():
    app = QApplication([])
    main_window = CustomMainWindow()
    login_ui = LoginUI(main_window)
    main_window.setCentralWidget(login_ui.widget)
    main_window.show()
    app.exec_()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
