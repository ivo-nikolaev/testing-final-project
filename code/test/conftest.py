# pip install pytest-flask
# pip install pytest-flask-sqlalchemy
import pytest
from models.user import UserModel
from app import create_app, db
#from db import db
from flask import Flask, url_for

@pytest.fixture(scope='module')
def new_user():
    user = UserModel('Test_user', 'Test_password', 'TestMail@gmail.com')
    return user

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('flask_test.cfg')
    #flask_app = create_app(True)
    #flask_app = create_app()
    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    testing_client = flask_app.test_client()

    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()


@pytest.fixture(scope='module')
def init_database():
    db.create_all()
    # Test users
    user1 = UserModel('test_user_1', 'test_password_1', 'test_mail_1@gmail.com')
    user2 = UserModel('TEST_USER_2', 'TEST_PASSWORD_2', 'TEST_MAIL_2@GMAIL.COM')
    user3 = UserModel('Test_User_3', 'Test_Password_3', 'Test_Mail_3@Gmail.Com')
    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)

    db.session.commit()

    yield db  # this is where the testing happens!

    db.drop_all()
