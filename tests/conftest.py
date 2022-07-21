"""
Setup test configurations
"""
import os
import time
import allure
import pytest

from selene import have, command
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
@allure.step('Set up base url, browser type')
def browser_management():
    """
    Set up browser
    """
    browser.config.base_url = os.getenv('selene.base_url', 'https://demoqa.com')
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
