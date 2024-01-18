import allure
from selene import browser, have, be
from allure import step


def find_register():
    with step('Поиск регистрации на главной странице'):
        browser.element('.b-tophead__register').should(have.text('РЕГИСТРАЦИЯ')).click()

def check_speed_register():
    with step('Поиск заголовка Быстрая регистрация'):
        browser.element('#register-popup').should(have.text('БЫСТРАЯ РЕГИСТРАЦИЯ'))

def check_field_email():
    with step('Поиск поля email'):
        browser.element('#email').should(be.empty)

def input_email():
    with step('Ввод в поле email данных'):
        browser.element('#email').should(be.visible).type(login)

def check_information_email():
    with step('Проверка существует ли такая учетка с этим эмейлом'):
        browser.element('.string-error').should(have.text('Данный email уже зарегистрирован'))

def find_login():
    with step('Поиск вход на главной странице'):
        browser.element('.b-tophead__login').should(have.text('ВХОД')).click()

def find_label_login():
    with step('Поиск заголовка Вход на сайт'):
        browser.element('#login-popup').should(have.text('ВХОД НА САЙТ'))

def input_login():
    with step('Ввод в поле логин'):
        browser.element('#login_name').should(be.visible).type(login)

def input_password():
    with step('Ввод в поле пароль'):
        browser.element('#login_password').should(be.visible).type(password).press_enter()

def input_incorrect_password():
    with step('Ввод в поле пароль'):
        browser.element('#login_password').should(be.visible).type('password_incorrect').press_enter()

def check_authorization():
    with step('Проверка авторизации под своей учеткой'):
        browser.element('.b-tophead-right').should(have.text('МОИ ЗАКЛАДКИ'))

def check_authorization_negotiv():
    with step('Проверка авторизации под своей учеткой'):
        browser.element('#login-popup-errors').should(have.text('Введен неверный логин или пароль.'))