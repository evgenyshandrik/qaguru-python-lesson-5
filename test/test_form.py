"""
Testing sing up form
"""
from selene import have
from selene.core.entity import Element

from data.user import User, expected_date_of_birthday
from model import application_manager
from test.conftest import open_page


def test_sign_up():
    """
    Testing sign up form
    """
    open_page('/automation-practice-form')

    application_manager.registration_form \
        .set_name(User.first_name, User.last_name) \
        .set_email(User.email) \
        .set_sex(User.sex) \
        .set_phone_number(User.phone) \
        .set_date_of_birthday(User.date_of_birthday) \
        .set_subject(User.subject) \
        .set_hobby(User.hobby) \
        .set_avatar(User.avatar) \
        .set_address(User.address) \
        .set_state(User.state) \
        .set_city(User.city) \
        .submit_form()

    application_manager.result_form.get_cells_by_index(0, 'Student Name', f'{User.first_name} {User.last_name}')
    application_manager.result_form.get_cells_by_index(1, 'Student Email', User.email)
    application_manager.result_form.get_cells_by_index(2, 'Gender', User.sex)
    application_manager.result_form.get_cells_by_index(3, 'Mobile', str(User.phone))
    application_manager.result_form.get_cells_by_index(4, 'Date of Birth', expected_date_of_birthday)
    application_manager.result_form.get_cells_by_index(5, 'Subjects', f'{User.subject[0]}, {User.subject[1]}')
    application_manager.result_form.get_cells_by_index(6, 'Hobbies', User.hobby[0])
    application_manager.result_form.get_cells_by_index(7, 'Picture', User.avatar)
    application_manager.result_form.get_cells_by_index(8, 'Address', User.address)
    application_manager.result_form.get_cells_by_index(9, 'State and City', f'{User.state} {User.city}')
