import os
import allure
from hdrezka_ui_project_tests.pages.authorization_page import authorization
from dotenv import load_dotenv

load_dotenv()
login_auth = os.getenv("login_auth")
password_auth = os.getenv("password_auth")
wrong_password = os.getenv("wrong_password")


@allure.story('Open registration page')
@allure.title('Registration page should be shown')
@allure.feature('Registration page')
@allure.label('microservice', 'Registration page')
@allure.label('owner', 'allure8')
@allure.tag('smoke', 'regress', 'web', 'critical')
@allure.severity('critical')
@allure.label('layer', 'web')
def test_failed_registration(open_main_page):
    # WHEN
    authorization.find_register()
    authorization.check_speed_register()
    authorization.input_email(login_auth)

    # THEN
    authorization.check_information_email()


@allure.story('Open authorization page')
@allure.title('Authorization page should be shown')
@allure.feature('Authorization page')
@allure.label('microservice', 'Authorization page')
@allure.label('owner', 'allure8')
@allure.tag('smoke', 'regress', 'web', 'critical')
@allure.severity('critical')
@allure.label('layer', 'web')
def test_successful_authorization(open_main_page):
    # WHEN
    authorization.find_login()
    authorization.find_label_login()
    authorization.input_login(login_auth)
    authorization.input_password(password_auth)

    # THEN
    authorization.check_authorization()


@allure.story('Open authorization page')
@allure.title('Authorization page should be shown and failed')
@allure.feature('Authorization page')
@allure.label('microservice', 'Authorization page')
@allure.label('owner', 'allure8')
@allure.tag('smoke', 'regress', 'web', 'critical')
@allure.severity('critical')
@allure.label('layer', 'web')
def test_failed_authorization(open_main_page):
    # WHEN
    authorization.find_login()
    authorization.find_label_login()
    authorization.input_login(login_auth)
    authorization.input_incorrect_password(wrong_password)

    # THEN
    authorization.check_authorization_negotiv()
