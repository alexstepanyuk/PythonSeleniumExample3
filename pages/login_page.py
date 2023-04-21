from pages.base_page import BasePage
from data.locators import LoginPageLocators


class LoginPage(BasePage):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.current_url += "login_page.php"
        self.locator = LoginPageLocators

    def paste_username(self, input_text):
        self.paste_text(*self.locator.USERNAME_INPUT, input_text)

    def click_login(self):
        self.click(*self.locator.LOGIN_BUTTON)