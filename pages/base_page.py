from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver, wait):
        self.current_url = "https://academ-it.ru/mantisbt/"
        self.driver = driver
        self.wait = wait

    def open(self):
        self.driver.get(self.current_url)

    def get_title(self):
        return self.driver.title

    def paste_text(self, locator, text):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).move_to_element()
        self.driver.find_element(*locator).send_keys(text)

    def click(self, locator):
        self.driver.find_element(*locator).move_to_element()
        self.driver.find_element(*locator).click()

    def is_current_url(self):
        self.wait.until(lambda driver: driver.current_url == self.current_url)
        return self.current_url == self.driver.current_url()

    def wait_element(self, element):
        self.wait.until(ec.presence_of_element_located(element))

