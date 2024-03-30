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
        # For example, check for specific values or data types

if __name__ == '__main__':
    unittest.main()
