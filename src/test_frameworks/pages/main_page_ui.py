import allure
from selene import browser, have, be
from allure import step


def open_main_page():
    with step('Открыть главную страницу'):
        browser.element('/')

def check_main_page():
    with step('Фильмы - отображается в верхнем меню'):
        browser.element('#topnav-menu').should(have.text('Фильмы'))

def click_announce():
    with step('Кликнуть по аннонсам'):
        browser.element('#top-nav').should(have.text('Анонсы')).click()

def find_announce():
    with step('Откроется страница аннонсов'):
        browser.element('.b-container').should(have.text('Трейлеры фильмов 2023 и 2024 года'))

def find_register():
    with step('Поиск регистрации на главной странице'):
        browser.element('.b-tophead__register').should(have.text('РЕГИСТРАЦИЯ')).click()

def check_speed_register():
    with step('Поиск заголовка Быстрая регистрация'):
        browser.element('#register-popup').should(have.text('БЫСТРАЯ РЕГИСТРАЦИЯ'))