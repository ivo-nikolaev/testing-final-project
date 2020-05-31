def test_home_page(test_client):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    print(type(test_client))
    response = test_client.get('/')
    print(response)
    assert response.status_code == 200
