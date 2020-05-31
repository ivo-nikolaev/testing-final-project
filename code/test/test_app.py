import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager  # pip install webdriver-manager
from selenium.webdriver.common.keys import Keys
import time
# https://www.lambdatest.com/blog/test-automation-using-pytest-and-selenium-webdriver/


# Retrieve the driver and pass it to the class once
@pytest.fixture(scope="class", autouse=True)
def prepare_driver(request):
    print("Running setup\rRetrieving driver...")
    driver = webdriver.Chrome(ChromeDriverManager().install())  # Retrieve driver
    request.cls.driver = driver  # Set the driver for the class
    yield
    driver.close()


@pytest.mark.usefixtures("prepare_driver")
class TestApp:

    URL = "http://localhost"
    PORT = 5000
    PHOTO = "photo"

    # Go to home page before each test
    @pytest.fixture(autouse=True)
    def prep_page(self):
        self.driver.get(f"{self.URL}:{self.PORT}/")

    @pytest.mark.parametrize("username, password", [
        ("test", "test"),
        ("test2", "test2"),
        ("test3", "test3")
    ])
    def test_login(self, username, password):
        print(self.log(" Testing login ..."))
        username_in = self.driver.find_element_by_id("in_username")
        password_in = self.driver.find_element_by_id("in_password")

        username_in.send_keys(username)
        time.sleep(1)
        password_in.send_keys(password)

    @pytest.mark.parametrize("photo_id", [
        (2),
        (2),
        (2),
    ])
    def test_see_photo(self, photo_id):
        self.driver.get(f"{self.URL}:{self.PORT}/{self.PHOTO}/{photo_id}")

    def test_see_album(self):
        pass

    @staticmethod
    def log(msg):
        return f"[INTERFACE] {msg}"
