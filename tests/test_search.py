import allure
from test_frameworks.pages.search_page import search_page

@allure.title('Search page should be shown')
@allure.feature('Search page')
@allure.label('microservice', 'Search page')
@allure.label('owner', 'allure8')
@allure.tag('smoke', 'regress', 'web', 'critical')
@allure.severity('critical')
@allure.label('layer', 'web')
def test_search_movie(open_main_page):
    # WHEN
    search_page.input_name_movie()

    # THEN
    search_page.check_result_search()

@allure.title('Search page should be shown')
@allure.feature('Search page')
@allure.label('microservice', 'Search page')
@allure.label('owner', 'allure8')
@allure.tag('smoke', 'regress', 'web', 'critical')
@allure.severity('critical')
@allure.label('layer', 'web')
def test_search_incorrect_movie(open_main_page):
    # WHEN
    search_page.input_incorrect_movie()

    # THEN
    search_page.check_incorrect_result_search()