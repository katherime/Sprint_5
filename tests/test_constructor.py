from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import TestLocators


class TestTransitionOnTabsinConstructor:

    def check_transition(self, driver, button):
        driver.find_element(*button).click()
        current_element = WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "[class*='current']")))
        assert 'current' in current_element.get_attribute('class')

    def test_transition_to_tab_about_sauses(self, driver, open_main_stellar_burgers):
        self.check_transition(driver, TestLocators.BUTTON_SAUSES)

    def test_transition_to_tab_about_filling(self, driver, open_main_stellar_burgers):
        self.check_transition(driver, TestLocators.BUTTON_FILLING)

    def test_transition_to_tab_about_bread(self, driver, open_main_stellar_burgers):
        driver.find_element(*TestLocators.BUTTON_FILLING).click()
        self.check_transition(driver, TestLocators.BUTTON_BREAD)

