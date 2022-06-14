# pytest -v tests\test_main_page.py

import pytest
from pages.main_page import MainPage
from selenium.webdriver.common.by import By


def test_link_logotype(driver):
    """Проверить кликабельность логотипа сайта Ozon"""
    page = MainPage(driver)
    page.logo_button.click()


def test_personal_account_page(driver):
    """Проверить вход в личный кабинет"""
    page = MainPage(driver)
    page.account_icon.click()
    driver.save_screenshot('page_my_main.png')


def test_link_favorites(driver):
    """Проверить ссылку (Избранное)"""
    page = MainPage(driver)
    page.link_favorites.click()


def test_link_help(driver):
    """Проверить ссылку (Помощь)"""
    page = MainPage(driver)
    page.link_help.click()


def test_issuing_point(driver):
    """Проверить ссылку (Пункты выдачи)"""
    page = MainPage(driver)
    page.link_points.click()


def test_link_business(driver):
    """Проверить ссылку (Ozon для бизнеса)"""
    page = MainPage(driver)
    page.link_business.click()


def test_link_mobile_app(driver):
    """Проверить ссылку (Мобильное приложение)"""
    page = MainPage(driver)
    page.link_mobile.click()


def test_slider_button(driver):
    """Проверить прокрутку банера"""
    page = MainPage(driver)
    page.slide_button.click()


def test_link_buy(driver):
    """Проверить ссылку (Успей купить)"""
    page = MainPage(driver)
    page.buy_button.click()


def test_catalog_visible(driver):
    """Проверить наличие каталога"""
    page = MainPage(driver)
    assert page.catalog_button.is_displayed()


def test_catalog(driver):
    """Проверить кликабельность иконки (Каталог)"""
    page = MainPage(driver)
    page.catalog_button.click()


@pytest.mark.parametrize('name', ['Акции', 'Бренды', 'Магазины'], ids=['actions', 'brends', 'shops'])
def test_main_menu_links(driver, name):
    """Проверить ссылки главного меню"""
    page = MainPage(driver)
    menu = []
    for i in range(len(page.main_menu)):
        menu.append(page.main_menu[i].text)
    assert name in menu


@pytest.mark.parametrize('name', ['Электроника', 'Детские товары', 'Дом и сад'],
                         ids=['Electronics', 'Children', 'Home'])
def test_catalog_menu(driver, name):
    """Проверить наличие товаров в каталоге"""
    page = MainPage(driver)
    page.catalog_button.click()
    catalog = []
    for i in range(len(page.catalog_menu)):
        catalog.append(page.catalog_menu[i].text)
    assert name in catalog


def test_catalog_menu_clickable(driver):
    """Проверить поиск товара по каталогу"""
    page = MainPage(driver)
    page.catalog_button.click()
    page.catalog_menu[1].click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == "Одежда"
    assert page.get_relative_link() == '/category/odezhda-obuv-i-aksessuary-7500/'


@pytest.mark.parametrize('name', ['Книга', 'Кружка', 'Рубашка'], ids=['Book', 'Cup', 'Shirt'])
def test_check_main_search(driver, name):
    """Проверить поисковую строку"""
    page = MainPage(driver)
    assert page.search_field.is_displayed()
    page.main_search_field(name)
