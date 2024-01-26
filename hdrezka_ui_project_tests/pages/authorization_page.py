from selene import browser, have, be
from allure import step


class Authorization:
    def find_register(self):
        with step('Поиск регистрации на главной странице'):
            browser.element('.b-tophead__register').should(have.text('РЕГИСТРАЦИЯ')).click()

    def check_speed_register(self):
        with step('Поиск заголовка Быстрая регистрация'):
            browser.element('#register-popup').should(have.text('БЫСТРАЯ РЕГИСТРАЦИЯ'))

    def check_field_email(self):
        with step('Поиск поля email'):
            browser.element('#email').should(be.empty)

    def input_email(self, login_auth):
        with step('Ввод в поле email данных'):
            browser.element('#email').should(be.visible).send_keys(login_auth)

    def check_information_email(self):
        with step('Проверка существует ли такая учетка с этим эмейлом'):
            browser.element('.string-error').should(have.text('Данный email уже зарегистрирован'))

    def find_login(self):
        with step('Поиск вход на главной странице'):
            browser.element('.b-tophead__login').should(have.text('ВХОД')).click()

    def find_label_login(self):
        with step('Поиск заголовка Вход на сайт'):
            browser.element('#login-popup').should(have.text('ВХОД НА САЙТ'))

    def input_login(self, login_auth):
        with step('Ввод в поле логин'):
            browser.element('#login_name').should(be.visible).send_keys(login_auth)

    def input_password(self, password_auth):
        with step('Ввод в поле пароль'):
            browser.element('#login_password').should(be.visible).send_keys(password_auth).press_enter()

    def input_incorrect_password(self, wrong_password):
        with step('Ввод в поле пароль'):
            browser.element('#login_password').should(be.visible).send_keys(wrong_password).press_enter()

    def check_authorization(self):
        with step('Проверка авторизации под своей учеткой'):
            browser.element('.b-tophead-right').should(have.text('МОИ ЗАКЛАДКИ'))

    def check_authorization_negotiv(self):
        with step('Проверка авторизации под своей учеткой'):
            browser.element('#login-popup-errors').should(have.text('Введен неверный логин или пароль.'))


authorization = Authorization()
