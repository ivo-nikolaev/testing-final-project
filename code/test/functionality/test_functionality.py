import pytest
from models.user import UserModel
from models.photo import PhotoModel

class TestUserFunctionality:
    @pytest.mark.parametrize("username, password, email", [
        ("martin",  "mpassw",        "ma@1.c"),
        ("MARTIN",  "MPASSW",        "MA@2.C"),
        ("MaRtI3",  "MpASsW",        "mA@3.C"),
        ("martin123m"*10,  "mpassw",        "ma@4.c"),
        ("marti5",  "mapassword"*10,    "ma@5.c"),
        ("martin321m"*10, "mapassword"*10, "ma@6.c"),
        ("martin455m"*10, "mapassword"*10, "mart@5.com"*10),
    ])
    def test_valid_registration(self, test_client, init_database, username, password, email):
        response = test_client.post('/register',
                                    data=dict(username=username,
                                              password=password,
                                              email=email),
                                    follow_redirects=True)
        assert response.status_code == 201
        print(response.data)
        assert b"User created successfully." in response.data


    pass

class TestPhotoFunctionality:
    pass