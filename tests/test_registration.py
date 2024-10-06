import urls_for_tests
from locators import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from generator_data_for_login import *


class TestRegistration:

    def test_registration_success(self, driver, open_registration_stellar_burgers):
        driver.find_element(*TestLocators.NAME_INPUT_FIELD).send_keys('Катя')
        driver.find_element(*TestLocators.EMAIL_INPUT_FIELD).send_keys(generate_login())
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD).send_keys(generate_password())
        driver.find_element(*TestLocators.BUTTON_REGISTRATION).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.ENTER_AFTER_REGISTRATION))
        assert driver.current_url == urls_for_tests.stellar_burgers_login
        driver.quit()

    def test_registration_with_wrong_password(self, driver, open_registration_stellar_burgers):
        driver.find_element(*TestLocators.NAME_INPUT_FIELD).send_keys('Катя')
        driver.find_element(*TestLocators.EMAIL_INPUT_FIELD).send_keys(generate_login())
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD).send_keys(generate_password(2))
        driver.find_element(*TestLocators.BUTTON_REGISTRATION).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.WARNING_WRONG_PASSWORD))
        assert driver.current_url == urls_for_tests.stellar_burgers_registration
        driver.quit()
