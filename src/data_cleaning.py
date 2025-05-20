import pandas as pd
import numpy as np
from scipy import stats

class DataCleaner:
    """Class for cleaning solar datasets."""
    
    def __init__(self, df, country):
        self.df = df.copy()
        self.country = country
        self.key_columns = ['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS', 'WSgust']
    
    def profile_data(self):
        """Generate summary statistics and missing value report."""
        summary = self.df.describe()
        missing = self.df.isna().sum()
        missing_pct = (missing / len(self.df)) * 100
        high_missing = missing_pct[missing_pct > 5]
        return summary, missing, high_missing
    
    def detect_outliers(self, z_threshold=3):
        """Flag outliers using Z-scores."""
        z_scores = np.abs(stats.zscore(self.df[self.key_columns].dropna()))
        outliers = (z_scores > z_threshold).any(axis=1)
        return self.df.index[outliers]
    
    def clean_data(self):
        """Clean data by handling missing values and outliers."""
        try:
            # Convert Timestamp to datetime
            self.df['Timestamp'] = pd.to_datetime(self.df['Timestamp'])
            
            # Handle missing values with median imputation
            for col in self.key_columns:
                if self.df[col].isna().sum() > 0:
                    self.df[col].fillna(self.df[col].median(), inplace=True)
            
            # Drop rows with remaining missing values in key columns
            self.df.dropna(subset=self.key_columns, inplace=True)
            
            # Remove outliers
            outlier_indices = self.detect_outliers()
            self.df = self.df[~self.df.index.isin(outlier_indices)]
            
            # Save cleaned data
            self.df.to_csv(f'data/{self.country}_clean.csv', index=False)
            return self.df
        except Exception as e:
            print(f"Error cleaning {self.country} data: {e}")
            return None