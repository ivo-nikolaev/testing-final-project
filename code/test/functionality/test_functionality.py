import pytest
from models.user import UserModel
from models.photo import PhotoModel
from security import authenticate, identity

class TestUserFunctionality:
    @pytest.mark.parametrize("username, password, email, status_code, data", [
        ("martin",          "mpassw",           "ma@1.c",           201, b"User created successfully."),
        ("MARTIN",          "MPASSW",           "MA@2.C",           201, b"User created successfully."),
        ("MaRtI3",          "MpASsW",           "mA@3.C",           201, b"User created successfully."),
        ("martin123m"*10,   "mpassw",           "ma@4.c",           201, b"User created successfully."),
        ("marti5",          "mapassword"*10,    "ma@5.c",           201, b"User created successfully."),
        ("martin321m"*10,   "mapassword"*10,    "ma@6.c",           201, b"User created successfully."),
        ("martin455m"*10,   "mapassword"*10,    "mart@5.com"*10,    201, b"User created successfully."),
        # Duplicate, same username as entry 1:
        ("martin",          "mpassw",           "mart@42.com",      400, b"A user with that username already exists"),
        # Duplicate, same email as entry 2:
        ("martin42",        "mpassw",           "MA@2.C",           400, b"A user with that email already exists"),
        # Add test fro 80 plus chars
    ])
    def test_registration(self, test_client, init_database, username, password, email, status_code, data):
        """
        Test registering users

        The given username, password and email will be registered and inserted into the database.
        :param test_client: Flask app client for testing (Fixture)
        :param init_database: Setup database if not already done (Fixture)
        :param username: String, max 80 char
        :param password: String, max 80 char
        :param email: String, max 80 char
        :param status_code: Expected return status code
        :param data: Expected data in response
        """
        response = test_client.post('/register',
                                    data=dict(username=username,
                                              password=password,
                                              email=email),
                                    follow_redirects=True)
        assert response.status_code == status_code
        assert data in response.data

    #@pytest.mark.parametrize("username, password, status_code", [
    #    ("test_user_1", "test_password_1", 200),
    #    ("TEST_USER_2", "TEST_PASSWORD_2", 200),
    #    ("Test_User_3", "Test_Password_3", 200),
    #])
    #def test_login(self, test_client, init_database, username, password, status_code):
    #    response = test_client.post('/auth',
    #                                data=dict(username=username,
    #                                          password=password),
    #                                follow_redirects=True)


    @pytest.mark.parametrize("username, password, email, uid, valid", [
        # Valid users
        ("test_user_1", "test_password_1", "test_mail_1@gmail.com", 1, True),
        ("TEST_USER_2", "TEST_PASSWORD_2", "TEST_MAIL_2@GMAIL.COM", 2, True),
        ("Test_User_3", "Test_Password_3", "Test_Mail_3@Gmail.Com", 3, True),
        # Invalid users
        ("Invalid_test_user", "NicePassword", "Test_Mail_3@Gmail.Com", 13, False),
        # Test matching username wrong password
        ("test_user_1", "Wrongpassword", "Test_Mail_3@Gmail.Com", 1, False),
        # Test case sensitivity:
        ("test_user_1", "Test_password_1", "Test_Mail_3@Gmail.Com", 1, False),
        # Test similar password
        ("test_user_1", "test_password_", "Test_Mail_3@Gmail.Com", 1, False),
    ])
    def test_authenticate(self, test_client, init_database, username, password, email, uid, valid):
        '''
        Test authentication of users

        :param test_client: Flask app client for testing (Fixture)
        :param init_database: Setup database if not already done (Fixture)
        :param username: String, max 80 char
        :param password: String, max 80 char
        :param email: String, max 80 char
        :param uid: id of returned user
        :param valid: whether testing a valid user or not
        '''
        test_user = authenticate(username, password)
        if valid:
            assert test_user.id == uid
            assert test_user.username == username
            assert test_user.password == password
            assert test_user.email == email
        else:
            assert test_user is None

        print(test_user)  # If anything goes wrong

    @pytest.mark.parametrize("payload, username, password, email, valid", [
        # Valid payloads using mocked payloads:
        ({'identity': 1}, "test_user_1", "test_password_1", "test_mail_1@gmail.com", True),
        ({'identity': 2}, "TEST_USER_2", "TEST_PASSWORD_2", "TEST_MAIL_2@GMAIL.COM", True),
        ({'identity': 3}, "Test_User_3", "Test_Password_3", "Test_Mail_3@Gmail.Com", True),
        # Invalid payloads
        ({'identity': 42}, "test_user_1", "test_password_1", "test_mail_1@gmail.com", False),
        ({'identity': 11}, "test_user_1", "test_password_1", "test_mail_1@gmail.com", False),
        ({'identity': 0}, "test_user_1", "test_password_1", "test_mail_1@gmail.com", False),
        ({'identity': -1}, "test_user_1", "test_password_1", "test_mail_1@gmail.com", False),
    ])
    def test_identity(self, test_client, init_database, payload, username, password, email, valid):
        test_user = identity(payload)
        if valid:
            assert test_user.username == username
            assert test_user.password == password
            assert test_user.email == email
        else:
            assert test_user is None

        print(test_user)  # If anything goes wrong

class TestPhotoFunctionality:
    pass