import allure

from src.test_frameworks.pages.main_page_ui import open_main_page, check_main_page, find_announce, click_announce

@allure.epic('Main page')
class TestMainPage:
    @allure.story('Open main page')
    @allure.title('Main page should be shown')
    @allure.feature('Main page')
    @allure.label('microservice', 'Main page')
    @allure.label('owner', 'allure8')
    @allure.tag('smoke', 'regress', 'web', 'critical')
    @allure.severity('critical')
    @allure.label('layer', 'web')
    def test_open_main_page(self):
        # GIVEN
        open_main_page()

        # THEN
        check_main_page()

    @allure.story('Open announce page')
    @allure.title('Announce page should be shown')
    @allure.feature('Announce page')
    @allure.label('microservice', 'Announce page')
    @allure.label('owner', 'allure8')
    @allure.tag('smoke', 'regress', 'web', 'critical')
    @allure.severity('critical')
    @allure.label('layer', 'web')
    def test_open_announce(self):
        # GIVEN
        open_main_page()

        # WHEN
        click_announce()

        # THEN
        find_announce()
