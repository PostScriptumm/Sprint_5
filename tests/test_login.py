from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest

from tests.locators import LoginPageLocators, MainPageLocators, ForgotPassPagelocators, RegPageLocators
from tests.data import UserLoginData, UrlPageData

page_button = \
    [
        [UrlPageData.main_page, MainPageLocators.main_login_button],
        [UrlPageData.main_page, MainPageLocators.main_account_button],
        [UrlPageData.registration_page, RegPageLocators.reg_login_button],
        [UrlPageData.forgot_pass_page, ForgotPassPagelocators.forgot_login_button]
    ]


class TestLogin:

    @pytest.mark.parametrize('page, button', page_button)
    def test_login_from_main_register_forgot_password_pages(self, driver, page, button):
        driver.get(page)
        driver.find_element(By.XPATH, button).click()
        WebDriverWait(driver, 5) \
            .until(expected_conditions.visibility_of_element_located((By.XPATH, LoginPageLocators.login_button_text)))
        driver.find_element(By.XPATH, LoginPageLocators.login_input).send_keys(UserLoginData.login)
        driver.find_element(By.XPATH, LoginPageLocators.password_input).send_keys(UserLoginData.password)
        driver.find_element(By.XPATH, LoginPageLocators.login_button).click()
        WebDriverWait(driver, 5) \
            .until(expected_conditions.visibility_of_element_located((By.XPATH, MainPageLocators.order_button)))
        assert driver.current_url == UrlPageData.main_page \
               and expected_conditions.element_to_be_clickable((By.XPATH, MainPageLocators.order_button))
