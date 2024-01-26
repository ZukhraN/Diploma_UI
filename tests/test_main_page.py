import allure
from hdrezka_ui_project_tests.pages.main_page_ui import main


@allure.story('Open main page')
@allure.title('Main page should be shown')
@allure.feature('Main page')
@allure.label('microservice', 'Main page')
@allure.label('owner', 'allure8')
@allure.tag('smoke', 'regress', 'web', 'critical')
@allure.severity('critical')
@allure.label('layer', 'web')
def test_check_theme(open_main_page):
    # WHEN
    main.check_main_page()
    main.find_change_theme()

    # THEN
    main.check_theme()


@allure.story('Open announce page')
@allure.title('Announce page should be shown')
@allure.feature('Announce page')
@allure.label('microservice', 'Announce page')
@allure.label('owner', 'allure8')
@allure.tag('smoke', 'regress', 'web', 'critical')
@allure.severity('critical')
@allure.label('layer', 'web')
def test_open_announce(open_main_page):
    # WHEN
    main.click_announce()

    # THEN
    main.find_announce()
