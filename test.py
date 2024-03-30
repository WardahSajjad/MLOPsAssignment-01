import unittest
from app import app

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        # Creates a test client for the Flask app.
        self.app = app.test_client()
        self.app.testing = True

    def test_valid_input(self):
        # This test case sends a POST request with valid data and expects a 200 status code.
        data = {
            'Age': 25,
            'Gender': 0,
            'Marital Status': 1,
            'Occupation': 2,
            'Monthly Income': 3000,
            'Educational Qualifications': 3,
            'Family size': 4,
            'latitude': 12.9716,
            'longitude': 77.5946,
            'Pin code': 560001
        }
        response = self.app.post('/predict', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Prediction', response.json)
        print("Test 'test_valid_input' passed successfully!")

    def test_missing_feature(self):
        # This test case intentionally omits a required feature to check if the app responds appropriately.
        data = {
            'Age': 25,
            'Gender': 0,
            # Missing 'Marital Status'
            'Occupation': 2,
            'Monthly Income': 3000,
            'Educational Qualifications': 3,
            'Family size': 4,
            'latitude': 12.9716,
            'longitude': 77.5946,
            'Pin code': 560001
        }
        response = self.app.post('/predict', json=data)
        self.assertNotEqual(response.status_code, 200)  # Assuming your app handles this with an error.
        print("Test 'test_missing_feature' passed successfully!")

    def test_invalid_value_type(self):
        # This test case provides an invalid type for one of the features to see if the app can handle it.
        data = {
            'Age': "twenty-five",  # Invalid type, should be int
            'Gender': 0,
            'Marital Status': 1,
            'Occupation': 2,
            'Monthly Income': 3000,
            'Educational Qualifications': 3,
            'Family size': 4,
            'latitude': 12.9716,
            'longitude': 77.5946,
            'Pin code': 560001
        }
        response = self.app.post('/predict', json=data)
        self.assertNotEqual(response.status_code, 200)  # Assuming your app handles this with an error.
        print("Test 'test_invalid_value_type' passed successfully!\n")

if __name__ == '__main__':
    unittest.main()
