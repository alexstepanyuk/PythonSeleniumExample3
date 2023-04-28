from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME_INPUT = (By.ID, "username")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='Войти']")

class LoginPasswordPageLocators:
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='Войти']")

class MyViewPageLocators:
    USERNAME = (By.XPATH, "//span[@class='user-info']")