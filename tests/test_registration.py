from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from tests.locators import (reg_name_input, reg_login_input, reg_pass_input, register_button, login_button_text,
                            incorrect_password_message)


class TestRegistration:

    def test_successful_registration(self, generate_login, generate_password, options):
        driver = webdriver.Chrome(options=options)
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(By.XPATH, reg_name_input).send_keys('Name')
        driver.find_element(By.XPATH, reg_login_input).send_keys(generate_login)
        driver.find_element(By.XPATH, reg_pass_input).send_keys(generate_password)
        driver.find_element(By.XPATH, register_button).click()
        WebDriverWait(driver, 5) \
            .until(expected_conditions.visibility_of_element_located((By.XPATH, login_button_text)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quit()

    def test_registration_failure_message(self, generate_login, options):
        driver = webdriver.Chrome(options=options)
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(By.XPATH, reg_name_input).send_keys('Name')
        driver.find_element(By.XPATH, reg_login_input).send_keys(generate_login)
        driver.find_element(By.XPATH, reg_pass_input).send_keys('pass')
        driver.find_element(By.XPATH, register_button).click()
        WebDriverWait(driver, 5) \
            .until(expected_conditions.presence_of_element_located((By.XPATH, incorrect_password_message)))
        assert (driver.find_element(By.XPATH, incorrect_password_message).text == 'Некорректный пароль')
        driver.quit()
