from locators import MainPageLocators, PersonalAccountLocators
from conftest import webdriver_wait


class TestNavigateToPersonalAccount:
    def test_navigate_to_pesronal_account_true(self, driver_logged):
        webdriver_wait(driver_logged, MainPageLocators.CONSTRUCTOR_HEADER)
        driver_logged.find_element(*MainPageLocators.PERSON_ACCOUNT_LINK).click()
        webdriver_wait(driver_logged, PersonalAccountLocators.LOGIN_BUTTON)
        driver_logged.find_element(*PersonalAccountLocators.CONSTRUCTOR_BUTTON).click()
        webdriver_wait(driver_logged, MainPageLocators.CONSTRUCTOR_HEADER)
        to_check = driver_logged.find_element(*MainPageLocators.CONSTRUCTOR_HEADER).text
        assert 'Соберите бургер' == to_check
