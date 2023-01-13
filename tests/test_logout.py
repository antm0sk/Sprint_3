from locators import MainPageLocators, LoginPageLocators, PersonalAccountLocators
from conftest import webdriver_wait


class TestNavigateToPersonalAccount:
    def test_logout_true(self, driver_logged):
        webdriver_wait(driver_logged, MainPageLocators.CONSTRUCTOR_HEADER)
        driver_logged.find_element(*MainPageLocators.PERSON_ACCOUNT_LINK).click()
        webdriver_wait(driver_logged, PersonalAccountLocators.LOGIN_BUTTON)
        driver_logged.find_element(*PersonalAccountLocators.LOGOUT_BUTTON).click()
        webdriver_wait(driver_logged, LoginPageLocators.MAIN_HEADER)
        to_check = driver_logged.find_element(*LoginPageLocators.MAIN_HEADER).text
        assert 'Вход' == to_check
