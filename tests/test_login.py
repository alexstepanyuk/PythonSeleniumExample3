# coding=utf-8
import pytest
from pages.login_page import LoginPage
from pages.login_password_page import LoginPasswordPage
from pages.my_view_page import MyViewPage
from tests.base_test import BaseTest


class TestLogin(BaseTest):

    def test_login(self):
        self.login_page = LoginPage(self.driver, self.wait)
        self.login_password_page = LoginPasswordPage(self.driver, self.wait)
        self.my_view_page = MyViewPage(self.driver, self.wait)

        self.login_page.open()
        assert self.login_page.is_current_url() == True, "Текущий url " + self.driver.current_url() + " не совпадает с " + self.login_page.current_url

        self.login_page.paste_username(self.ADMIN)
        assert self.login_page.get_username() == self.ADMIN, "Значение в поле Username не совпадает"
        self.login_page.click_login()
        assert self.login_password_page.is_current_url() == True, "Текущий url " + self.driver.current_url() + " не совпадает с " + self.login_password_page.current_url

        self.login_password_page.paste_password(self.ADMIN_PASSWORD)
        assert self.login_password_page.get_password() == self.ADMIN_PASSWORD, "Значение в поле Password не совпадает"
        self.login_page.click_login()
        assert self.my_view_page.is_current_url() == True, "Текущий url " + self.driver.current_url() + " не совпадает с " + self.my_view_page.current_url
        assert self.my_view_page.get_username() == self.ADMIN, "Имя пользователя не совпадает"
