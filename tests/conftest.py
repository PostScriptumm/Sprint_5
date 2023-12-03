import pytest
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options

from tests.locators import LoginPageLocators, MainPageLocators, PersonalPageLocators
from tests.data import UserLoginData, UrlPageData

# фикстура options
@pytest.fixture
def options():
    options = Options()
    options.add_argument("--windows-size=1920,1080")
    options.add_argument("--headless")
    return options


# фикстура setup_teardown
@pytest.fixture
def driver(options):
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


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


# фикстура логирования существующего пользователя в системе
@pytest.fixture
def login(driver):
    driver.get(UrlPageData.login_page)
    driver.find_element(By.XPATH, LoginPageLocators.login_input).send_keys(UserLoginData.login)
    driver.find_element(By.XPATH, LoginPageLocators.password_input).send_keys(UserLoginData.password)
    driver.find_element(By.XPATH, LoginPageLocators.login_button).click()
    WebDriverWait(driver, 5) \
        .until(expected_conditions.visibility_of_element_located((By.XPATH, MainPageLocators.order_button)))
    return driver


# фикстура перехода к разделу "Начинки" на главной
@pytest.fixture
def go_to_fillings(driver, login):
    driver.find_element(By.XPATH, MainPageLocators.fillings_button).click()
    WebDriverWait(driver, 5) \
        .until(expected_conditions.visibility_of_element_located((By.XPATH, MainPageLocators.fillings_button_activ)))
    return driver


# фикстура перехода в "Личный кабинет" с главной страницы
@pytest.fixture
def go_to_personal(driver, login):
    driver.find_element(By.XPATH, MainPageLocators.main_account_button).click()
    WebDriverWait(driver, 5) \
        .until(expected_conditions.visibility_of_element_located((By.XPATH, PersonalPageLocators.change_personal_data)))
    return driver
