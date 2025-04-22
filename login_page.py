"""
Login page contain methods related to the login action
"""

from selenium.webdriver.common.by import By
from Page_Objects.base_page import BasePage
from Test_Locators.locators import Locators

class LoginPage(BasePage):
    # Define locators for different elements on the page
    LOGIN_BUTTON = (By.XPATH, Locators.login_button_home)           # XPATH for final login submit button
    LOGIN_BTN = (By.ID, Locators.login_btn)                         # ID for login button on homepage
    SIGN_UP_BTN = (By.XPATH, Locators.sign_up)                      # XPATH for sign-up button
    EMAIL = (By.ID, Locators.email)                                 # ID for email input field
    EMAIL_PASSWORD = (By.ID, Locators.email_password)               # ID for password input field
    DROP_DOWN = (By.ID, Locators.drop_down)                         # ID for profile/account dropdown
    LOGOUT = (By.XPATH, Locators.logout)                            # XPATH for logout button

    # Clicks the login button on the homepage
    def click_login_home(self):
        self.click(self.LOGIN_BTN)

    # Enters the given email into the email input field
    def enter_email(self, email):
        self.enter_text(self.EMAIL, email)

    # Enters the given password into the password input field
    def enter_email_password(self, email_password):
        self.enter_text(self.EMAIL_PASSWORD, email_password)

    # Clicks on the profile/account dropdown
    def click_drop_down(self):
        self.click(self.DROP_DOWN)

    # Clicks the logout option in the dropdown
    def click_logout(self):
        self.click(self.LOGOUT)

    # Checks if the login button is visible and clickable
    def check_login(self):
        #return self.is_visible(self.LOGIN_BTN) and self.is_clickable(self.LOGIN_BTN)
        try:
            return self.is_visible(self.LOGIN_BTN) and self.is_clickable(self.LOGIN_BTN)
        except Exception as e:
            print(f"[ERROR] Error checking Login button: {e}")
            return False

    # Clicks the actual login button (after entering credentials)
    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    # Checks if the sign-up button is visible and clickable
    def check_sign_up_btn(self):
        #return self.is_visible(self.SIGN_UP_BTN) and self.is_clickable(self.SIGN_UP_BTN)
        try:
            return self.is_visible(self.SIGN_UP_BTN) and self.is_clickable(self.SIGN_UP_BTN)
        except Exception as e:
            print(f"[ERROR] Error checking Login button: {e}")
            return False











    # def enter_username(self, username):
    #     self.enter_text(self.USERNAME_INPUT, username)
    #
    # def enter_password(self, password):
    #     self.enter_text(self.PASSWORD_INPUT, password)

    # def validate_username(self):
    #     return self.is_visible(self.USERNAME_INPUT)

    # def validate_password(self):
    #     return self.is_visible(self.PASSWORD_INPUT)