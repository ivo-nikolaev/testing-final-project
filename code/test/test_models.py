import pytest
from models.user import UserModel

class TestUserModel:

    @pytest.fixture()
    def user_model(self):
        u = UserModel("Alice123", "test123", "standard@mail.com")
        yield u

    @pytest.mark.parametrize("input, result, expected", [
        ("Input",       "Result",   False),
        ("Input2",      "Input2",   True)
    ])
    def test_save_to_db(self, user_model, input, result, expected):
        assert (input == result) == expected

    def test_find_by_username(self):
        pass

    def test_find_by_email(self):
        pass

    def test_find_by_id(self):
        pass

class TestPhotoModel:
    def test_find_by_id(self):
        pass