import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def load_data(country):
    """Load cleaned dataset for a given country."""
    try:
        df = pd.read_csv(f'data/{country}_clean.csv')
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        return df
    except Exception as e:
        print(f"Error loading {country} data: {e}")
        return None

def plot_boxplot(dfs, countries, metric):
    """Generate boxplot for a metric across countries."""
    combined = pd.concat([df.assign(Country=country) for df, country in zip(dfs, countries)])
    fig = px.box(combined, x='Country', y=metric, title=f'{metric} Comparison Across Countries')
    return fig

def plot_time_series(df, country, metric):
    """Generate time series plot for a metric."""
    fig = px.line(df, x='Timestamp', y=metric, title=f'{metric} Time Series - {country}')
    return fig