def navigate_to_main_app(window, username):
    from mainUI import MainUI
    main_ui = MainUI(window, username)
    window.centralWidget().deleteLater()
    window.setCentralWidget(main_ui.widget)


def navigate_to_login_page(window):
    from loginUI import LoginUI
    login_ui = LoginUI(window)
    window.centralWidget().deleteLater()
    window.setCentralWidget(login_ui.widget)
