from locators import MainPageLocators, PersonalAccountLocators
from conftest import webdriver_wait


class TestNavigateToPersonalAccount:
    def test_navigate_to_pesronal_account_true(self, driver_logged):
        webdriver_wait(driver_logged, MainPageLocators.CONSTRUCTOR_HEADER)
        driver_logged.find_element(*MainPageLocators.PERSON_ACCOUNT_LINK).click()
        webdriver_wait(driver_logged, PersonalAccountLocators.LOGIN_BUTTON)
        to_check = driver_logged.find_element(*PersonalAccountLocators.LOGIN_BUTTON).text
        assert 'В этом разделе вы можете изменить свои персональные данные' == to_check
