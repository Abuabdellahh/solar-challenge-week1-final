import pandas as pd
import numpy as np
from pathlib import Path

def load_data(country):
    """
    Load data for a specific country.
    
    Args:
        country (str): Name of the country (Benin, Sierra Leone, or Togo)
    
    Returns:
        pd.DataFrame: Processed data for the country
    """
    try:
        # Convert country name to filename format
        filename = country.lower().replace(" ", "_") + "_clean.csv"
        filepath = Path("data") / filename
        
        if not filepath.exists():
            return None
            
        df = pd.read_csv(filepath, parse_dates=['Timestamp'])
        return process_data(df)
    except Exception as e:
        print(f"Error loading data for {country}: {str(e)}")
        return None

def process_data(df):
    """
    Process the data by handling missing values and outliers.
    
    Args:
        df (pd.DataFrame): Raw data
    
    Returns:
        pd.DataFrame: Processed data
    """
    # Make a copy to avoid modifying the original
    df_processed = df.copy()
    
    # Handle missing values
    numeric_columns = df_processed.select_dtypes(include=[np.number]).columns
    for col in numeric_columns:
        if df_processed[col].isnull().sum() > 0:
            df_processed[col] = df_processed[col].fillna(df_processed[col].median())
    
    # Handle outliers using IQR method
    for col in numeric_columns:
        Q1 = df_processed[col].quantile(0.25)
        Q3 = df_processed[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        df_processed[col] = df_processed[col].clip(lower_bound, upper_bound)
    
    return df_processed

def calculate_solar_potential(df):
    """
    Calculate solar potential metrics.
    
    Args:
        df (pd.DataFrame): Processed data
    
    Returns:
        dict: Dictionary containing solar potential metrics
    """
    metrics = {
        'avg_ghi': df['GHI'].mean(),
        'max_ghi': df['GHI'].max(),
        'avg_dni': df['DNI'].mean(),
        'max_dni': df['DNI'].max(),
        'avg_dhi': df['DHI'].mean(),
        'max_dhi': df['DHI'].max(),
        'avg_temp': df['Tamb'].mean(),
        'avg_wind_speed': df['WS'].mean()
    }
    
    return metrics 