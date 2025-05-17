import pandas as pd
import numpy as np

class DataCleaner:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)
        self.original_shape = self.df.shape
        
    def handle_missing_values(self, threshold=0.05):
        """Handle missing values using median imputation or dropping"""
        for col in self.df.columns:
            if self.df[col].isna().mean() > threshold:
                self.df.drop(col, axis=1, inplace=True)
            else:
                self.df[col].fillna(self.df[col].median(), inplace=True)
        return self.df
    
    def remove_outliers(self, columns, z_threshold=3):
        """Remove outliers using Z-score method"""
        for col in columns:
            z_scores = np.abs((self.df[col] - self.df[col].mean()) / self.df[col].std())
            self.df = self.df[z_scores < z_threshold]
        return self.df
    
    def get_cleaning_report(self):
        """Generate cleaning summary report"""
        cleaned_shape = self.df.shape
        return {
            'original_rows': self.original_shape[0],
            'cleaned_rows': cleaned_shape[0],
            'rows_removed': self.original_shape[0] - cleaned_shape[0]
        }