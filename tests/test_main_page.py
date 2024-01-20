import allure
from test_frameworks.pages.main_page_ui import main_page

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
    main_page.check_main_page()
    main_page.find_change_theme()

    # THEN
    main_page.check_theme()

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
    main_page.click_announce()

    # THEN
    main_page.find_announce()
