import os
import allure
from test_frameworks.pages.authorization_page import authorization_page

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
    authorization_page.find_register()
    authorization_page.check_speed_register()
    authorization_page.input_email(login_auth)

    # THEN
    authorization_page.check_information_email()

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
    authorization_page.find_login()
    authorization_page.find_label_login()
    authorization_page.input_login(login_auth)
    authorization_page.input_password(password_auth)

    # THEN
    authorization_page.check_authorization()

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
    authorization_page.find_login()
    authorization_page.find_label_login()
    authorization_page.input_login(login_auth)
    authorization_page.input_incorrect_password(wrong_password)

    # THEN
    authorization_page.check_authorization_negotiv()