"""
Module for work with resources
"""
import time
import allure
import tests

from allure_commons.types import AttachmentType
from pathlib import Path
from selene.support.shared import browser


def path_from_resources(relative_path):
    """
    Get path to resource file
    """
    return (
        Path(tests.__file__)
        .parent
        .parent
        .joinpath('resources/')
        .joinpath(relative_path)
        .absolute()
        .__str__()
    )


def take_screenshot(name: str, type_file: AttachmentType):
    """
    Take screenshot
    """
    # for loading page
    time.sleep(0.5)
    allure.attach(browser.driver.get_screenshot_as_png(), name=name, attachment_type=type_file)
