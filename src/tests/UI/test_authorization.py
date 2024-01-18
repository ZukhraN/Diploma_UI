import os
import allure

from src.test_frameworks.pages.main_page_ui import open_main_page
from src.test_frameworks.pages.authorization_page import find_register, check_speed_register, input_email, \
    check_information_email, find_login, find_label_login,  input_login, input_password, check_authorization, \
    input_incorrect_password, check_authorization_negotiv

login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")
password_incorrect = os.getenv("PASSWORD_INCORRECT")

@allure.epic('Authorization page')
class TestAuthorizationPage:
    @allure.story('Open registration page')
    @allure.title('Registration page should be shown')
    @allure.feature('Registration page')
    @allure.label('microservice', 'Registration page')
    @allure.label('owner', 'allure8')
    @allure.tag('smoke', 'regress', 'web', 'critical')
    @allure.severity('critical')
    @allure.label('layer', 'web')
    def test_registration_negotiv(self):
        # GIVEN
        open_main_page()

        # WHEN
        find_register()
        check_speed_register()
        input_email()

        # THEN
        check_information_email()

    @allure.story('Open authorization page')
    @allure.title('Authorization page should be shown')
    @allure.feature('Authorization page')
    @allure.label('microservice', 'Authorization page')
    @allure.label('owner', 'allure8')
    @allure.tag('smoke', 'regress', 'web', 'critical')
    @allure.severity('critical')
    @allure.label('layer', 'web')
    def test_authorization_pozotiv(self):
        # GIVEN
        open_main_page()

        # WHEN
        find_login()
        find_label_login()
        input_login()
        input_password()

        # THEN
        check_authorization()

    @allure.story('Open authorization page')
    @allure.title('Authorization page should be shown')
    @allure.feature('Authorization page')
    @allure.label('microservice', 'Authorization page')
    @allure.label('owner', 'allure8')
    @allure.tag('smoke', 'regress', 'web', 'critical')
    @allure.severity('critical')
    @allure.label('layer', 'web')
    def test_authorization_negotiv(self):
        # GIVEN
        open_main_page()

        # WHEN
        find_login()
        find_label_login()
        input_login()
        input_incorrect_password()

        # THEN
        check_authorization_negotiv()