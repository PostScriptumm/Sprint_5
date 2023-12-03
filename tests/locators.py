# Страница регистрации "https://stellarburgers.nomoreparties.site/register"
class RegPageLocators:

    reg_login_button = ".//a[@href='/login']"  # кнопка "Войти"
    reg_name_input = ".//label[text()='Имя']/following-sibling::input"  # поле ввода имени
    reg_login_input = ".//label[text()='Email']/following-sibling::input"  # поле ввода логина
    reg_pass_input = ".//label[text()='Пароль']/following-sibling::input"  # поле ввода пароля
    register_button = ".//button[text()='Зарегистрироваться']"  # кнопка "Зарегистрироваться"
    incorrect_password_message = ".//p[text()='Некорректный пароль']"  # сообщение 'Некорректный пароль'


# Страница входа 'https://stellarburgers.nomoreparties.site/login'
class LoginPageLocators:

    login_button = ".//button[text()='Войти']"  # кнопка "Войти"
    login_button_text = ".//h2[text()='Вход']"  # надпись "Вход"
    login_input = ".//label[text()='Email']/following-sibling::input"  # поле ввода логина
    password_input = ".//label[text()='Пароль']/following-sibling::input"  # поле ввода пароля


# Страница конструктора/главная 'https://stellarburgers.nomoreparties.site/'
class MainPageLocators:

    order_button = ".//button[text()='Оформить заказ']"  # кнопка "Оформить заказ"
    main_login_button = ".//button[text()='Войти в аккаунт']"  # кнопка "Войти в аккаунт"
    main_account_button = ".//p[text()='Личный Кабинет']"  # кнопка "Личный кабинет"
    stellar_burgers_logo = ".//div[@class='AppHeader_header__logo__2D0X2']"  # логотип "Stellar Burgers"
    constructor_button = ".//p[text()='Конструктор']"  # кнопка "Конструктор"
    collect_burger = ".//h1[text()='Соберите бургер']"  # надпись "Соберите бургер"
    fillings_button = ".//span[text()='Начинки']/parent::div"  # кнопка "Начинки"
    fillings_button_activ = \
        ".//div[3][@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']"
    # кнопка "Начинки" если она выбрана
    sauces_button = ".//span[text()='Соусы']/parent::div"  # кнопка "Соусы"
    sauces_button_activ = \
        ".//div[2][@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']"
    # кнопка "Соусы" если она выбрана
    buns_button = ".//span[text()='Булки']/parent::div"  # кнопка "Булки"
    buns_button_activ = ".//div[1][@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']"
    # кнопка "Булки" если она выбрана


# Страница восстановления пароля 'https://stellarburgers.nomoreparties.site/forgot-password'
class ForgotPassPagelocators:

    forgot_login_button = ".//a[@href='/login']"  # кнопка "Войти"


# Страница личного кабинета 'https://stellarburgers.nomoreparties.site/account/profile'
class PersonalPageLocators:

    account_exit_button = ".//button[text()='Выход']"  # кнопка "Выход"
    change_personal_data = ".//p[text()='В этом разделе вы можете изменить свои персональные данные']"
    # надпись "В этом разделе вы можете изменить свои персональные данные"
