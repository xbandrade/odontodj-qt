from PyQt5.QtWidgets import QApplication, QStackedWidget

from loginUI import LoginUI
from mainUI import MainUI
from window import CustomMainWindow


def main():
    app = QApplication([])
    main_window = CustomMainWindow()
    stacked_widget = QStackedWidget(main_window)
    login_ui = LoginUI(main_window, stacked_widget)
    main_ui = MainUI(main_window)
    stacked_widget.addWidget(login_ui)
    stacked_widget.addWidget(main_ui)
    main_window.setCentralWidget(stacked_widget)
    stacked_widget.setCurrentIndex(0)
    main_window.show()
    app.exec_()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
