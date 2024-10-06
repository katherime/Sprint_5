import pytest
import urls_for_tests
from locators import TestLocators
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def open_main_stellar_burgers(driver):
    driver.get(urls_for_tests.stellar_burgers_main)
    return driver


@pytest.fixture
def open_registration_stellar_burgers(driver):
    driver.get(urls_for_tests.stellar_burgers_registration)
    return driver


@pytest.fixture
def open_recovery_password_stellar_burgers(driver):
    driver.get(urls_for_tests.stellar_burgers_recovery_password)
    return driver


@pytest.fixture
def login(driver):
    driver.get(urls_for_tests.stellar_burgers_login)
    driver.find_element(*TestLocators.BUTTON_PERSONAL_CABINET).click()
    driver.find_element(*TestLocators.EMAIL_INPUT_FIELD).send_keys('medved_14@yandex.ru')
    driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD).send_keys('123456')
    driver.find_element(*TestLocators.BUTTON_ENTER).click()
