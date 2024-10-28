import pytest
from keras.models import load_model
from keras.utils import img_to_array
import numpy as np
from PIL import Image

from model import preprocess_img


def test_preprocess_img():
    # using one of existing the images in the project
    # renamed the "Sign 3 (99).jpeg" to "preprocess_img_test.jpeg"
    img_path = "preprocess_img_test.jpeg"

    # Calling the preprocess_img function
    # passing the path of the test image
    processed_image = preprocess_img(img_path)

    # Checking the shape of the processed image
    assert processed_image.shape == (
        1, 224, 224, 3), "Shape of processed image is incorrect"

    # Checking that the pixel values are in the range [0, 1]
    assert np.all(processed_image >= 0.0) and np.all(
        processed_image <= 1.0), "Out of range pixel values"

    # Checking that the output image is of type float32
    assert processed_image.dtype == np.float32, "Processed image dtype is incorrect"
