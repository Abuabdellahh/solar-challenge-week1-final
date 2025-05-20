# Jupyter Notebooks

This directory contains Jupyter notebooks for data analysis and visualization.

## Notebooks

1. `benin_eda.ipynb`: Exploratory Data Analysis for Benin's solar data
   - Data loading and initial inspection
   - Summary statistics and missing value analysis
   - Outlier detection and cleaning
   - Time series analysis
   - Correlation analysis
   - Monthly and hourly patterns

2. `sierra_leone_eda.ipynb`: Exploratory Data Analysis for Sierra Leone's solar data
   - Similar structure to Benin's EDA
   - Country-specific insights and patterns

3. `togo_eda.ipynb`: Exploratory Data Analysis for Togo's solar data
   - Similar structure to Benin's EDA
   - Country-specific insights and patterns

4. `compare_countries.ipynb`: Comparative Analysis
   - Cross-country comparison of solar potential
   - Comparative visualization of key metrics
   - Identification of high-potential regions

## Running the Notebooks

1. Make sure you have Jupyter installed:
```bash
pip install jupyter
```

2. Start Jupyter Notebook:
```bash
jupyter notebook
```

3. Navigate to the notebooks directory and open the desired notebook.

## Data Requirements

The notebooks expect the following data files in the `data` directory:
- `benin_clean.csv`
- `sierra_leone_clean.csv`
- `togo_clean.csv`

These files should be generated using the `process_data.py` script in the `scripts` directory.
