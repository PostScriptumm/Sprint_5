В проекте написаны UI тесты для сервиса Stellar Burger https://stellarburgers.nomoreparties.site/ согласно заданию

Для написания тестов используются библиотека Selenium.webdriver(Chrome) и pytest

Для входа в систему используются данные:
login - 'andreytebenkov3000@yandex.ru'
password - 'password'

Содержание проекта:

README - описание проекта

data - файл с адресами используемых страниц и данными для логина пользователя

conftest - файл с фикстурами

locators - файл с локаторами

test_registeration - файл содержит следующие проверки:
test_successful_registration - Успешную регистрацию. Поле «Имя» должно быть не пустым; в поле Email введён email в формате логин@домен: например, 123@ya.ru. Минимальный пароль — шесть символов.
test_registration_failure_message - Ошибку для некорректного пароля.

test_login - файл содержит следующие проверки:
test_login_from_main_register_forgot_password_pages - 
вход по кнопке «Войти в аккаунт» на главной,
вход через кнопку «Личный кабинет»,
вход через кнопку в форме регистрации,
вход через кнопку в форме восстановления пароля.

test_personal_account - файл содержит следующие проверки:
test_button_personal_account - Проверь переход по клику на «Личный кабинет».
test_button_exit_in_personal_account - роверь выход по кнопке «Выйти» в личном кабинете.
test_go_to_constructor_from_personal_account - Проверь переход по клику на «Конструктор» и на логотип Stellar Burgers.

test_constructor - файл содержит следующие проверки:
Проверь, что работают переходы к разделам:
test_go_to_buns - Булки
test_go_to_sauces - Соусы
test_go_to_fillings - Начинки
