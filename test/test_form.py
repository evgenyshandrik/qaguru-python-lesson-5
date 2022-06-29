"""
Testing sing up form
"""
import os

from selene import have, command
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss


class User():
    """
    User profile data
    """
    first_name = 'Evgen'
    last_name = 'Sh'
    email = 'test@test.ru'
    sex = 'Male'
    phone = 1234567890
    date_of_birthday = {'day': '20', 'month': '3', 'year': '1991'}
    subject = 'English'
    hobby = 'Sports'
    address = 'Address street'
    state = 'NCR'
    city = 'Delhi'
    avatar = 'test.png'


month_name = {'1': 'January',
              '2': 'February',
              '3': 'March',
              '4': 'April',
              '5': 'May',
              '6': 'June',
              '7': 'July',
              '8': 'August',
              '9': 'September',
              '10': 'October',
              '11': 'November',
              '12': 'December'}

expected_date_of_birthday = f'{User.date_of_birthday.get("day")} ' \
                            f'{month_name.get(User.date_of_birthday.get("month"))},{User.date_of_birthday.get("year")}'


def open_page():
    """
    Open(redirect) page contains testing form
    """
    browser.open('/automation-practice-form')
    (
        ss('[id^=google_ads][id$=container__]').with_(timeout=10)
        .should(have.size_greater_than_or_equal(2))
        .perform(command.js.remove)
    )


def test_sign_up():
    """
    Testing sign up form
    """
    open_page()

    s('#firstName').type(User.first_name)
    s('#lastName').type(User.last_name)
    s('#userEmail').type(User.email)

    gender_types = s('#genterWrapper')
    gender_types.all('.custom-radio').element_by(have.exact_text(User.sex)).click()

    s('#userNumber').type(User.phone)

    s('#dateOfBirthInput').click()
    s('.react-datepicker__year-select').element(f'[value="{User.date_of_birthday.get("year")}"]').click()
    s('.react-datepicker__month-select').element(f'[value="{int(User.date_of_birthday.get("month")) - 1}"]').click()
    s(f'.react-datepicker__day--0{User.date_of_birthday.get("day")}').click()

    s('#subjectsInput').type(User.subject).press_tab()

    hobbies_types = s('#hobbiesWrapper')
    hobbies_types.all('.custom-checkbox').element_by(have.exact_text(User.hobby)).click()

    s('#uploadPicture').send_keys(os.path.abspath(f'../resources/{User.avatar}'))

    s('#currentAddress').type(User.address)
    s('#state').element('input').type(User.state).press_tab()
    s('#city').element('input').type(User.city).press_tab()

    s('#submit').perform(command.js.click)

    tr = browser.elements("table tr")
    tr.element(1).should(have.text(f'{User.first_name} {User.last_name}'))
    tr.element(2).should(have.text(User.email))
    tr.element(3).should(have.text(User.sex))
    tr.element(4).should(have.text(str(User.phone)))
    tr.element(5).should(have.text(expected_date_of_birthday))
    tr.element(6).should(have.text(User.subject))
    tr.element(7).should(have.text(User.hobby))
    tr.element(8).should(have.text(User.avatar))
    tr.element(9).should(have.text(User.address))
    tr.element(10).should(have.text(f'{User.state} {User.city}'))
