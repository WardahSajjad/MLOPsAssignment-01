import unittest
import pandas as pd
from onlinefood import preprocessing_pipeline

class TestPreprocessingPipeline(unittest.TestCase):

    def test_preprocessing_pipeline(self):
        # Generate sample data for testing
        sample_data = {
            'Gender': ['Male', 'Female', 'Male', 'Female'],
            'Monthly Income': [3000, 'Unknown', 5000, 4000],
            'Marital Status': ['Single', 'Married', 'Single', 'Married'],
            'Occupation': ['Engineer', 'Doctor', 'Teacher', 'Artist'],
            'Educational Qualifications': ['Graduate', 'Postgraduate', 'Graduate', 'Undergraduate'],
            'Output': [1, 0, 1, 0]
        }
        df = pd.DataFrame(sample_data)

        # Apply preprocessing pipeline
        X, y = preprocessing_pipeline(df)

        # Assert that X and y have the correct shapes
        self.assertEqual(X.shape, (4, 5))
        self.assertEqual(y.shape, (4,))

        # Add more specific assertions as needed based on your preprocessing pipeline
        # For example, check for specific values or data types

if __name__ == '__main__':
    unittest.main()
