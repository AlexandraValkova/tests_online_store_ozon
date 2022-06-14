from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    def __init__(self, driver):
        url = 'https://www.ozon.ru/'
        super().__init__(driver, url)
        driver.get(url)
        self.logo_button = driver.find_element(By.XPATH, '//a[@href="/highlight/marafon-skidok-478522/"]')
        self.account_icon = driver.find_element(By.XPATH, '//span[text()="Войти"]')
        self.link_favorites = driver.find_element(By.XPATH, '//span[text()="Избранное"]')
        self.link_help = driver.find_element(By.XPATH, '//a[@href="//docs.ozon.ru/common/"]')
        self.link_points = driver.find_element(By.XPATH, '//a[@href="/info/map/"]')
        self.link_business = driver.find_element(By.XPATH, '//a[@href="//business.ozon.ru/?perehod=header"]')
        self.link_mobile = driver.find_element(By.XPATH, '//span[text()="Мобильное приложение"]')
        self.slide_button = driver.find_element(By.XPATH, '//button[@aria-label="Previous slide"]')
        self.buy_button = driver.find_element(By.XPATH, '//a[@href="/highlight/globalpromo/"]')
        self.catalog_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Каталог')]")
        self.main_menu = driver.find_elements(By.XPATH, "//ul[@data-widget='horizontalMenu']//a")
        self.catalog_menu = driver.find_elements(By.XPATH, "//div[@data-widget='catalogMenu']//a/span")
        self.search_field = driver.find_element(By.XPATH, '//input[@placeholder="Искать на Ozon"]')
        self.search_button = driver.find_element(By.XPATH, '//*[@aria-label="Поиск"]/..')
        self.result_table = driver.find_element(By.XPATH, '//a[contains(@href, "/product/")]')

    def main_search_field(self, input_text):
        self.search_field.clear()
        self.search_field.send_keys(input_text)
        self.search_button.click()


class FooterPage(BasePage):
    def __init__(self, driver):
        url = 'https://www.ozon.ru/'
        super().__init__(driver, url)
        driver.get(url)
        self.body = driver.find_element(By.TAG_NAME, 'body')
        self.footer = (By.XPATH, '//footer')
        self.link_vk = (By.XPATH, '//a[@title ="VK"]')
        self.link_ok = (By.XPATH, '//a[@title ="Одноклассники"]')
        self.link_tg = (By.XPATH, '//a[@title ="Telegram"]')
        self.safety_service = (By.XPATH, '//img[@alt="Зона безопасного сервиса"]')
        self.job = driver.find_element(By.XPATH, '//a[contains(text(), "Ozon Вакансии")]')
        self.travel = driver.find_element(By.XPATH, '//a[contains(text(), "OZON Travel")]')
        self.route = driver.find_element(By.XPATH, '//a[contains(text(), "Route 256")]')
        self.litres = driver.find_element(By.XPATH, '//a[contains(text(), "LITRES.ru")]')

    def scroll_to_footer(self):
        self.body.send_keys(Keys.END)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.footer))
        self.body.send_keys(Keys.END)
