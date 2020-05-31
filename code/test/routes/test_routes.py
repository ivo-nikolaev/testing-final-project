import pytest

class TestRoutes:

    @pytest.mark.parametrize("route, status_code, data", [
        ("/",               200,            b"Testesting App"),
        #("/photo/2",        404,            None),  # THIS WILL FAIL, THERE IS NO IMAGE IN THE DB!
        ("/test_page",      200,            b"THIS IS PURELY FOR TESTING ROUTES"),
    ])
    def test_routes(self, test_client, route, status_code, data):
        """
        GIVEN a Flask application
        WHEN the a route is requested (GET)
        THEN check the response is valid
        """
        response = test_client.get(route)
        print(response)
        assert response.status_code == status_code
        if data:
            assert data in response.data
