# Автоматизация тестов для сайта https://stellarburgers.nomoreparties.site/

### Для начала работы необходимо:
1. Установить WebDriver: 
```
https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/
Мы используем webdriver, который доступен из PATH
```
2. Установить зависимости из requirements.txt
```
pip3 install -r requirements.txt
```
3. Запустить тесты из корневого каталога проекта:
```
pytest -v ./tests/
```

### Содержимое проекта:
```
README.md - этот файл
requirements.txt - основные зависимости
./tests/ - каталог с тестами
./tests/conftest.py - конфигурация проекта, фикстуры, переиспользуемые функции
./tests/locators.py - локаторы, применяемые в проекте
./tests/test_login.py - тесты аутентификации
./tests/test_logout.py - тесты, проверяющие выход из аккаунта
./tests/test_navigate_from_pa_to_constructor.py - тесты навигации из личного аккаунта в конструктор
./tests/test_navigate_into_constructor.py - тесты навигации по конструктору бургеров
./tests/test_navigate_to_personal_account.py - тесты для проверки навигации в персональный аккаунт
./tests_registration.py - тесты для проверки регистрации
```
