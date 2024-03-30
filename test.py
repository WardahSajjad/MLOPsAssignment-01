import unittest
from app import app


class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_valid_input(self):
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
        data = {
            'Age': 25,
            'Gender': 0,
            'Occupation': 2,
            'Monthly Income': 3000,
            'Educational Qualifications': 3,
            'Family size': 4,
            'latitude': 12.9716,
            'longitude': 77.5946,
            'Pin code': 560001
            # 'Marital Status' is intentionally omitted to test response
        }
        response = self.app.post('/predict', json=data)
        self.assertNotEqual(response.status_code, 200)
        print("Test 'test_missing_feature' passed successfully!")

    def test_invalid_value_type(self):
        data = {
            'Age': "twenty-five",  # Incorrect type
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
        self.assertNotEqual(response.status_code, 200)
        print("Test 'test_invalid_value_type' passed successfully!\n")


if __name__ == '__main__':
    unittest.main()