import pytest
import secrets
import string

from random import randint
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import MainPageLocators, LoginPageLocators


COGORTA_ID = "06"
EMAIL_DOMAIN = "yandex.ru"
EMAIL_USER = "antonmoskovskiy"

SITE_NAME = "https://stellarburgers.nomoreparties.site/"
USER_NAME = "Антон Московский"
BAD_PASSWORD = "123"

GOOD_LOGIN = "antonmoskovskiy_06555@yandex.ru"
GOOD_PASSWORD = "123456"

TIME_TO_WAIT_ELEMENTS = 5


def generate_password():
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(6))
    return password


def generate_login():
    return EMAIL_USER + COGORTA_ID + str(randint(111, 999)) + "@" + EMAIL_DOMAIN


def webdriver_wait(driver_to_use, locator):
    WebDriverWait(driver_to_use, TIME_TO_WAIT_ELEMENTS).until(
        expected_conditions.visibility_of_element_located(locator))


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(SITE_NAME)

    yield driver

    driver.quit()


@pytest.fixture()
def driver_logged():
    driver_logged = webdriver.Chrome()
    driver_logged.maximize_window()
    driver_logged.get(SITE_NAME)
    driver_logged.find_element(*MainPageLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver_logged, 5).until(
        expected_conditions.visibility_of_element_located(LoginPageLocators.MAIN_HEADER))
    driver_logged.find_element(*LoginPageLocators.INPUT_LOGIN).send_keys(GOOD_LOGIN)
    driver_logged.find_element(*LoginPageLocators.INPUT_PASSWORD).send_keys(GOOD_PASSWORD)
    driver_logged.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    yield driver_logged

    driver_logged.quit()
