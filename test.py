import unittest
from unittest.mock import patch
import pandas as pd
from onlinefood import preprocessing_pipeline

class TestPreprocessingPipeline(unittest.TestCase):
    @patch('onlinefood.pd.read_csv')
    def test_preprocessing_pipeline(self, mock_read_csv):
        # Mocking pd.read_csv to return a predefined DataFrame
        mock_read_csv.return_value = pd.DataFrame({
            'Gender': ['Male', 'Female', 'Male', 'Female'],
            'Monthly Income': [3000, 'Unknown', 5000, 4000],
            'Marital Status': ['Single', 'Married', 'Single', 'Married'],
            'Occupation': ['Engineer', 'Doctor', 'Teacher', 'Artist'],
            'Educational Qualifications': ['Graduate', 'Postgraduate', 'Graduate', 'Undergraduate'],
            'Output': [1, 0, 1, 0]
        })
        
        # Apply preprocessing pipeline
        X, y = preprocessing_pipeline(mock_read_csv.return_value)

        # Assert that X and y have the correct shapes
        self.assertEqual(X.shape, (4, 5))
        self.assertEqual(y.shape, (4,))

        # Add more specific assertions as needed based on your preprocessing pipeline
        # For example, check for specific values or data types78888888888888
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
        self.assertNotEqual(response.status_code, 
        200)
        print("Test 'test_invalid_value_type' passed successfully!\n")


if __name__ == '__main__':
    unittest.main()
