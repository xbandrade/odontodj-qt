from PyQt5.QtWidgets import QApplication, QStackedWidget

from loginUI import LoginUI as UI
from window import CustomMainWindow


def main():
    app = QApplication([])
    main_window = CustomMainWindow()
    main_window.setGeometry(100, 100, 800, 600)
    stacked_widget = QStackedWidget(main_window)
    login_ui = UI(main_window)
    stacked_widget.addWidget(login_ui)
    main_window.setCentralWidget(stacked_widget)
    main_window.show()
    app.exec_()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
