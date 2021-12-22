input_password = '0117273'


def test_check_password(user):
    response = user.check_password(input_password)
    assert response == True
