import allure
from selene import browser, have, be
from allure import step

def input_name_movie():
    with step('Ввод названия фильма в поле поиска'):
        browser.element('#search-field').should(be.visible).type('Милашка').press_enter()

def check_result_search():
    with step('Страница с результатми поиска'):
        browser.element('.b-content__htitle').should(have.text('Результаты поиска «Милашка»'))

def input_incorrect_movie():
    with step('Ввод названия фильма в поле поиска'):
        browser.element('#search-field').should(be.visible).type('nvfvnmcvkmxkcvm').press_enter()

def check_incorrect_result_search():
    with step('Страница с результатми поиска'):
        browser.element('.b-info__message').should(have.text('Нам не удалось ничего найти. Нет ли грамматических ошибок в запросе?'))