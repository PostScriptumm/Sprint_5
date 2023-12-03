from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest

from tests.locators import LoginPageLocators, MainPageLocators, PersonalPageLocators
from tests.data import UrlPageData


class TestPersonalAccount:

    def test_button_personal_account(self, driver, go_to_personal):
        assert driver.current_url == UrlPageData.profile_page \
               and expected_conditions.element_to_be_clickable((By.XPATH, PersonalPageLocators.account_exit_button))

    def test_button_exit_in_personal_account(self, driver, go_to_personal):
        driver.find_element(By.XPATH, PersonalPageLocators.account_exit_button).click()
        WebDriverWait(driver, 5) \
            .until(expected_conditions.visibility_of_element_located((By.XPATH, LoginPageLocators.login_button_text)))
        assert driver.current_url == UrlPageData.login_page \
               and expected_conditions.element_to_be_clickable((By.XPATH, LoginPageLocators.login_button))

    @pytest.mark.parametrize('button', [MainPageLocators.stellar_burgers_logo, MainPageLocators.constructor_button])
    def test_go_to_constructor_from_personal_account(self, driver, go_to_personal, button):
        driver.find_element(By.XPATH, button).click()
        WebDriverWait(driver, 5) \
            .until(expected_conditions.visibility_of_element_located((By.XPATH, MainPageLocators.collect_burger)))
        assert driver.current_url == UrlPageData.main_page \
               and expected_conditions.element_to_be_clickable((By.XPATH, MainPageLocators.order_button))
