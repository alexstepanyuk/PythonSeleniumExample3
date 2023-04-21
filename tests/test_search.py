# coding=utf-8
import pytest
from pages.login_page import LoginPage
from tests.base_test import BaseTest


class TestSearch(BaseTest):

    def test_login(self, load_pages):
        self.login_page = LoginPage(self.driver, self.wait)
        self.login_page.open()

        self.login_page.paste_username("admin")
        self.login_page.click_login()

