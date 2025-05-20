import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from app.utils import load_data, process_data

st.set_page_config(
    page_title="Solar Data Analysis Dashboard",
    page_icon="☀️",
    layout="wide"
)

def main():
    st.title("Solar Data Analysis Dashboard")
    st.write("Analysis of solar farm data from Benin, Sierra Leone, and Togo")

    # Sidebar for country selection
    country = st.sidebar.selectbox(
        "Select Country",
        ["Benin", "Sierra Leone", "Togo", "Compare All"]
    )

    if country == "Compare All":
        show_comparison()
    else:
        show_country_analysis(country)

def show_country_analysis(country):
    # Load and process data
    df = load_data(country)
    if df is None:
        st.error(f"No data available for {country}")
        return

    # Display basic statistics
    st.subheader(f"Basic Statistics for {country}")
    st.write(df.describe())

    # Time series plot
    st.subheader("Solar Radiation Over Time")
    fig = px.line(df, x='Timestamp', y=['GHI', 'DNI', 'DHI'],
                  title=f'Solar Radiation in {country}')
    st.plotly_chart(fig)

    # Temperature and Wind Analysis
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Temperature Distribution")
        fig = px.histogram(df, x='Tamb', title='Temperature Distribution')
        st.plotly_chart(fig)

    with col2:
        st.subheader("Wind Speed Distribution")
        fig = px.histogram(df, x='WS', title='Wind Speed Distribution')
        st.plotly_chart(fig)

def show_comparison():
    st.subheader("Country Comparison")
    
    # Load data for all countries
    countries = ["Benin", "Sierra Leone", "Togo"]
    data = {}
    
    for country in countries:
        df = load_data(country)
        if df is not None:
            data[country] = df

    if not data:
        st.error("No data available for comparison")
        return

    # Compare average GHI
    st.write("Average Global Horizontal Irradiance (GHI) by Country")
    avg_ghi = {country: df['GHI'].mean() for country, df in data.items()}
    fig = px.bar(x=list(avg_ghi.keys()), y=list(avg_ghi.values()),
                 title='Average GHI by Country')
    st.plotly_chart(fig)

if __name__ == "__main__":
    main() 