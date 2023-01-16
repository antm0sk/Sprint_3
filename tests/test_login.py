from conftest import SITE_NAME, GOOD_LOGIN, GOOD_PASSWORD
from locators import MainPageLocators, LoginPageLocators, ForgotPasswordPageLocators
from conftest import webdriver_wait


class TestLogIn:
    def test_login_from_main_page_use_login_button_true(self, driver):
        driver.get(SITE_NAME)
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        webdriver_wait(driver, LoginPageLocators.MAIN_HEADER)
        driver.find_element(*LoginPageLocators.INPUT_LOGIN).send_keys(GOOD_LOGIN)
        driver.find_element(*LoginPageLocators.INPUT_PASSWORD).send_keys(GOOD_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        webdriver_wait(driver, MainPageLocators.PERSON_ACCOUNT_LINK)
        to_check = driver.find_element(*MainPageLocators.PERSON_ACCOUNT_LINK).text
        assert 'Личный Кабинет' == to_check

    def test_login_from_main_page_use_personal_account_link_true(self, driver):
        driver.get(SITE_NAME)
        driver.find_element(*MainPageLocators.PERSON_ACCOUNT_LINK).click()
        webdriver_wait(driver, LoginPageLocators.MAIN_HEADER)
        driver.find_element(*LoginPageLocators.INPUT_LOGIN).send_keys(GOOD_LOGIN)
        driver.find_element(*LoginPageLocators.INPUT_PASSWORD).send_keys(GOOD_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        webdriver_wait(driver, MainPageLocators.PERSON_ACCOUNT_LINK)
        to_check = driver.find_element(*MainPageLocators.PERSON_ACCOUNT_LINK).text
        assert 'Личный Кабинет' == to_check

    def test_login_from_register_page_use_login_button_true(self, driver):
        driver.get(SITE_NAME + 'register')
        driver.find_element(*MainPageLocators.PERSON_ACCOUNT_LINK).click()
        webdriver_wait(driver, LoginPageLocators.MAIN_HEADER)
        driver.find_element(*LoginPageLocators.INPUT_LOGIN).send_keys(GOOD_LOGIN)
        driver.find_element(*LoginPageLocators.INPUT_PASSWORD).send_keys(GOOD_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        webdriver_wait(driver, MainPageLocators.PERSON_ACCOUNT_LINK)
        to_check = driver.find_element(*MainPageLocators.PERSON_ACCOUNT_LINK).text
        assert 'Личный Кабинет' == to_check

    def test_login_from_forgot_password_page_use_login_button_true(self, driver):
        driver.get(SITE_NAME + 'forgot-password')
        driver.find_element(*ForgotPasswordPageLocators.LOGIN_BUTTON).click()
        webdriver_wait(driver, LoginPageLocators.MAIN_HEADER)
        driver.find_element(*LoginPageLocators.INPUT_LOGIN).send_keys(GOOD_LOGIN)
        driver.find_element(*LoginPageLocators.INPUT_PASSWORD).send_keys(GOOD_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        webdriver_wait(driver, MainPageLocators.PERSON_ACCOUNT_LINK)
        to_check = driver.find_element(*MainPageLocators.PERSON_ACCOUNT_LINK).text
        assert 'Личный Кабинет' == to_check
