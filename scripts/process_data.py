import pandas as pd
import numpy as np
from pathlib import Path
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def process_country_data(country):
    """
    Process data for a specific country.
    
    Args:
        country (str): Name of the country
    """
    try:
        # Convert country name to filename format
        filename = country.lower().replace(" ", "_") + ".csv"
        input_path = Path("data/raw") / filename
        output_path = Path("data") / f"{country.lower().replace(' ', '_')}_clean.csv"
        
        if not input_path.exists():
            logger.error(f"Input file not found: {input_path}")
            return
            
        # Read the data
        logger.info(f"Processing data for {country}")
        df = pd.read_csv(input_path, parse_dates=['Timestamp'])
        
        # Basic cleaning
        df = clean_data(df)
        
        # Save processed data
        output_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(output_path, index=False)
        logger.info(f"Processed data saved to {output_path}")
        
    except Exception as e:
        logger.error(f"Error processing data for {country}: {str(e)}")

def clean_data(df):
    """
    Clean the data by handling missing values and outliers.
    
    Args:
        df (pd.DataFrame): Raw data
    
    Returns:
        pd.DataFrame: Cleaned data
    """
    # Make a copy to avoid modifying the original
    df_clean = df.copy()
    
    # Handle missing values
    numeric_columns = df_clean.select_dtypes(include=[np.number]).columns
    for col in numeric_columns:
        if df_clean[col].isnull().sum() > 0:
            df_clean[col] = df_clean[col].fillna(df_clean[col].median())
    
    # Handle outliers using IQR method
    for col in numeric_columns:
        Q1 = df_clean[col].quantile(0.25)
        Q3 = df_clean[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        df_clean[col] = df_clean[col].clip(lower_bound, upper_bound)
    
    return df_clean

def main():
    """Process data for all countries."""
    countries = ["Benin", "Sierra Leone", "Togo"]
    
    for country in countries:
        process_country_data(country)

if __name__ == "__main__":
    main() 