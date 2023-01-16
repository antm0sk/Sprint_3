from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import MainPageLocators
from conftest import webdriver_wait


class TestLogIn:
    def test_navigate_to_loaf_true(self, driver_logged):
        webdriver_wait(driver_logged, MainPageLocators.CONSTRUCTOR_HEADER)
        WebDriverWait(driver_logged, 5).until(expected_conditions.element_to_be_clickable(MainPageLocators.LOAF_HEADER))
        to_check = driver_logged.find_element(*MainPageLocators.SELECTED_TAB).text
        assert 'Булки' == to_check

    def test_navigate_to_sauce_true(self, driver_logged):
        webdriver_wait(driver_logged, MainPageLocators.CONSTRUCTOR_HEADER)
        WebDriverWait(driver_logged, 5).until(expected_conditions.element_to_be_clickable(MainPageLocators.LOAF_HEADER))
        driver_logged.find_element(*MainPageLocators.SAUCE_TAB).click()
        WebDriverWait(driver_logged, 5).until(expected_conditions.element_to_be_clickable(MainPageLocators.SAUCE_HEADER))
        to_check = driver_logged.find_element(*MainPageLocators.SELECTED_TAB).text
        assert 'Соусы' == to_check

    def test_navigate_to_filling_true(self, driver_logged):
        webdriver_wait(driver_logged, MainPageLocators.CONSTRUCTOR_HEADER)
        WebDriverWait(driver_logged, 5).until(expected_conditions.element_to_be_clickable(MainPageLocators.LOAF_HEADER))
        driver_logged.find_element(*MainPageLocators.FILLING_TAB).click()
        WebDriverWait(driver_logged, 5).until(expected_conditions.element_to_be_clickable(MainPageLocators.FILLING_HEADER))
        to_check = driver_logged.find_element(*MainPageLocators.SELECTED_TAB).text
        assert 'Начинки' == to_check
