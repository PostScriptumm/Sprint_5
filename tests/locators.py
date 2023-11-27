# Страница регистрации "https://stellarburgers.nomoreparties.site/register"
reg_login_button = './/div[1]/div/main/div/div/p/a'  # кнопка "Войти"
reg_name_input = ".//fieldset[1]/div/div/input"  # поле ввода имени
reg_login_input = ".//fieldset[2]/div/div/input"  # поле ввода логина
reg_pass_input = ".//fieldset[3]/div/div/input"  # поле ввода пароля
register_button = ".//button[text()='Зарегистрироваться']"  # кнопка "Зарегистрироваться"
incorrect_password_message = ".//div[1]/div/main/div/form/fieldset[3]/div/p"  # сообщение 'Некорректный пароль'

# Страница входа 'https://stellarburgers.nomoreparties.site/login'
login_button = ".//div[1]/div/main/div/form/button"  # кнопка "Вход"
login_button_text = ".//h2[text()='Вход']"  # текст кнопки "Вход"
login_input = ".//fieldset[1]/div/div/input"  # поле ввода логина
password_input = ".//fieldset[2]/div/div/input"  # поле ввода пароля

# Страница конструктора/главная 'https://stellarburgers.nomoreparties.site/'
order_button = ".//div[1]/div/main/section[2]/div/button"  # кнопка "Оформить заказ"
main_login_button = './/div[1]/div/main/section[2]/div/button'  # кнопка "Войти в аккаунт"
main_account_button = './/div[1]/div/header/nav/a'  # кнопка "Личный кабинет"
stellar_burgers_logo = './/div[1]/div/header/nav/div'  # логотип "Stellar Burgers"
constructor_button = './/div[1]/div/header/nav/ul/li[1]/a'  # кнопка "Конструктор"
collect_burger = ".//div[1]/div/main/section[1]/h1"  # надпись "Соберите бургер"
fillings_button = ".//div[1]/div/main/section[1]/div[1]/div[3]"  # кнопка "Начинки"
fillings_button_activ = ".//div[3][@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']"
# кнопка "Начинки" если она выбрана
sauces_button = ".//div[1]/div/main/section[1]/div[1]/div[2]"  # кнопка "Соусы"
sauces_button_activ = ".//div[2][@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']"
# кнопка "Соусы" если она выбрана
buns_button = ".//div[1]/div/main/section[1]/div[1]/div[1]"  # кнопка "Булки"
buns_button_activ = ".//div[1][@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']"
# кнопка "Булки" если она выбрана

# Страница восстановления пароля 'https://stellarburgers.nomoreparties.site/forgot-password'
forgot_login_button = './/div[1]/div/main/div/div/p/a'  # кнопка "Войти"

# Страница личного кабинета 'https://stellarburgers.nomoreparties.site/account/profile'
account_exit_button = './/div[1]/div/main/div/nav/ul/li[3]/button'  # кнопка "Выйти"
change_personal_data = ".//div[1]/div/main/div/nav/p"
# надпись "В этом разделе вы можете изменить свои персональные данные"
