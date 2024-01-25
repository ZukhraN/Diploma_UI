import allure
from selene import browser, have, be
from allure import step


class Main:
    def check_main_page(self):
        with step('Фильмы - отображается в верхнем меню'):
            browser.element('#topnav-menu').should(have.text('Фильмы'))

    def find_change_theme(self):
        with step('Найти тогл переключения темы'):
            browser.element('.b-theme__switcher').should(be.visible)

    def check_theme(self):
        with step('Проверить переключение на темную тему'):
            browser.element('.has-brand').should(have.css_property('.b-theme__template__night'))

    def click_announce(self):
        with step('Кликнуть по аннонсам'):
            browser.element('#top-nav').should(have.text('Анонсы')).click()

    def find_announce(self):
        with step('Откроется страница аннонсов'):
            browser.element('.b-container').should(have.text('Трейлеры фильмов 2023 и 2024 года'))

    def find_register(self):
        with step('Поиск регистрации на главной странице'):
            browser.element('.b-tophead__register').should(have.text('РЕГИСТРАЦИЯ')).click()

    def check_speed_register(self):
        with step('Поиск заголовка Быстрая регистрация'):
            browser.element('#register-popup').should(have.text('БЫСТРАЯ РЕГИСТРАЦИЯ'))


main_page = Main()
