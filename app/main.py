import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Solar Data Dashboard')

@st.cache
def load_data():
    benin = pd.read_csv('data/benin_clean.csv')
    sierra = pd.read_csv('data/sierraleone_clean.csv')
    togo = pd.read_csv('data/togo_clean.csv')
    return pd.concat([
        benin.assign(country='Benin'),
        sierra.assign(country='Sierra Leone'),
        togo.assign(country='Togo')
    ])

df = load_data()
selected = st.multiselect('Countries', df['country'].unique(), default=df['country'].unique())

if selected:
    fig, ax = plt.subplots()
    sns.boxplot(x='country', y='GHI', data=df[df['country'].isin(selected)], ax=ax)
    st.pyplot(fig)