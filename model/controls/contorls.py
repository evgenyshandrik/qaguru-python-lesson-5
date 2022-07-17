"""
Controls on the pages
"""
from selene.support.shared.jquery_style import s
from typing import Optional

from selene import have, command
from selene.core.entity import Element
from selene.support.shared import browser


class TagsInput(object):
    """
    Page object tag input
    """

    def __init__(self, element: Element):
        self.element = element

    def add(self, from_: str, *, autocomplete: Optional[str] = None):
        self.element.type(from_)
        browser.all(
            '.subjects-auto-complete__option'
        ).element_by(have.text(autocomplete or from_)).click()

    def autocomplete(self, from_: str):
        self.element.type(from_).press_tab()


class Dropdown(object):
    """
        Page object dropdown
    """

    def __init__(self, element: Element):
        self.element = element

    def select(self, *, option: str):
        self.element.perform(command.js.scroll_into_view).click()
        browser.all('[id^=react-select-][id*=-option]').element_by(have.exact_text(option)).click()

    def autocomplete(self, *, option: str):
        self.element.element(
            '[id^=react-select-][id*=-input]'
        ).type(option).press_enter()


class DatePicker(object):
    """
        Page object date picker
    """

    def __init__(self, element: Element):
        self.element = element

    def set_date(self, date: str):
        self.element.click()
        date_attribute = date.split('.')
        self.__set_year(int(date_attribute[2]))
        self.__set_month(int(date_attribute[1]))
        self.__set_day(int(date_attribute[0]))

    @staticmethod
    def __set_year(option: int):
        s('.react-datepicker__year-select').element(f'[value="{option}"]').click()

    @staticmethod
    def __set_month(option: int):
        s('.react-datepicker__month-select').element(f'[value="{str(option - 1)}"]').click()

    @staticmethod
    def __set_day(option: int):
        s(f'.react-datepicker__day--0{option}').click()


class Table(object):
    """
        Page object table
    """
    def __init__(self, element: Element):
        self.element = element

    def cells_of_row(self, index):
        return self.element.all('tbody tr')[index].all('td')
