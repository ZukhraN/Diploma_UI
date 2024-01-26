import allure
from hdrezka_ui_project_tests.pages.search_page import search


@allure.title('Search page should be shown correct results')
@allure.feature('Search page')
@allure.label('microservice', 'Search page')
@allure.label('owner', 'allure8')
@allure.tag('smoke', 'regress', 'web', 'critical')
@allure.severity('critical')
@allure.label('layer', 'web')
def test_search_movie(open_main_page):
    # WHEN
    search.input_name_movie()

    # THEN
    search.check_result_search()


@allure.title('Search page should be shown no results')
@allure.feature('Search page')
@allure.label('microservice', 'Search page')
@allure.label('owner', 'allure8')
@allure.tag('smoke', 'regress', 'web', 'critical')
@allure.severity('critical')
@allure.label('layer', 'web')
def test_search_incorrect_movie(open_main_page):
    # WHEN
    search.input_incorrect_movie()

    # THEN
    search.check_incorrect_result_search()
