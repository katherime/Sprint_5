import urls_for_tests
from locators import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestPersonalCabinet:

    def test_entering_to_personal_cabinet(self, driver, open_main_stellar_burgers, login):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.MAIN_H1_CONSTRUCTOR))
        driver.find_element(*TestLocators.BUTTON_PERSONAL_CABINET).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_EXIT_FROM_ACCOUNT))
        assert driver.current_url == urls_for_tests.stellar_burgers_personal_cabinet


    def test_exit_from_account(self, driver, open_main_stellar_burgers, login):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.MAIN_H1_CONSTRUCTOR))
        driver.find_element(*TestLocators.BUTTON_PERSONAL_CABINET).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_EXIT_FROM_ACCOUNT))
        driver.find_element(*TestLocators.BUTTON_EXIT_FROM_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.ENTER_AFTER_REGISTRATION))
        assert driver.current_url == urls_for_tests.stellar_burgers_login
