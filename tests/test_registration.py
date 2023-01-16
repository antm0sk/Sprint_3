from selenium.common.exceptions import ElementNotInteractableException
from conftest import SITE_NAME, generate_login, generate_password, USER_NAME, BAD_PASSWORD
from locators import RegistrationPageLocators, LoginPageLocators
from conftest import webdriver_wait


class TestRegistration:
    def test_register_new_user_true(self, driver):
        driver.get(SITE_NAME + 'register')
        driver.find_elements(*RegistrationPageLocators.INPUT_LOGIN_AND_USERNAME)[0].send_keys(USER_NAME)
        driver.find_elements(*RegistrationPageLocators.INPUT_LOGIN_AND_USERNAME)[1].send_keys(generate_login())
        driver.find_element(*RegistrationPageLocators.INPUT_PASSWORD).send_keys(generate_password())
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
        webdriver_wait(driver, LoginPageLocators.MAIN_HEADER)
        current_url = driver.current_url
        assert current_url == SITE_NAME + 'login'

    def test_register_new_user_with_bad_password_false(self, driver):
        driver.get(SITE_NAME + 'register')
        driver.find_elements(*RegistrationPageLocators.INPUT_LOGIN_AND_USERNAME)[0].send_keys(USER_NAME)
        driver.find_elements(*RegistrationPageLocators.INPUT_LOGIN_AND_USERNAME)[1].send_keys(generate_login())
        driver.find_element(*RegistrationPageLocators.INPUT_PASSWORD).send_keys(BAD_PASSWORD)

        try:
            driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
        except ElementNotInteractableException:
            print("the Button to register doesn't work since password is too short")

        response = driver.find_element(*RegistrationPageLocators.INCORRECT_PASSWORD).text
        assert 'Некорректный пароль' == response
