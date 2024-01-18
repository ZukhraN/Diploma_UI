import pytest
import os

from allure_commons._allure import attach
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#from test_frameworks.utils import allure_attach

@pytest.fixture(scope='function')
def setup_browser(request):
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    browser_url = os.getenv('DEFAULT_BROWSER_URL')

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@{browser_url}",
        options=options
    )
    browser.config.driver = driver
    browser.config.base_url = "https://hdrezka.ag/"
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
