from selene import have, command
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss

firstName = 'Evgen'
lastName = 'Sh'
email = 'test@test.ru'
sex = 'Male'
phone = 1234567890
date_of_birthday = '20 March,1991'
subject = 'English'
hobbies = 'Sports'
address = 'Address street'
state = 'NCR'
city = 'Delhi'
filename = 'main.png'


def open_page():
    browser.open('/automation-practice-form')
    (
        ss('[id^=google_ads][id$=container__]').with_(timeout=10)
        .should(have.size_greater_than_or_equal(2))
        .perform(command.js.remove)
    )


def test_sign_up():
    open_page()

    s('#firstName').type(firstName)
    s('#lastName').type(lastName)
    s('#userEmail').type(email)
    s('[for="gender-radio-1"]').click()
    s('#userNumber').type(phone)
    s('#dateOfBirthInput').click()
    s('[value="1991"]').click()
    s('[value="2"]').click()
    s('[aria-label="Choose Wednesday, March 20th, 1991"]').click()
    s('#subjectsInput').type(subject).press_tab()
    s('[for="hobbies-checkbox-1"]').click()
    s('#uploadPicture').type(f'/Users/evgen/Downloads/{filename}')
    s('#currentAddress').type(address)
    s('#react-select-3-input').type(state).press_tab()
    s('#react-select-4-input').type(city).press_tab().press_enter()

    tr = browser.elements("table tr")
    tr.element(1).should(have.text(f'{firstName} {lastName}'))
    tr.element(2).should(have.text(email))
    tr.element(3).should(have.text(sex))
    tr.element(4).should(have.text(str(phone)))
    tr.element(5).should(have.text(date_of_birthday))
    tr.element(6).should(have.text(subject))
    tr.element(7).should(have.text(hobbies))
    tr.element(8).should(have.text(filename))
    tr.element(9).should(have.text(address))
    tr.element(10).should(have.text(f'{state} {city}'))
