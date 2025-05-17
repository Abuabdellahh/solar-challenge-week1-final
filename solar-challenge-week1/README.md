# Solar Challenge Week 1

This repository contains code and resources for the Solar Challenge Week 1 project. The goal is to analyze and visualize solar energy data for different countries.

## Project Structure

```
solar-challenge-week1/
├── .github/
│   └── workflows/
│       └── ci.yml
├── data/                   # Ignored via .gitignore
├── notebooks/
│   ├── benin_eda.ipynb
│   ├── sierraleone_eda.ipynb
│   ├── togo_eda.ipynb
│   └── compare_countries.ipynb
├── src/
│   ├── data_cleaner.py     # Modular code for cleaning
│   └── visualization.py    # Reusable plotting functions
├── tests/                  # Unit tests (optional)
├── .gitignore
├── requirements.txt
└── README.md
```

- **data/**: Contains raw and processed data files (not tracked by git).
- **notebooks/**: Jupyter notebooks for exploratory data analysis (EDA) and comparison.
- **src/**: Source code for data cleaning and visualization utilities.
- **tests/**: (Optional) Unit tests for the codebase.
- **.github/workflows/**: CI/CD configuration files.

## Getting Started

1. Clone the repository.
2. Install dependencies from `requirements.txt`.
3. Explore the notebooks in the `notebooks/` directory.

## Requirements
See `requirements.txt` for Python dependencies.
