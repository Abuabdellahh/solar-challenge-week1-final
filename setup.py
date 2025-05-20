from setuptools import setup, find_packages

setup(
    name="solar-data-analysis",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "streamlit",
        "pandas",
        "plotly",
        "numpy",
        "scipy",
        "matplotlib",
        "seaborn"
    ],
) 