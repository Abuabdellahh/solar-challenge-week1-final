Solar Data Discovery - Week 1 Challenge
This repository contains the implementation of the Solar Data Discovery challenge for MoonLight Energy Solutions. It includes data profiling, cleaning, exploratory data analysis (EDA), cross-country comparison, and an optional Streamlit dashboard for solar radiation data from Benin, Sierra Leone, and Togo.
Repository Structure

.github/workflows/ci.yml: GitHub Actions workflow for CI/CD.
src/: Python scripts for data cleaning, EDA, and comparison.
notebooks/: Jupyter notebooks for EDA and cross-country comparison.
app/: Streamlit dashboard application.
tests/: Unit tests for data cleaning functions.
data/: Contains datasets (not committed, ignored via .gitignore).

Setup Instructions

Clone the Repository:git clone https://github.com/your-username/solar-challenge-week1.git
cd solar-challenge-week1


Set Up Virtual Environment:python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:pip install -r requirements.txt


Place Datasets:
Place benin.csv, sierraleone.csv, and togo.csv in the data/ folder.


Run Notebooks:
Open notebooks/ in Jupyter and run <country>_eda.ipynb for each country and compare_countries.ipynb for cross-country analysis.


Run Streamlit Dashboard:streamlit run app/main.py


Deploy to Streamlit Community Cloud (see app/ instructions).



Contributions

Git Setup: Initialized repository with branches (setup-task, eda-<country>, compare-countries, dashboard-dev).
EDA: Performed data profiling, cleaning, and visualization for each country.
Comparison: Conducted cross-country analysis with boxplots and summary statistics.
Dashboard: Built an interactive Streamlit app to visualize insights.

Usage

Run EDA notebooks for individual country analysis.
Run compare_countries.ipynb for cross-country comparisons.
Access the Streamlit dashboard for interactive visualizations.

Deployment

The Streamlit app is deployed at [Streamlit Community Cloud URL] (replace with actual URL after deployment).

