from selenium.webdriver.common.by import By


class LoginPageLocators():
    MAIN_HEADER = (By.XPATH, "//h2[text()='Вход']") # заголовок Вход
    INPUT_LOGIN = (By.XPATH, "//input[@name='name']") # форма для ввода логина
    INPUT_PASSWORD = (By.XPATH, "//input[@name='Пароль']") # форма для ввода пароля
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']") # кнопка для логина


class RegistrationPageLocators():
    INPUT_LOGIN_AND_USERNAME = (By.XPATH, "//input[@name='name']") # форма для ввода логина и имя пользователя
    INPUT_PASSWORD = (By.XPATH, "//input[@name='Пароль']") # форма для ввода пароля
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']") # кнопка для регистрации
    INCORRECT_PASSWORD = (By.XPATH, "//p[text()='Некорректный пароль']") # поле для проверки неправильного пароля
    LOGIN_BUTTON = (By.XPATH, "// a[text()='Войти']") # кнопка для логина


class MainPageLocators():
    LOGIN_BUTTON = (By.XPATH, "// button[text() = 'Войти в аккаунт']") # кнопка для логина
    PERSON_ACCOUNT_LINK = (By.XPATH, "// p[text()='Личный Кабинет']") # линк на персональный кабинет
    CONSTRUCTOR_HEADER = (By.XPATH, "// h1[text()='Соберите бургер']") # хидер на сборку бургера
    SELECTED_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect')]/span")
    # блог с ингридиентами, для проверки что он активен
    LOAF_TAB = (By.XPATH, "//span[text()='Булки']") # таба с булками
    LOAF_HEADER = (By.XPATH, "//h2[text()='Булки']") # хидер с булками
    SAUCE_TAB = (By.XPATH, "//span[text()='Соусы']") # таба с соусами
    SAUCE_HEADER = (By.XPATH, "//h2[text()='Соусы']") # хидер с соусами
    FILLING_TAB = (By.XPATH, "//span[text()='Начинки']") # таба с начинками
    FILLING_HEADER = (By.XPATH, "//h2[text()='Начинки']") # хидер с начинками


class ForgotPasswordPageLocators():
    LOGIN_BUTTON = (By.XPATH, "// a[text()='Войти']") # кнопка для лоигна


class PersonalAccountLocators():
    LOGIN_BUTTON = (By.XPATH, "// p[text()='В этом разделе вы можете изменить свои персональные данные']")
    # ^^ кнопка для логина
    CONSTRUCTOR_BUTTON = (By.XPATH, "// p[text()='Конструктор']") # кнопка для перехода в конструктор
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']") # кнопка для выхода из аккаунта
