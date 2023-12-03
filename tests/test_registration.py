from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from tests.locators import RegPageLocators, LoginPageLocators, MainPageLocators
from tests.data import UrlPageData


class TestRegistration:

    def test_successful_registration(self, driver, generate_login, generate_password):
        driver.get(UrlPageData.registration_page)
        driver.find_element(By.XPATH, RegPageLocators.reg_name_input).send_keys('Name')
        driver.find_element(By.XPATH, RegPageLocators.reg_login_input).send_keys(generate_login)
        driver.find_element(By.XPATH, RegPageLocators.reg_pass_input).send_keys(generate_password)
        driver.find_element(By.XPATH, RegPageLocators.register_button).click()
        WebDriverWait(driver, 5) \
            .until(expected_conditions.visibility_of_element_located((By.XPATH, LoginPageLocators.login_button_text)))
        driver.find_element(By.XPATH, LoginPageLocators.login_input).send_keys(generate_login)
        driver.find_element(By.XPATH, LoginPageLocators.password_input).send_keys(generate_password)
        driver.find_element(By.XPATH, LoginPageLocators.login_button).click()
        WebDriverWait(driver, 5) \
            .until(expected_conditions.visibility_of_element_located((By.XPATH, MainPageLocators.order_button)))
        assert driver.current_url == UrlPageData.main_page \
               and expected_conditions.element_to_be_clickable((By.XPATH, MainPageLocators.order_button))

    def test_registration_failure_message(self, driver, generate_login):
        driver.get(UrlPageData.registration_page)
        driver.find_element(By.XPATH, RegPageLocators.reg_name_input).send_keys('Name')
        driver.find_element(By.XPATH, RegPageLocators.reg_login_input).send_keys(generate_login)
        driver.find_element(By.XPATH, RegPageLocators.reg_pass_input).send_keys('pass')
        driver.find_element(By.XPATH, RegPageLocators.register_button).click()
        WebDriverWait(driver, 5) \
            .until(expected_conditions.
                   presence_of_element_located((By.XPATH, RegPageLocators.incorrect_password_message)))
        assert (driver.find_element(By.XPATH, RegPageLocators.incorrect_password_message).text == 'Некорректный пароль')
