from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME_INPUT = (By.ID, "username")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='Войти']")