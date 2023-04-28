from pages.base_page import BasePage
from data.locators import MyViewPageLocators


class MyViewPage(BasePage):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.current_url += "my_view_page.php"
        self.locator = MyViewPageLocators

    def get_username(self):
        return self.get_text(self.locator.USERNAME)
