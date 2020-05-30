import pytest
from selenium import webdriver
#import chromedriver_binary # pip install chromedriver-binary
#from webdriver_manager.chrome import ChromeDriverManager  #  pip install webdriver-manager
from selenium.webdriver.common.keys import Keys


class TestApp:

    URL = "http://127.0.0.1"
    PORT = 5000

    @pytest.fixture
    def driver(self):
        #driver = webdriver.Chrome()
        #driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = webdriver.Firefox(executable_path='/builds/dosehunter/testingmandatory2_exam/driver/geckodriver')  # Chrome
        #driver = webdriver.Firefox(executable_path='drivers\geckodriver.exe')  # Firefox
        yield driver

    def test_home_route(self, driver):
        #driver.get(f"{self.URL}:{self.PORT}/")
        driver.get("https://en.wikipedia.org/wiki/Main_Page")
        print("Title of page: " + driver.title)
        assert driver.title == "Wikipedia, the free encyclopedia"
        search_bar = driver.find_element_by_id("searchInput")
        search_bar.send_keys("Paper")
        search_bar.send_keys(Keys.ENTER)
        #pass

    @pytest.mark.parametrize("album, allowed", [
        ("Album_name", True)
    ])
    def test_see_album(self, album, allowed):
        pass

    @pytest.mark.parametrize("username, password, expected", [
        ("test",            "test",             True),
        ("NotValidUser",    "NotAPassword",     False),
    ])
    def test_login(self, username, password, expected):
        # Go to index page
        # Attempt to login with above username and password combinations
        # See if able to login and wether it should be
        pass

    @pytest.mark.parametrize("username, email, passowrd, expected", [
        ("Martin123",   "martin@mail.com",  "martinspassword", True),
    ])
    def test_register(self, username, email, passowrd, expected):
        # Open website
        # Navigate to register page
        # Insert information
        # Attempt to register user
        # Match with expected result
        pass
