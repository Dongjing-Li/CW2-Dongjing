from user import User
import pytest

@pytest.fixture(scope='module')
def user():
    first_name = 'Dongjing'
    last_name = 'Li'
    email_address = 'zcemdli@ucl.ac.uk'
    username = 'Jerry'
    password = '19011895'

    user = User(password, first_name, last_name, email_address, username)
    yield user
