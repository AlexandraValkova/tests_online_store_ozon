from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    def __init__(self, driver):
        url = 'https://www.ozon.ru/'
        super().__init__(driver, url)
        driver.get(url)

        self.icon = driver.find_element(By.XPATH, '//span[text()="Войти"]')
        self.form = (By.XPATH, '//input[@name="phone"]')
        self.btn = driver.find_element(By.XPATH, '//span[text()="Войти"]')
