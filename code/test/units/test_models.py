import pytest
from models.user import UserModel
from models.photo import PhotoModel
from db import db


class TestUserModel:

    @pytest.mark.parametrize("username, password, email", [
        ("test_username","test_password","test_mail@gmail.com"),
        ("8279301238","123879014","1231412@gmail.com"),
        ("test_usernametest_usernametest_usernametest_usernametest_usernametest_username12","test_password","test_mail@gmail.com"),
        ("test_username","test_password","test_mail@gmail.com"),
    ])
    def test_user_model(self, username, password, email):
        new_user = UserModel(username, password, email)
        assert new_user.username == username
        assert new_user.password == password
        assert new_user.email == email


class TestPhotoModel:

    @pytest.mark.parametrize("photo_name, data, visible, user_id", [
        ("Robot", "DATA_PLACEHOLDER_1", True, 1),
        ("Cat", "DATA_PLACEHOLDER_2", False, 2),
        ("Robot_cat", "DATA_PLACEHOLDER_3", True, 3),
        ("Robot", "DATA_PLACEHOLDER_4", False, 2),
    ])
    def test_photo_model(self, photo_name, data, visible, user_id):
        new_photo = PhotoModel(photo_name, data, visible, user_id)
        assert new_photo.photo_name == photo_name
        assert new_photo.data == data
        assert new_photo.visible == visible
        assert new_photo.user_id == user_id
