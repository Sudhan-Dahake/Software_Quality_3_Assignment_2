import pytest
from io import BytesIO
from app import app

# Setting up a client fixture to initialize a client
@pytest.fixture
def client():
    # Enabling testing mode, which provides better error messages and disables error handling
    app.config['TESTING'] = True

    # Creating a test client instance of the app to use in tests
    with app.test_client() as client:
        yield client


# Test case for successfully predicting an image
def test_prediction_route_success(client):
    # Opening a sample image file in binary mode to simulate an uploaded image
    with open("prediction_test_image.jpeg", "rb") as img_file:
        img_data = img_file.read()

    # Preparing the data dictionary with the image to send with the POST request
    data = {
        'file': (BytesIO(img_data), 'prediction_test_image.jpeg')
    }

    # Send a POST request to the '/prediction' route with the image data
    response = client.post(
        '/prediction', content_type='multipart/form-data', data=data)

    # Checking if the response status code is 200 (OK)
    assert response.status_code == 200

    # Verifying that the response contains the "Prediction" header, indicating the page loaded correctly
    assert b"Prediction" in response.data

    # Checking that the prediction value is displayed with the correct styling in the response HTML
    assert b"text-dark font-weight-bold" in response.data


# Test case for handling errors when no image is provided
def test_prediction_route_error(client):
    # Sending a POST request to '/prediction' without any file data to simulate a missing file
    response = client.post(
        '/prediction', content_type='multipart/form-data', data={})

    # Checking if the response status code is 200 (OK), as the route should handle this gracefully
    assert response.status_code == 200
    
    # Confirming that the error message "File cannot be processed." appears in the HTML response
    assert b"File cannot be processed." in response.data
