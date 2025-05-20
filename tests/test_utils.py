import pytest
import pandas as pd
import numpy as np
from app.utils import process_data, calculate_solar_potential

def test_process_data():
    # Create sample data
    data = {
        'Timestamp': pd.date_range(start='2023-01-01', periods=5, freq='H'),
        'GHI': [100, 200, np.nan, 300, 400],
        'DNI': [50, 150, 250, 350, 450],
        'Tamb': [25, 26, 27, 28, 29]
    }
    df = pd.DataFrame(data)
    
    # Process the data
    processed_df = process_data(df)
    
    # Check if missing values are handled
    assert processed_df['GHI'].isnull().sum() == 0
    
    # Check if data types are preserved
    assert isinstance(processed_df['Timestamp'], pd.DatetimeIndex)
    assert isinstance(processed_df['GHI'], pd.Series)
    
    # Check if outliers are handled
    assert processed_df['DNI'].max() <= 450
    assert processed_df['DNI'].min() >= 50

def test_calculate_solar_potential():
    # Create sample data
    data = {
        'GHI': [100, 200, 300, 400, 500],
        'DNI': [50, 150, 250, 350, 450],
        'DHI': [25, 75, 125, 175, 225],
        'Tamb': [25, 26, 27, 28, 29],
        'WS': [2, 3, 4, 5, 6]
    }
    df = pd.DataFrame(data)
    
    # Calculate metrics
    metrics = calculate_solar_potential(df)
    
    # Check if all metrics are calculated
    assert 'avg_ghi' in metrics
    assert 'max_ghi' in metrics
    assert 'avg_dni' in metrics
    assert 'max_dni' in metrics
    assert 'avg_dhi' in metrics
    assert 'max_dhi' in metrics
    assert 'avg_temp' in metrics
    assert 'avg_wind_speed' in metrics
    
    # Check if calculations are correct
    assert metrics['avg_ghi'] == 300
    assert metrics['max_ghi'] == 500
    assert metrics['avg_temp'] == 27 