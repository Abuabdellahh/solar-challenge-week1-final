# Solar Data Discovery Challenge

This repository contains analysis of solar farm data from Benin, Sierra Leone, and Togo for MoonLight Energy Solutions. The project aims to identify high-potential regions for solar installation through data analysis and visualization.

## Project Structure

```
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows/
│       └── ci.yml
├── src/
│   └── __init__.py
├── notebooks/
│   ├── __init__.py
│   ├── benin_eda.ipynb
│   ├── sierra_leone_eda.ipynb
│   ├── togo_eda.ipynb
│   └── compare_countries.ipynb
├── tests/
│   └── __init__.py
├── scripts/
│   ├── __init__.py
│   └── README.md
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── utils.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Environment Setup

### Prerequisites
- Python 3.8+
- Git

### Setting up the development environment

1. Clone the repository:
```bash
git clone https://github.com/Abuabdellahh/solar-challenge-week1-final 
cd solar-challenge-week1
```

2. Create and activate a virtual environment:
```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Data Analysis

The project includes:
- Data profiling and cleaning for each country
- Exploratory Data Analysis (EDA) to identify patterns and insights
- Cross-country comparison to identify high-potential regions
- Interactive dashboard for visualization (optional)

## Running the Streamlit Dashboard

To run the Streamlit dashboard locally:

```bash
streamlit run app/main.py
```

## Contributors

- Your Name
