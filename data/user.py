"""
User data
"""


class User(object):
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
    hobby = ['Sports']
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
