"""
This file contains all the web locators like xpath, id, tag name, link text etc.,
"""

class Locators:

    # Login Page
    username_locator = "user-name"                   # ID
    password_locator = "password"
    email = "email"
    email_password = "password"
    login_btn = "login-btn"                            # Class
    login_button_home = "//a[@class='btn login-btn' and text()='Login']"
    sign_up = "//a[@class='⭐️rawbli-0 bg-green-500 hover:bg-green-600 text-white font-normal py-2 px-4 rounded text-base min-h-8 h-8 align-middle mr-2']"
    drop_down = "dropdown_contents"
    logout = "//div[contains(text(), 'Sign Out')]"