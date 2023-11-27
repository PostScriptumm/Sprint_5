from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest

from tests.locators import (account_exit_button, login_button_text, stellar_burgers_logo, constructor_button,
                            collect_burger)


class TestPersonalAccount:

    def test_button_personal_account(self, login_personal_account):
        driver = login_personal_account
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
        driver.quit()

    def test_button_exit_in_personal_account(self, login_personal_account):
        driver = login_personal_account
        driver.find_element(By.XPATH, account_exit_button).click()
        WebDriverWait(driver, 5) \
            .until(expected_conditions.visibility_of_element_located((By.XPATH, login_button_text)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quit()

    @pytest.mark.parametrize('button', [stellar_burgers_logo, constructor_button])
    def test_go_to_constructor_from_personal_account(self, login_personal_account, button):
        driver = login_personal_account
        driver.find_element(By.XPATH, button).click()
        WebDriverWait(driver, 5) \
            .until(expected_conditions.visibility_of_element_located((By.XPATH, collect_burger)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()
