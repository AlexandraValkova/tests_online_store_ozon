from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def __init__(self, driver):
        url = 'https://www.ozon.ru/category/printery-15771'
        super().__init__(driver, url)
        driver.get(url)
        self.product_card = driver.find_element(By.XPATH, '//span[text()="Лучшая цена на Ozon"]')
        self.add_basket = driver.find_element(By.XPATH, '//span[text()="В корзину"]')


class ElectronicsPage(BasePage):
    def __init__(self, driver):
        url = 'https://www.ozon.ru/category/elektronika-15500/'
        super().__init__(driver, url)
        driver.get(url)
        self.title = (By.TAG_NAME, 'h1')
        self.main_menu = self.driver.find_elements(By.XPATH, '//div[@data-widget="catalogHorizontalMenu"]//a')
        self.kitchen_appliances = driver.find_element(By.XPATH, '//span[text()="Техника для кухни"]')
