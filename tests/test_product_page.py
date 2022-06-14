# pytest -v tests\test_product_page.py

import pytest
from pages.product_page import ProductPage
from pages.product_page import ElectronicsPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_open_card_product(driver):
    """Проверить кликабельность карточки товара"""
    page = ProductPage(driver)
    page.product_card.click()


def test_buy_link(driver):
    """Проверить кликабельность кнопки(В корзину)"""
    page = ProductPage(driver)
    page.add_basket.click()


@pytest.mark.parametrize('point', ['БЫТОВАЯ ТЕХНИКА', 'СМАРТ-ЧАСЫ', 'ТЕЛЕВИЗОРЫ', 'НОУТБУКИ',
                         'КОМПЬЮТЕРЫ', 'АУДИОТЕХНИКА', 'ИГРЫ И КОНСОЛИ'],
                         ids=['Home appliance', 'Smartphones', 'TV', 'Notebooks', 'Computers', 'Audio', 'Playstations'])
def test_electronics_menu(driver, point):
    """Проверить всплывающие окна категорий товаров (Электроника)"""
    page = ElectronicsPage(driver)
    electronics_title = WebDriverWait(driver, 10).until(EC.presence_of_element_located(page.title))
    assert 'Электроника' == electronics_title.text
    menu = page.main_menu
    menu_points = []
    for i in range(len(menu)):
        menu_points.append(menu[i].text)
    for i in range(len(menu_points)):
        if point in menu_points[i]:
            assert menu[i].is_displayed()
            menu[i].click()


def test_appliances_card(driver):
    """Проверить карточку товара в категории (Бытовая техника)"""
    page = ElectronicsPage(driver)
    driver.execute_script("arguments[0].scrollIntoViewIfNeeded(true);", page.kitchen_appliances)
    page.kitchen_appliances.click()
