
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators


class TestLogin:

    def login_with_right_data(self, driver):
        driver.find_element(*TestLocators.EMAIL_INPUT_FIELD).send_keys('medved_14@yandex.ru')
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD).send_keys('123456')
        driver.find_element(*TestLocators.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.MAIN_H1_CONSTRUCTOR))

    def test_login_to_account_by_button_enter_on_main(self, driver, open_main_stellar_burgers):
        driver.find_element(*TestLocators.BUTTON_ENTER_TO_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.ENTER_AFTER_REGISTRATION))
        self.login_with_right_data(driver)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.MAIN_H1_CONSTRUCTOR))
        assert driver.find_element(*TestLocators.BUTTON_MAKE_ORDER)
        driver.quit()

    def test_login_to_account_by_button_personal_cabinet(self, driver, open_main_stellar_burgers):
        driver.find_element(*TestLocators.BUTTON_PERSONAL_CABINET).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.ENTER_AFTER_REGISTRATION))
        self.login_with_right_data(driver)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.MAIN_H1_CONSTRUCTOR))
        assert driver.find_element(*TestLocators.BUTTON_MAKE_ORDER)
        driver.quit()

    def test_login_to_account_by_form_of_registration(self, driver, open_registration_stellar_burgers):
        driver.find_element(*TestLocators.BUTTON_LOGIN_TO_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.ENTER_AFTER_REGISTRATION))
        self.login_with_right_data(driver)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.MAIN_H1_CONSTRUCTOR))
        assert driver.find_element(*TestLocators.BUTTON_MAKE_ORDER)
        driver.quit()

    def test_login_to_account_by_form_of_recovery_password(self, driver,open_recovery_password_stellar_burgers):
        driver.find_element(*TestLocators.BUTTON_LOGIN_TO_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.ENTER_AFTER_REGISTRATION))
        self.login_with_right_data(driver)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.MAIN_H1_CONSTRUCTOR))
        assert driver.find_element(*TestLocators.BUTTON_MAKE_ORDER)
        driver.quit()

