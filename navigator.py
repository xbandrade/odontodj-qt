def navigate_to_main_app(window, username, url, access_token):
    from gui.mainUI import MainUI
    main_ui = MainUI(window, username, url, access_token)
    window.centralWidget().deleteLater()
    window.setCentralWidget(main_ui.widget)


def navigate_to_login_page(window):
    from gui.loginUI import LoginUI
    login_ui = LoginUI(window)
    window.centralWidget().deleteLater()
    window.setCentralWidget(login_ui.widget)
