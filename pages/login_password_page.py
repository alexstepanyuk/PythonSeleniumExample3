from pages.base_page import BasePage
from data.locators import LoginPasswordPageLocators


class LoginPasswordPage(BasePage):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.current_url += "login_password_page.php"
        self.locator = LoginPasswordPageLocators

    def paste_password(self, input_text):
        self.paste_text(self.locator.PASSWORD_INPUT, input_text)

    def get_password(self):
        return self.get_value(self.locator.PASSWORD_INPUT)

    def click_login(self):
        self.click(self.locator.LOGIN_BUTTON)