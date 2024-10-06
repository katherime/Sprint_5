import urls_for_tests
from locators import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestTransationFromPersonalCabinet:

    def test_transation_from_personal_cabinet_to_constructor(self, driver, open_main_stellar_burgers, login):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.MAIN_H1_CONSTRUCTOR))
        driver.find_element(*TestLocators.BUTTON_PERSONAL_CABINET).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_EXIT_FROM_ACCOUNT))
        driver.find_element(*TestLocators.BUTTON_CONSTRUCTOR).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.MAIN_H1_CONSTRUCTOR))
        assert driver.current_url == urls_for_tests.stellar_burgers_main
        driver.quit()

    def test_transation_from_personal_cabinet_to_logotype(self, driver, open_main_stellar_burgers, login):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.MAIN_H1_CONSTRUCTOR))
        driver.find_element(*TestLocators.BUTTON_PERSONAL_CABINET).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_EXIT_FROM_ACCOUNT))
        driver.find_element(*TestLocators.BUTTON_LOGOTYPE).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.MAIN_H1_CONSTRUCTOR))
        assert driver.current_url == urls_for_tests.stellar_burgers_main
        driver.quit()