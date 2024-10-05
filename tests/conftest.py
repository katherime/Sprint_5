import pytest
from locators import TestLocators
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def open_main_stellar_burgers(driver):
    driver.get("https://stellarburgers.nomoreparties.site")
    yield driver


@pytest.fixture
def open_registration_stellar_burgers(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    yield driver

@pytest.fixture
def open_recovery_password_stellar_burgers(driver):
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
    yield driver

@pytest.fixture
def login(driver):
    driver.get('https://stellarburgers.nomoreparties.site/login')
    driver.find_element(*TestLocators.BUTTON_PERSONAL_CABINET).click()
    driver.find_element(*TestLocators.EMAIL_INPUT_FIELD).send_keys('medved_14@yandex.ru')
    driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD).send_keys('123456')
    driver.find_element(*TestLocators.BUTTON_ENTER).click()
