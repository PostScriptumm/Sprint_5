from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest

from tests.locators import (login_input, password_input, login_button, login_button_text, order_button,
                            main_login_button, main_account_button, reg_login_button, forgot_login_button)

page_button = \
    [
        ['https://stellarburgers.nomoreparties.site/', main_login_button],
        ['https://stellarburgers.nomoreparties.site/', main_account_button],
        ['https://stellarburgers.nomoreparties.site/register', reg_login_button],
        ['https://stellarburgers.nomoreparties.site/forgot-password', forgot_login_button]
    ]


class TestLogin:

    @pytest.mark.parametrize('page, button', page_button)
    def test_login_from_main_register_forgot_password_pages(self, page, button, options):
        driver = webdriver.Chrome(options=options)
        driver.get(page)
        driver.find_element(By.XPATH, button).click()
        WebDriverWait(driver, 5) \
            .until(expected_conditions.visibility_of_element_located((By.XPATH, login_button_text)))
        driver.find_element(By.XPATH, login_input).send_keys('andreytebenkov3000@yandex.ru')
        driver.find_element(By.XPATH, password_input).send_keys('password')
        driver.find_element(By.XPATH, login_button).click()
        WebDriverWait(driver, 5) \
            .until(expected_conditions.visibility_of_element_located((By.XPATH, order_button)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()
