# pytest -v tests\test_login_page.py
import time
import pickle
import pytest
from pages.login_page import LoginPage


def test_login_url(driver):
    """Проверить форму входа в аккаунт"""
    page = LoginPage(driver)
    page.icon.click()
    time.sleep(2)


@pytest.mark.skip
def test_positive_login(driver):
    """Войти с валидными данными"""
    page = LoginPage(driver)
    with open('cookie.txt', 'wb') as cookies:
        pickle.dump(driver.get_cookies(), cookies)
    page.icon.click()
    time.sleep(2)
    page.form.clear()
    page.form.send_keys(cookies)
    page.btn.click()
