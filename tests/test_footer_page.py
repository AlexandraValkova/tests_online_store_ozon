# pytest -v tests\test_footer_page.py

from pages.main_page import FooterPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_link_vk(driver):
    """Проверить ссылку на социальные сети VK"""
    page = FooterPage(driver)
    page.scroll_to_footer()
    vk_icon = WebDriverWait(driver, 10).until(EC.presence_of_element_located(page.link_vk))
    vk_icon.click()
    driver.switch_to.window(driver.window_handles[1])
    assert page.get_url() == 'https://vk.com/ozon'
    driver.save_screenshot('page_vk.png')


def test_link_ok(driver):
    """Проверить ссылку на социальные сети OK"""
    page = FooterPage(driver)
    page.scroll_to_footer()
    ok_icon = WebDriverWait(driver, 10).until(EC.presence_of_element_located(page.link_ok))
    ok_icon.click()
    driver.switch_to.window(driver.window_handles[1])
    assert page.get_url() == 'https://ok.ru/ozon'
    driver.save_screenshot('page_ok.png')


def test_link_tg(driver):
    """Проверить ссылку на социальные сети Telegram"""
    page = FooterPage(driver)
    page.scroll_to_footer()
    tg_icon = WebDriverWait(driver, 10).until(EC.presence_of_element_located(page.link_tg))
    tg_icon.click()
    driver.switch_to.window(driver.window_handles[1])
    assert page.get_url() == 'https://t.me/ozonhq'
    driver.save_screenshot('page_tg.png')


def test_safety_icon(driver):
    """Проверить иконку (Зона безопасного сервиса)"""
    page = FooterPage(driver)
    page.scroll_to_footer()
    safety_icon = WebDriverWait(driver, 10).until(EC.presence_of_element_located(page.safety_service))
    safety_icon.click()
    driver.switch_to.window(driver.window_handles[1])
    assert page.get_url() == 'https://ecomvscovid.ru/'


def test_job_link(driver):
    """Проверить ссылку (Ozon Вакансии)"""
    page = FooterPage(driver)
    page.scroll_to_footer()
    page.job.click()
    assert page.get_url() == 'https://job.ozon.ru/'


def test_travel_link(driver):
    """Проверить ссылку (Ozon Travel)"""
    page = FooterPage(driver)
    page.scroll_to_footer()
    page.travel.click()
    assert page.get_url() == 'https://www.ozon.ru/travel/?perehod=mainpagebottom'


def test_it_courses_link(driver):
    """Проверить ссылку (Route 256)"""
    page = FooterPage(driver)
    page.scroll_to_footer()
    page.route.click()
    assert page.get_url() == 'https://route256.ozon.ru/'


def test_litres_link(driver):
    """Проверить ссылку (LITRES.ru)"""
    page = FooterPage(driver)
    page.scroll_to_footer()
    page.litres.click()
    assert page.get_url() == 'https://www.litres.ru/'
