from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from tests.locators import MainPageLocators


class TestConstructor:

    def test_go_to_fillings(self, driver, go_to_fillings):
        assert 'tab_tab_type_current__2BEPc' in driver \
            .find_element(By.XPATH, MainPageLocators.fillings_button).get_attribute('class')

    def test_go_to_sauces(self, driver, go_to_fillings):
        driver.find_element(By.XPATH, MainPageLocators.sauces_button).click()
        WebDriverWait(driver, 5) \
            .until(expected_conditions.visibility_of_element_located((By.XPATH, MainPageLocators.sauces_button_activ)))
        assert 'tab_tab_type_current__2BEPc' in driver \
            .find_element(By.XPATH, MainPageLocators.sauces_button).get_attribute('class')

    def test_go_to_buns(self, driver, go_to_fillings):
        driver.find_element(By.XPATH, MainPageLocators.buns_button).click()
        WebDriverWait(driver, 5) \
            .until(expected_conditions.visibility_of_element_located((By.XPATH, MainPageLocators.buns_button_activ)))
        assert 'tab_tab_type_current__2BEPc' in driver \
            .find_element(By.XPATH, MainPageLocators.buns_button).get_attribute('class')
