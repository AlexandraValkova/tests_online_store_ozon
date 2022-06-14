from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class PersonalAccountPage(BasePage):
    def __init__(self, driver):
        url = 'https://www.ozon.ru/my/main'
        super().__init__(driver, url)
        driver.get(url)

        self.points = driver.find_element(By.XPATH, '//span[text()="Пункты выдачи"]')
        self.comparison_products = driver.find_element(By.XPATH, '//span[text()="Сравнение товаров"]')
        self.ozon_business = driver.find_element(By.XPATH, '//span[text()="Ozon для бизнеса"]')
        self.account = driver.find_element(By.XPATH, '//span[text()="Войти или зарегистрироваться"]')
        self.for_me = driver.find_element(By.XPATH, '//span[text()="Для меня"]')
        self.delivery = driver.find_element(By.XPATH, '//span[text()="Условия и стоимость доставки"]')
        self.payment = driver.find_element(By.XPATH, '//span[text()="Условия оплаты"]')
        self.refund = driver.find_element(By.XPATH, '//span[text()="Условия возврата"]')
        self.questions = driver.find_element(By.XPATH, '//span[text()="Все вопросы"]')
        self.view_all = driver.find_element(By.XPATH, '//span[text()="Смотреть все"]')
