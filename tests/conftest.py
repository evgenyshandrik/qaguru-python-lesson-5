"""
Setup test configurations
"""
import os
import time
import allure
import pytest
import json
from dotenv import load_dotenv

from selene import have, command
from selene.support.shared import browser
from selenium import webdriver

from util.resources import path

DEFAULT_REMOTE_DRIVER = 'selenoid.autotests.cloud'


@pytest.fixture(scope='session', autouse=True)
def load_env():
    """
    Load .env
    """
    load_dotenv()


def pytest_addoption(parser):
    """
    Parser option
    """
    parser.addoption(
        '--remote_driver',
        default='selenoid.autotests.cloud'
    )


@pytest.fixture(scope='session', autouse=True)
def set_up_config_notification():
    """
    Set up config notification
    """
    token = os.getenv('TOKEN')
    chat_id = os.getenv('CHAT_ID')
    file = open(path('config.json'), 'w')
    print(f"PATH TO CONFIG {path('config.json')}")
    json_str = {
        "base": {
            "project": "qaguru python",
            "environment": "prod",
            "comment": "",
            "reportLink": "",
            "language": "en",
            "allureFolder": "allure-report",
            "enableChart": True
        },
        "telegram": {
            "token": f"{token}",
            "chat": f"{chat_id}",
            "replyTo": ""
        }
    }
    json_object = json.dumps(json_str, indent=4)
    file.write(json_object)
    file.close()


@pytest.fixture(scope='function', autouse=True)
@allure.step('Set up base url, browser type')
def browser_management(request):
    """
    Set up browser
    """
    remote_driver = request.config.getoption('--remote_driver')
    remote_driver = remote_driver if remote_driver != "" else DEFAULT_REMOTE_DRIVER
    capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    browser.config.driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@{remote_driver}/wd/hub",
        desired_capabilities=capabilities)

    browser.config.browser_name = os.getenv('selene.browser_name', 'chrome')
    browser.config.hold_browser_open = (
            os.getenv('selene.hold_browser_open', 'false').lower() == 'true'
    )
    browser.config.timeout = float(os.getenv('selene.timeout', '3'))


@allure.step('Open page: {path}')
def open_page(path: str):
    """
    Open(redirect) pages contains testing form
    """
    browser.open(path)
    # for loading advertise
    time.sleep(1)
    (
        browser.all('[id^=google_ads][id$=container__],[id$=Advertisement]')
        .with_(timeout=10)
        .should(have.size_greater_than_or_equal(3))
        .perform(command.js.remove)
    )
