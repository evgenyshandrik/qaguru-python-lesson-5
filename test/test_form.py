"""
Testing sing up form
"""
import time

from selene import have, command
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss

from controls import TagsInput, Dropdown, DatePicker, Table
from util.resources import path


class User():
    """
    User profile data
    """
    first_name = 'Evgen'
    last_name = 'Sh'
    email = 'test@test.ru'
    sex = 'Male'
    phone = 1234567890
    date_of_birthday = '20.03.1991'
    subject = ['English', 'Maths']
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

year_birthday = int(User.date_of_birthday.split('.')[2])
month_birthday = int(User.date_of_birthday.split('.')[1])
day_birthday = int(User.date_of_birthday.split('.')[0])
expected_date_of_birthday = f'{day_birthday} ' \
                            f'{month_name.get(str(month_birthday))},{year_birthday}'


def open_page():
    """
    Open(redirect) page contains testing form
    """
    browser.open('/automation-practice-form')
    time.sleep(1)  # todo: for loading advertise
    (
        browser.all('[id^=google_ads][id$=container__],[id$=Advertisement]')
        .with_(timeout=10)
        .should(have.size_greater_than_or_equal(3))
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

    mobile_phone = '#userNumber'
    s(mobile_phone).type(User.phone)

    date_picker = DatePicker(s('#dateOfBirthInput'))
    date_picker.set_date("20.03.1991")

    first_user_subject = User.subject[0]
    second_user_subject = User.subject[1]
    subjects = TagsInput(s('#subjectsInput'))
    subjects.add(first_user_subject[0:3], autocomplete=first_user_subject)
    subjects.add(second_user_subject)

    hobbies_types = s('#hobbiesWrapper')
    hobbies_types.all('.custom-checkbox').element_by(have.exact_text(User.hobby)).click()

    s('#uploadPicture').send_keys(path(f'{User.avatar}'))

    s('#currentAddress').type(User.address)

    state_element = Dropdown(s('#state'))
    state_element.select(option=User.state)

    city_element = Dropdown(s('#city'))
    city_element.autocomplete(option=User.city)

    s('#submit').perform(command.js.click)

    result_table = Table(s('.modal-content .table'))
    result_table.cells_of_row(0).should(have.exact_texts('Student Name', f'{User.first_name} {User.last_name}'))
    result_table.cells_of_row(1).should(have.exact_texts('Student Email', User.email))
    result_table.cells_of_row(2).should(have.exact_texts('Gender', User.sex))
    result_table.cells_of_row(3).should(have.exact_texts('Mobile', str(User.phone)))
    result_table.cells_of_row(4).should(have.exact_texts('Date of Birth', expected_date_of_birthday))
    result_table.cells_of_row(5).should(have.exact_texts('Subjects', f'{User.subject[0]}, {User.subject[1]}'))
    result_table.cells_of_row(6).should(have.exact_texts('Hobbies', User.hobby))
    result_table.cells_of_row(7).should(have.exact_texts('Picture', User.avatar))
    result_table.cells_of_row(8).should(have.exact_texts('Address', User.address))
    result_table.cells_of_row(9).should(have.exact_texts('State and City', f'{User.state} {User.city}'))
