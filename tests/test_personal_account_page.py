# pytest -v tests\test_personal_account_page.py

from pages.personal_account_page import PersonalAccountPage


def test_link_points(driver):
    """Проверить ссылку (Пункты выдачи)"""
    page = PersonalAccountPage(driver)
    page.points.click()


def test_link_comparison(driver):
    """Проверить ссылку (Сравнение товаров)"""
    page = PersonalAccountPage(driver)
    page.points.click()


def test_link_business(driver):
    """Проверить ссылку (Ozon для бизнеса)"""
    page = PersonalAccountPage(driver)
    page.points.click()


def test_link_account(driver):
    """Проверить ссылку (Войти или зарегистрироваться)"""
    page = PersonalAccountPage(driver)
    page.account.click()


def test_link_for_me(driver):
    """Проверить ссылку (Для меня)"""
    page = PersonalAccountPage(driver)
    page.for_me.click()


def test_link_delivery(driver):
    """Проверить ссылку (Условия и стоимость доставки)"""
    page = PersonalAccountPage(driver)
    page.delivery.click()


def test_link_payment(driver):
    """Проверить ссылку (Условия оплаты)"""
    page = PersonalAccountPage(driver)
    page.payment.click()


def test_link_refund(driver):
    """Проверить ссылку (Условия возврата)"""
    page = PersonalAccountPage(driver)
    page.refund.click()


def test_link_questions(driver):
    """Проверить ссылку (Все вопросы)"""
    page = PersonalAccountPage(driver)
    page.questions.click()


def test_link_view_all(driver):
    """Проверить ссылку истории (Смотреть все)"""
    page = PersonalAccountPage(driver)
    page.view_all.click()
