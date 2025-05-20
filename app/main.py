import streamlit as st
import pandas as pd
from app.utils import load_data, plot_boxplot, plot_time_series

st.title('Solar Data Discovery Dashboard')

# Country selection
countries = ['Benin', 'Sierra Leone', 'Togo']
selected_countries = st.multiselect('Select Countries', countries, default=countries)

# Load data
dfs = [load_data(country.lower()) for country in selected_countries]
valid_dfs = [df for df in dfs if df is not None]
valid_countries = [country for df, country in zip(dfs, selected_countries) if df is not None]

# Boxplots
if valid_dfs:
    for metric in ['GHI', 'DNI', 'DHI']:
        st.plotly_chart(plot_boxplot(valid_dfs, valid_countries, metric))

# Time series for each country
for df, country in zip(valid_dfs, valid_countries):
    st.subheader(f'{country} Time Series')
    metric = st.selectbox(f'Select Metric for {country}', ['GHI', 'DNI', 'DHI', 'Tamb'], key=country)
    st.plotly_chart(plot_time_series(df, country, metric))

# Top regions table (simplified, assumes GHI as key metric)
if valid_dfs:
    summary = []
    for df, country in zip(valid_dfs, valid_countries):
        summary.append({
            'Country': country,
            'Average GHI': df['GHI'].mean(),
            'Median GHI': df['GHI'].median()
        })
    st.subheader('Top Regions by GHI')
    st.dataframe(pd.DataFrame(summary))