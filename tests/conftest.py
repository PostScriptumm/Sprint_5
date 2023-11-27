import pytest
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options

from tests.locators import (login_input, password_input, login_button, main_account_button, order_button,
                            fillings_button, fillings_button_activ, change_personal_data)


@pytest.fixture
# фикстура options
def options():
    options = Options()
    options.add_argument("--windows-size=1920,1080")
    options.add_argument("--headless")
    return options


# фикстура генерации нового логина(email) для регистрации
@pytest.fixture
def generate_login():
    name_surname = ''.join((random.choice(string.ascii_lowercase) for x in range(12)))
    three_numbers = ''.join((random.choice(string.digits) for x in range(3)))
    return f"{name_surname}3{three_numbers}@yandex.ru"


# фикстура генерации нового пароля для регистрации
@pytest.fixture
def generate_password():
    return ''.join((random.choice(string.ascii_letters + string.digits) for x in range(10)))


# фикстура логирования существующего пользователя в системе и переход в личный кабинет
@pytest.fixture
def login_personal_account(options):
    driver = webdriver.Chrome(options=options)
    driver.get('https://stellarburgers.nomoreparties.site/login')
    driver.find_element(By.XPATH, login_input).send_keys('andreytebenkov3000@yandex.ru')
    driver.find_element(By.XPATH, password_input).send_keys('password')
    driver.find_element(By.XPATH, login_button).click()
    WebDriverWait(driver, 5) \
        .until(expected_conditions.visibility_of_element_located((By.XPATH, order_button)))
    driver.find_element(By.XPATH, main_account_button).click()
    WebDriverWait(driver, 5) \
        .until(expected_conditions.visibility_of_element_located((By.XPATH, change_personal_data)))
    return driver


# фикстура логирования существующего пользователя и переход к разделу "Начинки" на главной
@pytest.fixture
def login_click_fillings(options):
    driver = webdriver.Chrome(options=options)
    driver.get('https://stellarburgers.nomoreparties.site/login')
    driver.find_element(By.XPATH, login_input).send_keys('andreytebenkov3000@yandex.ru')
    driver.find_element(By.XPATH, password_input).send_keys('password')
    driver.find_element(By.XPATH, login_button).click()
    WebDriverWait(driver, 5) \
        .until(expected_conditions.visibility_of_element_located((By.XPATH, order_button)))
    driver.find_element(By.XPATH, fillings_button).click()
    WebDriverWait(driver, 5) \
        .until(expected_conditions.visibility_of_element_located((By.XPATH, fillings_button_activ)))
    return driver
