import allure

from src.test_frameworks.pages.main_page_ui import open_main_page
from src.test_frameworks.pages.search_page import input_name_movie, check_result_search, check_incorrect_result_search, \
    input_incorrect_movie

@allure.epic('Search page')
class TestSearchPage:
    @allure.title('Search page should be shown')
    @allure.feature('Search page')
    @allure.label('microservice', 'Search page')
    @allure.label('owner', 'allure8')
    @allure.tag('smoke', 'regress', 'web', 'critical')
    @allure.severity('critical')
    @allure.label('layer', 'web')
    def test_search_movie(self):
        # GIVEN
        open_main_page()

        # WHEN
        input_name_movie()

        # THEN
        check_result_search()

    @allure.title('Search page should be shown')
    @allure.feature('Search page')
    @allure.label('microservice', 'Search page')
    @allure.label('owner', 'allure8')
    @allure.tag('smoke', 'regress', 'web', 'critical')
    @allure.severity('critical')
    @allure.label('layer', 'web')
    def test_search_incorrect_movie(self):
        # GIVEN
        open_main_page()

        # WHEN
        input_incorrect_movie()

        # THEN
        check_incorrect_result_search()