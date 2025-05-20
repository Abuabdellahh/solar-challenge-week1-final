import unittest
import pandas as pd
import numpy as np
from src.data_cleaning import DataCleaner

class TestDataCleaner(unittest.TestCase):
    def setUp(self):
        # Create a sample DataFrame
        data = {
            'Timestamp': ['2023-01-01 00:00', '2023-01-01 01:00', '2023-01-01 02:00'],
            'GHI': [100, np.nan, 1000],
            'DNI': [80, 90, 800],
            'DHI': [20, 30, 200],
            'ModA': [90, 100, 900],
            'ModB': [95, 105, 950],
            'WS': [5, 6, 50],
            'WSgust': [7, 8, 70]
        }
        self.df = pd.DataFrame(data)
        self.cleaner = DataCleaner(self.df, 'test')
    
    def test_profile_data(self):
        summary, missing, high_missing = self.cleaner.profile_data()
        self.assertEqual(missing['GHI'], 1)
        self.assertTrue('GHI' in high_missing)
    
    def test_clean_data(self):
        cleaned_df = self.cleaner.clean_data()
        self.assertEqual(cleaned_df['GHI'].isna().sum(), 0)
        self.assertTrue(len(cleaned_df) <= len(self.df))

if __name__ == '__main__':
    unittest.main()