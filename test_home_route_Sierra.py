import pytest
from app import app as flask_app

# Arrange
@pytest.fixture
def app(): # creates a test environment of the app
    flask_app.config.update({'TESTING':True})
    return flask_app

# Arrange
@pytest.fixture
def client(app):  # creates a test client
    return app.test_client()


def test_home_route(client):
    # Act
    actual_response = client.get('/') # Call the home route for the app
    
    # Assert 
    assert b"A webapp to detect a digit using hand sign language." in actual_response.data # check that the correct sub heading is on the page (b represents bytes)
    assert actual_response.status_code == 200 # check that the call for the home route returns 200 OK status code

