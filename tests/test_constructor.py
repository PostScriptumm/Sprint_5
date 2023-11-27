from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from tests.locators import fillings_button, sauces_button, sauces_button_activ, buns_button, buns_button_activ


class TestConstructor:

    def test_go_to_fillings(self, login_click_fillings):
        driver = login_click_fillings
        assert (driver.find_element(By.XPATH, fillings_button).
                get_attribute('class') == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect')
        driver.quit()

    def test_go_to_sauces(self, login_click_fillings):
        driver = login_click_fillings
        driver.find_element(By.XPATH, sauces_button).click()
        WebDriverWait(driver, 5) \
            .until(expected_conditions.visibility_of_element_located((By.XPATH, sauces_button_activ)))
        assert (driver.find_element(By.XPATH, sauces_button).
                get_attribute('class') == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect')
        driver.quit()

    def test_go_to_buns(self, login_click_fillings):
        driver = login_click_fillings
        driver.find_element(By.XPATH, buns_button).click()
        WebDriverWait(driver, 5) \
            .until(expected_conditions.visibility_of_element_located((By.XPATH, buns_button_activ)))
        assert (driver.find_element(By.XPATH, buns_button).
                get_attribute('class') == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect')
        driver.quit()
