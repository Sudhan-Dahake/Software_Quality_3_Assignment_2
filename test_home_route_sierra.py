"""This module will perform a basic test on the home route of the app"""
import pytest
from app import app as flask_app

# Arrange
@pytest.fixture
def create_test_app():
    """creates a test environment of the app"""
    flask_app.config.update({'TESTING':True})
    return flask_app

# Arrange
@pytest.fixture
def create_test_client(create_test_app):
    """creates a test client"""
    return create_test_app.test_client()

def test_home_route(create_test_client):
    """Tests the home route of the application to ensure that it functions as expected""" 
    # Act
    actual_response = create_test_client.get('/') # Call the home route for the app
    # Assert
    assert b"A webapp to detect a digit using hand sign language." in actual_response.data
    # check that the correct sub heading is on the page (b represents bytes)
    assert actual_response.status_code == 200
    # check that the call for the home route returns 200 OK status code
