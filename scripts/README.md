# Scripts

This directory contains utility scripts for data processing and analysis.

## process_data.py

This script processes the raw solar data files for each country. It performs the following tasks:

1. Reads raw CSV files from the `data/raw` directory
2. Cleans the data by:
   - Handling missing values using median imputation
   - Removing outliers using the IQR method
3. Saves processed data to the `data` directory

### Usage

```bash
python scripts/process_data.py
```

The script will process data for all three countries (Benin, Sierra Leone, and Togo) and save the cleaned data files in the `data` directory.

### Input Data Format

The input CSV files should contain the following columns:
- Timestamp: Date and time of the measurement
- GHI: Global Horizontal Irradiance
- DNI: Direct Normal Irradiance
- DHI: Diffuse Horizontal Irradiance
- Tamb: Ambient Temperature
- WS: Wind Speed
- WD: Wind Direction
- BP: Barometric Pressure

### Output

The script generates cleaned CSV files with the following naming convention:
- `benin_clean.csv`
- `sierra_leone_clean.csv`
- `togo_clean.csv`
